import re
import os
import webob.dec
from LOG import LOG
from pprint import pprint
class filter_factory(object):
    def __init__(self, app):
        self.app = app

    @classmethod
    def factory(cls,global_conf, **kwargs):
        def filter(app):
            return cls(app)
        return filter


class filter01(filter_factory):
    def __init__(self,app):
        super(filter01, self).__init__(app)

    def __call__(self, environ, start_response):
        print 'request method is: %s' % environ['REQUEST_METHOD']
        return self.app(environ, start_response)


