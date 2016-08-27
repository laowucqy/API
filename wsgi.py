import routes.middleware
import webob.dec
import webob.exc
from pprint import pprint

class Router(object):

    def __init__(self, mapper):
        self.map = mapper
        self._router = routes.middleware.RoutesMiddleware(self._dispatch, self.map)

    @classmethod
    def factory(cls, global_conf, **local_conf):
        return cls()

    @webob.dec.wsgify
    def __call__(self, req):
        return self._router

    @staticmethod
    @webob.dec.wsgify
    def _dispatch(req):
        match = req.environ['wsgiorg.routing_args'][1]
        if not match:
            res = webob.exc.HTTPNotFound()
            pprint(res.__dict__)
            return res
        app = match['controller']
        return app