import base_controller
from pprint import pprint
from gevent import monkey;monkey.patch_all()
from httpexe import httpexe
class Template_Flavor_Controller(base_controller.Controller):
    def __init__(self,sendobj):
        super(Template_Flavor_Controller, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'flavor_template'
        self.attrs = {'name','ram','vcpus','disk'}
    def create(self,req):

        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result :
            return result

        self.message['cmdtype'] = 'create'
        content = dict()
        content['flavor'] = eval(str(req.json_body))
        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message

    def delete(self,req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['flavor'] = dict()
        content['flavor']['name'] = req.json_body['name']
        content['flavor']['ram'] = req.json_body['ram']
        content['flavor']['vcpus'] = req.json_body['vcpus']
        content['flavor']['disk'] = req.json_body['disk']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return self.message


class Template_Image_Controller(base_controller.Controller):
    def __init__(self, sendobj):
        super(Template_Image_Controller, self).__init__(sendobj)
        self.message = dict()
        self.message['optype'] = 'image_template'
        self.attrs = {'container_format','disk_format','disk_format','name','min_ram','visibility','min_disk','filename'}

    def create(self, req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'create'
        content = dict()
        content['image'] = dict()
        content['image']['container_format'] = req.json_body['container_format']
        content['image']['disk_format'] = req.json_body['disk_format']
        content['image']['name'] = req.json_body['name']
        content['image']['min_ram'] = req.json_body['min_ram']
        content['image']['visibility'] = req.json_body['visibility']
        content['image']['min_disk'] = req.json_body['min_disk']
        content['filename'] = req.json_body['filename']

        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        result = self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return result

    def delete(self, req):
        error = httpexe(req)
        result = error.check_keys(self.attrs)
        if result:
            return result
        self.message['cmdtype'] = 'delete'
        content = dict()
        content['image'] = dict()
        content['image']['container_format'] = req.json_body['container_format']
        content['image']['disk_format'] = req.json_body['disk_format']
        content['image']['name'] = req.json_body['name']
        content['image']['min_ram'] = req.json_body['min_ram']
        content['image']['visibility'] = req.json_body['visibility']
        content['image']['min_disk'] = req.json_body['min_disk']
        content['filename'] = req.json_body['filename']


        self.message['content'] = content
        #pprint(self.message)
        pprint("Build create message!")
        result = self.sendobj.call(self.message)
        # gevent.joinall(gevent.spawn(self.sendobj.call, self.message))
        # res = self.sendobj.call(self.message)
        pprint("send create message to receive thread!")
        return result


