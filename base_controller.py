import httplib
import simplejson
import webob.dec
from webob import Response
from rpc_client import FibonacciRpcClient

class Controller(object):
    def __init__(self, sendobj):
        self.sendobj = sendobj


    def index(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        #response = Response(request=req, status=httplib.MULTIPLE_CHOICES,
        #                   content_type='application/json')
        #fibonacci_rpc = FibonacciRpcClient()
        #ans = self.sendobj.call(self.mes, self.rpc_queue)
        #response.body = json.dumps(ans)
        action = match.pop('action')
        del match['controller']

        method = getattr(self, action)
        result = method(req, **match)

        if result is None:
            return webob.Response(body='',
                                  status='204 Not Found',
                                  headerlist=[('Content-Type',
                                               'application/json')])
        else:
            if not isinstance(result, basestring):
                result = simplejson.dumps(result)
            return result

    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)