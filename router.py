import routes
import wsgi
import resource
from rpc_client import RpcClient

attrs_account = {'name','email','password'}
attrs_quota  =  {'name','force','instances'}
attrs_environment = {'template_id','user_id'}
attrs_image = {'container_format','disk_format','disk_format','name','min_ram','visibility','min_disk','filename'}
attrs_flavor = {'name','ram','vcpus','disk'}


class user(wsgi.Router):

    def __init__(self, mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj_account = RpcClient('amqp::user::account')
        account_controller = resource.Controller(sendobj_account,'account',attrs_account)
        mapper.connect("/account", controller=account_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/account", controller=account_controller, action="update",conditions={'method': ['PATCH']})
        mapper.connect("/account", controller=account_controller, action="delete",conditions={'method': ['DELETE']})
        sendobj_quota = RpcClient('amqp::user::quota')
        quota_controller = resource.Controller(sendobj_quota,'quota',attrs_quota)
        mapper.connect("/quota", controller=quota_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/quota", controller=quota_controller, action="delete", conditions={'method': ['DELETE']})
        super(user, self).__init__(mapper)

class template(wsgi.Router):

    def __init__(self,mapper=None):
        if(mapper is None):
            mapper = routes.Mapper()
        sendobj_flavor = RpcClient('amqp::template::flavor')
        template_flavor_controller = resource.Controller(sendobj_flavor,'flovor',attrs_flavor)
        mapper.connect("/flavor", controller=template_flavor_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/flavor", controller=template_flavor_controller, action="delete",conditions={'method': ['DELETE']})
        mapper.connect("/flavor", controller=template_flavor_controller, action="update",conditions={'method': ['UPDATE']})
        sendobj_image = RpcClient('amqp::template::image')
        template_image_controller = resource.Controller(sendobj_image,'image',attrs_image)
        mapper.connect("/image", controller=template_image_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/image", controller=template_image_controller, action="delete", conditions={'method': ['DELETE']})
        mapper.connect("/image", controller=template_image_controller, action="update",conditions={'method': ['UPDATE']})
        super(template, self).__init__(mapper)

class environment(wsgi.Router):
    def __init__(self, mapper=None):
        if (mapper is None):
            mapper = routes.Mapper()
        sendobj = RpcClient('amqp::environment')
        environment_controller = resource.Controller(sendobj,'environment',attrs_environment)
        mapper.connect("/environment", controller=environment_controller, action="create", conditions={'method': ['POST']})
        mapper.connect("/environment", controller=environment_controller, action="delete", conditions={'method': ['DELETE']})
        mapper.connect("/environment/start", controller=environment_controller, action="start", conditions={'method': ['POST']})
        mapper.connect("/environment/shutdown", controller=environment_controller, action="shutdown", conditions={'method': ['POST']})
        super(environment, self).__init__(mapper)



