
import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()
import gevent

class RoleController(base_controller.Controller):
    def __init__(self,sendobj):
        super(RoleController, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'flavor_templet'

    def create(self, req):
        self.message['cmdtype'] = 'create'
        self.message['user'] = req.headers.get('X-User-Id')
        content = dict()
        self.message['content'] = content
        pprint(self.message)
        pprint("Build create message!")
        #gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return content


    def delete(self, req):
        content = dict()
        return content

    def update(self, req):
        content = dict()
        return content
