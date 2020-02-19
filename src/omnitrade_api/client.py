import requests
import json
from auth import Auth

OMNITRADE_URL = 'https://omnitrade.io'
class Client(object):
    def __init__(self, options={}):
        global OMNITRADE_URL
        self.setup_auth_keys(options)

        self.endpoint  = options['endpoint'] if 'endpoint' in options.keys() else OMNITRADE_URL
        self.timeout   =  options['timeout'] if 'timeout' in options.keys() else 60 

    def get_public(self, path, params={}):
        uri = self.parameters('GET',path, params)

        return self.get_request(uri, params)


    def get(self, path, params={}):
        self.check_auth()

        uri, params = self.parameters('GET',path, params)
        return self.get_request(uri, params)
    
    def post(self, path, params={}):
        self.check_auth()

        uri, params = self.parameters('POST', path, params)
        return self.post_request(uri, params)

    def setup_auth_keys(self, options):
        if not('access_key' in options.keys() and 'secret_key' in options.keys()):
            return

        self.access_key = options['access_key']
        self.secret_key = options['secret_key']
        self.auth       = Auth(self.access_key, self.secret_key)


    def check_auth(self):
        if self.auth == None:
            raise Exception('Missing access key and/or secret key')
    
    def get_request(self, uri, params):
        return requests.get(uri,data = params).json()

    def post_request(self, uri, params):
        return requests.post(uri,data = params).json()

    def parameters(self, action, path, params):
        uri = '{endpoint}{path}'.format(endpoint=self.endpoint, path=path)
        params = self.auth.signed_params(action, path, params) if self.auth else params
        return uri, params
