import os
import sys
from paste import deploy
import eventlet
import eventlet.wsgi
import greenlet
import socket
import ConfigParser
from LOG import LOG

LOG = LOG("log.ini",'api')

CONF = ConfigParser.ConfigParser()
CONF.read("api.conf")
module_dir = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]), os.pardir, os.pardir))
sys.path.insert(0, module_dir)
bind_host = CONF.get('api','bind_host')
bind_port = CONF.get('api','bind_port')
pool_size = CONF.get('api','pool_size')
backlog = CONF.get('api','backlog')
def server(app_name):
    app = load_paste_app(app_name, "api.ini")
    #serve = make_server(bind_host, bind_port, app)
    server = Server(app,bind_host,bind_port,int(pool_size),int(backlog))
    server.start()
    server.wait()
    #serve.serve_forever()


class Server(object):
    #default_pool_size = CONF.wsgi_default_pool_size
    def __init__(self, app, host, port ,pool_size ,backlog):
        self.app = app
        self.host = host
        self.port = port
        self._server = None
        self._protocol = eventlet.wsgi.HttpProtocol
        self.pool_size = pool_size #or self.default_pool_size
        self._pool = eventlet.GreenPool(self.pool_size)
        self.backlog = backlog
        #self._max_url_len = max_url_len
        self.client_socket_timeout = 1#or CONF.client_socket_timeout
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
            self._socket = eventlet.listen(bind_addr, family, backlog=int(self.backlog))
            mes = "Listening on %(host)s:%(port)s" % self.__dict__
            #LOG.INFO(mes)
            print(mes)
        except EnvironmentError:
            mes = "Could not bind to %(host)s:%(port)s"
            LOG.ERROR(mes)
            print(mes)
            raise
    def start(self):
        dup_socket = self._socket.dup()
        dup_socket.setsockopt(socket.SOL_SOCKET,
                              socket.SO_REUSEADDR, 1)
        # sockets can hang around forever without keepalive
        dup_socket.setsockopt(socket.SOL_SOCKET,
                              socket.SO_KEEPALIVE, 1)
        wsgi_kwargs = {
            'func':eventlet.wsgi.server,
            'sock':dup_socket,
            'site':self.app,
            'protocol':self._protocol,
            'custom_pool':self._pool,
            'socket_timeout':self.client_socket_timeout
        }
        try:
            self._server = eventlet.spawn(**wsgi_kwargs)
        except OSError:
            mes = "Could not start server "
            LOG.ERROR(mes)

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
        mes = "Could not load app called %(app_name)s at %(conf_file)s"
        raise RuntimeError(str(e))

if __name__ == '__main__':
    app_name = "main"
    conf_file ="api.ini"
    server(app_name)

