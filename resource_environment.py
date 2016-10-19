import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()

class Environment_Controller(base_controller.Controller):
    def __init__(self, sendobj):
        super(Environment_Controller, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'environment'

    def create(self,req):
        self.message['cmdtype'] = 'create'
        content = dict()
        content['environment'] = dict()
        content['environment']['template_id'] = req.json_body['template_id']
        content['environment']['target_id'] = req.json_body['target_id']
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
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['environment'] = dict()
        content['environment']['template_id'] = req.json_body['template_id']
        content['environment']['target_id'] = req.json_body['target_id']
        content['environment']['user_id'] = req.json_body['user_id']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message