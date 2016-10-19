import os
import sys
from paste import deploy
from wsgiref.simple_server import make_server
from threading import Thread
import eventlet
import eventlet.wsgi
import greenlet


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
    def __init__(self, app, host, port):
        self._pool = eventlet.GreenPool(1000)
        self.app = app
        self._socket = eventlet.listen((host, port), backlog=100)
        (self.host, self.port) = self._socket.getsockname()
        print("Listening on %(host)s:%(port)s" % self.__dict__)

    def start(self):
        self._server = eventlet.spawn(eventlet.wsgi.server,
                                      self._socket,
                                      self.app,
                                      protocol=eventlet.wsgi.HttpProtocol,
                                      custom_pool=self._pool)

    def stop(self):
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

