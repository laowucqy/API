import routes
import wsgi
import account_resource
import roles_resource
from rpc_client import FibonacciRpcClient

class account(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = FibonacciRpcClient('account')
        account_controller = account_resource.AccountController(sendobj)
        mapper.connect("/", controller=account_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/{user_name}/passwd", controller=account_controller, action="update", conditions={'method': ['POST']})
        mapper.connect("/{user_name}", controller=account_controller, action="show", conditions={'method': ['GET']})
        mapper.connect("/", controller=account_controller, action="list",conditions={'method': ['GET']})
        mapper.connect("/{user_name}", controller=account_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/{user_name}", controller=account_controller, action="delete",conditions={'method': ['DELETE']})
        super(account, self).__init__(mapper)


class roles(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = FibonacciRpcClient('role')
        role_controller = roles_resource.RoleController(sendobj)
        mapper.connect("/", controller=role_controller, action="create",conditions={'method': ['POST']})
        mapper.connect("/", controller=role_controller, action="list",conditions={'method': ['GET']})
        mapper.connect("/{roles_id}", controller=role_controller, action="show",conditions={'method': ['GET']})
        mapper.connect("/{roles_id}", controller=role_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/{roles_id}", controller=role_controller, action="delete",conditions={'method': ['DELETE']})
        super(roles, self).__init__(mapper)


