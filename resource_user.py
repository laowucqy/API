import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()
import gevent
from httpexe import httpexe

class AccountController(base_controller.Controller):
    def __init__(self,sendobj):
        super(AccountController, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'account'
        self.attrs = {'name','email','password'}
    def create(self, req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'create'
        #self.message['user'] = req.headers.get('X-User-Id')

        content = dict()
        content['user'] = dict()
        content['user']['name'] = req.json_body['name']
        content['user']['email'] = req.json_body['email']
        content['user']['password'] = req.json_body['password']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        #gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        #res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message


    def delete(self, req ):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['user'] = dict()
        content['user']['name'] = req.json_body['name']
        content['user']['email'] = req.json_body['email']
        content['user']['password'] = req.json_body['password']
        self.message['content'] = content
        #pprint(self.message)
        pprint("Build delete message!")
        self.sendobj.call(self.message)
        #gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        pprint("Send delete message to receive thread!")
        # return response
        return self.message

    def update(self, req, user_name):
        self.message['cmdtype'] = 'update'
        content = dict()
        content['user_name'] = user_name
        self.message['content'] = content
        #pprint(self.message)
        pprint("Build update message!")
        self.sendobj.call(self.message)
       # gevent.join(gevent.spawn(self.sendobj.call, self.message))
        pprint("Send delete message to receive thread!")

        # return response
        return self.message

class QuotaController(base_controller.Controller):
    def __init__(self,sendobj):
        super(QuotaController, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'quota'
        self.attrs = {'name','force','instances'}

    def create(self, req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'create'
        # self.message['user'] = req.headers.get('X-User-Id')

        content = dict()
        content['quota_set'] = dict()
        content['quota_set']['name'] = req.json_body['name']
        content['quota_set']['force'] = req.json_body['force']
        content['quota_set']['instances'] = req.json_body['instances']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message

    def delete(self, req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['quota_set'] = dict()
        content['quota_set']['name'] = req.json_body['name']
        self.message['content'] = content
        #pprint(self.message)
        pprint("Build delete message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        pprint("Send delete message to receive thread!")
        # return response
        return self.message