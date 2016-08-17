import base_controller
from pprint import pprint

class AccountController(base_controller.Controller):
    def __init__(self,sendobj):
        super(AccountController, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'account'

    def create(self, req):
        self.message['cmdtype'] = 'create'
        #self.message['user'] = req.headers.get('X-User-Id')

        content = dict()
        content['userName'] = req.json_body['user_name']
        content['password'] = req.json_body['password']
        content['email'] = req.json_body['email']

        self.message['content'] = content
        pprint(self.message)
        pprint("Build create message!")

        res = self.sendobj.call(self.message)
        print res
        pprint("send create message to receive thread!")
        return content

    def show(self, req):
        content = dict()
        return content

    def list(self, req):
        self.message['cmdtype'] = 'list'
        pprint(self.message)
        pprint("Build list message!")

        self.sendobj.call(self.message)
        pprint("Send list message to receive thread!")

        # return response
        return self.message
    def delete(self, req ,user_name):
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['userName'] = user_name
        self.message['content'] = content
        pprint(self.message)
        pprint("Build delete message!")

        self.sendobj.call(self.message)
        pprint("Send delete message to receive thread!")

        # return response
        return self.message

    def update(self, req, user_name):
        self.message['cmdtype'] = 'update'
        content = dict()
        content['user_name'] = user_name
        self.message['content'] = content
        pprint(self.message)
        pprint("Build update message!")

        self.sendobj.call(self.message)
        pprint("Send delete message to receive thread!")

        # return response
        return self.message