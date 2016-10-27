import os
import sys
from paste import deploy
from wsgiref.simple_server import make_server
from threading import Thread
import eventlet
import eventlet.wsgi
import greenlet
import socket

module_dir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir))
sys.path.insert(0, module_dir)
bind_host = "172.29.153.52"
bind_port =8080

def server(app_name):
    app = load_paste_app(app_name, "identity.ini")
    #serve = make_server(bind_host, bind_port, app)
    server = Server(app,bind_host,bind_port)
    server.start()
    server.wait()
    #serve.serve_forever()


class Server(object):
    #default_pool_size = CONF.wsgi_default_pool_size
    def __init__(self, app, host, port ):
        self.app = app
        self._server = None
        self._protocol = eventlet.wsgi.HttpProtocol
        self.pool_size = 1000 #or self.default_pool_size
        self._pool = eventlet.GreenPool(self.pool_size)
        #self._max_url_len = max_url_len
        self.client_socket_timeout = 60#or CONF.client_socket_timeout
        bind_addr=(bind_host,bind_port)
        try:
            info = socket.getaddrinfo(bind_addr[0],
                                      bind_addr[1],
                                      socket.AF_UNSPEC,
                                      socket.SOCK_STREAM)[0]
            family = info[0]
            bind_addr = info[-1]
        except Exception:
            family = socket.AF_INET
        try:
            self._socket = eventlet.listen(bind_addr, family, backlog=128)
            print("Listening on %(host)s:%(port)s" % self.__dict__)
        except EnvironmentError:
            print(("Could not bind to %(host)s:%(port)s"),
                      {'host': host, 'port': port})
            raise

        self._socket = eventlet.listen((host, port), backlog=100)
        (self.host, self.port) = self._socket.getsockname()


    def start(self):
        dup_socket = self._socket.dup()
        dup_socket.setsockopt(socket.SOL_SOCKET,
                              socket.SO_REUSEADDR, 1)
        # sockets can hang around forever without keepalive
        dup_socket.setsockopt(socket.SOL_SOCKET,
                              socket.SO_KEEPALIVE, 1)

        # This option isn't available in the OS X version of eventlet


        wsgi_kwargs = {
            'func':eventlet.wsgi.server,
            'sock':dup_socket,
            'site':self.app,
            'protocol':self._protocol,
            'custom_pool':self._pool,
            'socket_timeout':self.client_socket_timeout
        }

        self._server = eventlet.spawn(**wsgi_kwargs)

    def reset(self):
        """Reset server greenpool size to default.

                :returns: None

                """
        self._pool.resize(self.pool_size)

    def stop(self):
        """Stop this server.

                This is not a very nice action, as currently the method by which a
                server is stopped is by killing its eventlet.

                :returns: None

                """

        if self._server is not None:
            self._pool.resize(0)
            self._server.kill()

    def wait(self):
         try:
            self._server.wait()
         except greenlet.GreenletExit:
            print("WSGI server has stopped.")



def load_paste_app(app_name, conf_file):
    try:
        app = deploy.loadapp("config:%s" % os.path.abspath(conf_file), name=app_name)
        return app
    except(LookupError, ImportError) as e:
        raise RuntimeError(str(e))

if __name__ == '__main__':
    app_name = "main"
    conf_file = "identity.ini"
    server(app_name)

