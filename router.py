import routes
import wsgi
import resource_account
import roles_resource
from rpc_client import RpcClient

class account(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::account')
        account_controller = resource_account.AccountController(sendobj)
        mapper.connect("/", controller=account_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/{user_name}", controller=account_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/{user_name}", controller=account_controller, action="delete",conditions={'method': ['DELETE']})
        super(account, self).__init__(mapper)

class flavor(wsgi.Router):

    def __init__(self,mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::template::flavor')


class roles(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('role')
        role_controller = roles_resource.RoleController(sendobj)
        mapper.connect("/", controller=role_controller, action="create",conditions={'method': ['POST']})
        mapper.connect("/{roles_id}", controller=role_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/{roles_id}", controller=role_controller, action="delete",conditions={'method': ['DELETE']})
        super(roles, self).__init__(mapper)


