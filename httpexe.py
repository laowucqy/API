import simplejson
import json
import webob.dec


class httpexe(object):
    def __init__(self, req):
        self.req = req

    def check_keys(self,keys):
        result = dict()
        for key in keys:
            if key not in self.req.json_body.keys():
                result['error_parameter'] = True
        return result
