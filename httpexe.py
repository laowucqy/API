import simplejson
import json
import webob.dec


class httpexe(object):
    def __init__(self, req):
        self.req = req

    def check_keys(self,key):
        if key in self.req.json_body.keys():
            return True
        else:
            return False

    def check_user_account(self):
        flag = True
        result = dict()
        if not self.check_keys( 'name'):
            flag = False
        if not self.check_keys( 'email'):
            flag = False
        if not self.check_keys( 'password'):
            flag = False
        if not flag:
            result ['error_parameter'] = True
        return result

    def check_user_quota(self):
        flag = True
        result = dict()
        if not self.check_keys('name'):
            flag = False
        if not self.check_keys('force'):
            flag = False
        if not self.check_keys('instances'):
            flag = False
        if not flag:
            result['error_parameter'] = True
        return result

    def check_template_image(self):
        flag = True
        result = dict()
        if not self.check_keys('container_format'):
            flag = False
        if not self.check_keys('disk_format'):
            flag = False
        if not self.check_keys('name'):
            flag = False
        if not self.check_keys('min_ram'):
            flag = False
        if not self.check_keys('visibility'):
            flag = False
        if not self.check_keys('min_disk'):
            flag = False
        if not self.check_keys('filename'):
            flag = False
        if not flag:
            result['error_parameter'] = True
        return result
    def check_template_flavor(self):
        flag = True
        result = dict()
        if not self.check_keys('name'):
            flag = False
        if not self.check_keys('ram'):
            flag = False
        if not self.check_keys('vcpus'):
            flag = False
        if not self.check_keys('disk'):
            flag = False
        if not flag:
            result['error_parameter'] = True
        return result