import httplib
import simplejson
import webob.dec
from pprint import pprint
from webob import Response
from rpc_client import RpcClient
from LOG import LOG
class Controller(object):
    def __init__(self, sendobj):
        self.sendobj = sendobj
        self.LOG = LOG("log.ini",'api')


    def index(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        #response = Response(request=req, status=httplib.MULTIPLE_CHOICES,
        #                   content_type='application/json')
        #pprint (response.__dict__)
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
                result = webob.Response(simplejson.dumps(result))
                mes = self.get_request(req.environ) + self.get_status(result) + self.get_len(req.environ)
                self.LOG.INFO(mes)
                #pprint(result.__dict__)
            return result

    @webob.dec.wsgify
    def __call__(self, request):
        return self.index(request)

    def get_request(self,environ):

        mes =environ['REMOTE_ADDR'] +' '+environ['REQUEST_METHOD']+' '+ environ['SCRIPT_NAME']+' '+environ['PATH_INFO'] +' '+environ['SERVER_PROTOCOL']+' '
        return mes

    def get_status(self,result):
        mes = result._status
        mes = 'status:'+ mes + ' '
        return mes

    def get_len(self,environ):
        mes = str(environ['CONTENT_LENGTH'])
        mes = 'len:' + mes + ' '
        return mes
