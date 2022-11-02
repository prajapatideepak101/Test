from email import charset
from rest_framework import renderers
import json

class UserRenderer(renderers.JSONRenderer):
    charset='utf_8'
    def render(self, data, accepted_media_type=None, renderer_context=None):
        response=''
        if 'Errordetail' in str(data):
            response = json.dumps({'errors':data})
        else:
            response = json.dumps(data)
        return response