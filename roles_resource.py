import httplib
import json
import webob.dec
from webob import Response
from rpc_client import RpcClient
import base_controller
from pprint import pprint

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

        res = self.sendobj.call(self.message)
        print res
        pprint("send create message to receive thread!")
        return content


    def delete(self, req):
        content = dict()
        return content

    def update(self, req):
        content = dict()
        return content
