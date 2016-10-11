import routes
import wsgi
import resource_user
import roles_resource
import resource_template
import resource_environment
from rpc_client import RpcClient

class account(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::user::quota')
        account_controller = resource_user.AccountController(sendobj)
        mapper.connect("/", controller=account_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/", controller=account_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/", controller=account_controller, action="delete",conditions={'method': ['DELETE']})
        super(account, self).__init__(mapper)

class quota(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::user::quota')
        quota_controller = resource_user.QuotaController(sendobj)
        mapper.connect("/", controller=quota_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/", controller=quota_controller, action="delete",conditions={'method': ['DELETE']})
        super(quota, self).__init__(mapper)

class flavor(wsgi.Router):

    def __init__(self,mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::template::flavor')
        template_flavor_controller = resource_template.Template_Flavor_Controller(sendobj)
        mapper.connect("/", controller=template_flavor_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/", controller=template_flavor_controller, action="delete",conditions={'method': ['DELETE']})
        super(flavor, self).__init__(mapper)

class image(wsgi.Router):

    def __init__(self,mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::template::image')
        template_image_controller = resource_template.Template_Image_Controller(sendobj)
        mapper.connect("/", controller=template_image_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/", controller=template_image_controller, action="delete",conditions={'method': ['DELETE']})
        super(image, self).__init__(mapper)

class environment(wsgi.Router):
    def __init__(self, mapper=None):
        if (mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::environment')
        environment_controller = resource_environment.Environment_Controller(sendobj)
        mapper.connect("/", controller=environment_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/", controller=environment_controller, action="delete", conditions={'method': ['DELETE']})
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


