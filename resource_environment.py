import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()
from httpexe import httpexe
class Environment_Controller(base_controller.Controller):
    def __init__(self, sendobj):
        super(Environment_Controller, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'environment'
        self.attrs = {'template_id','user_id'}
    def create(self,req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'create'
        content = dict()
        content['environment'] = dict()
        content['environment']['template_id'] = req.json_body['template_id']
        content['environment']['user_id'] = req.json_body['user_id']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message


    def delete(self,req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['environment'] = dict()
        content['environment']['template_id'] = req.json_body['template_id']
        content['environment']['user_id'] = req.json_body['user_id']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message