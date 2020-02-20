import requests
import json
import urllib
from auth import Auth
from ordered_dict import ordered_dict

OMNITRADE_URL = 'http://localhost:5000'#'https://omnitrade.io'
class Client(object):
    def __init__(self, options={}):
        global OMNITRADE_URL
        self.auth = None
        self.__setup_auth_keys(options)

        self.endpoint  =    options['endpoint'] if 'endpoint' in options.keys() else OMNITRADE_URL
        self.timeout   =    options['timeout'] if 'timeout' in options.keys() else 60 

    def get_public(self, path, params={}):
        uri, params = self.__parameters('GET',path, params)

        return self.__get_request(uri, params)


    def get(self, path, params={}):
        self.__check_auth()

        uri, params = self.__parameters('GET',path, params)
        return self.__get_request(uri, params)
    
    def post(self, path, params={}):
        self.__check_auth()

        uri, params = self.__parameters('POST', path, params)
        return self.__post_request(uri, params)

    def __setup_auth_keys(self, options):
        if not('access_key' in options.keys() and 'secret_key' in options.keys()):
            return

        self.access_key = options['access_key']
        self.secret_key = options['secret_key']
        self.auth       = Auth(self.access_key, self.secret_key)


    def __check_auth(self):
        if self.auth == None:
            raise Exception('Missing access key and/or secret key')
    
    def __get_request(self, uri, params):
        return requests.get(uri, params = urllib.urlencode(params))

    def __post_request(self, uri, params):
        print(uri)
        print(params)
        return requests.post(uri, params = urllib.urlencode(params))

    def __parameters(self, action, path, params):
        uri = '{endpoint}{path}'.format(endpoint=self.endpoint, path=path)
        print('Com auth\n')
        print(self.auth.signed_params(action, path, params))
        dict_params = self.auth.signed_params(action, path, params) if self.auth != None else params

        return uri, ordered_dict(dict_params)

    
