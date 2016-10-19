import routes
import wsgi
import resource_user
import roles_resource
import resource_template
import resource_environment
from rpc_client import RpcClient

class user(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj_account = RpcClient('amqp::user::account')
        account_controller = resource_user.AccountController(sendobj_account)
        mapper.connect("/account", controller=account_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/account", controller=account_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/account", controller=account_controller, action="delete",conditions={'method': ['DELETE']})
        sendobj_quota = RpcClient('amqp::user::quota')
        quota_controller = resource_user.QuotaController(sendobj_quota)
        mapper.connect("/quota", controller=quota_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/quota", controller=quota_controller, action="delete", conditions={'method': ['DELETE']})
        super(user, self).__init__(mapper)

class template(wsgi.Router):

    def __init__(self,mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj_flavor = RpcClient('amqp::template::flavor')
        template_flavor_controller = resource_template.Template_Flavor_Controller(sendobj_flavor)
        mapper.connect("/flavor", controller=template_flavor_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/flavor", controller=template_flavor_controller, action="delete",conditions={'method': ['DELETE']})
        sendobj_image = RpcClient('amqp::template::image')
        template_image_controller = resource_template.Template_Image_Controller(sendobj_image)
        mapper.connect("/image", controller=template_image_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/image", controller=template_image_controller, action="delete", conditions={'method': ['DELETE']})
        super(template, self).__init__(mapper)

class environment(wsgi.Router):
    def __init__(self, mapper=None):
        if (mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::environment')
        environment_controller = resource_environment.Environment_Controller(sendobj)
        mapper.connect("/environment", controller=environment_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/environment", controller=environment_controller, action="delete", conditions={'method': ['DELETE']})
        super(environment, self).__init__(mapper)

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


