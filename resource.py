import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()
from httpexe import httpexe
class Resource(base_controller.Controller):
    def __init__(self, sendobj, optype, attrs):
        super(Resource, self).__init__(sendobj)
        self.message = dict()
        self.optype = optype
        self.attrs = attrs

    def method(self, req, method):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['optype'] = self.optype
        self.message['cmdtype'] = method
        content = dict()
        content[self.optype] = eval(str(req.json_body))
        self.message['content'] = content
        pprint("Build create message!")
        self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message

class Controller(Resource):
    def __init__(self, sendobj, optype, attrs):
        super(Controller, self).__init__(sendobj, optype, attrs)

    def create(self,req):
        result = super(Controller, self).method(req, 'create')
        return result
    def delete(self,req):
        result = super(Controller, self).method(req, 'delete')
        return result
