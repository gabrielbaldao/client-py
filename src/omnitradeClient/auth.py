from platform import python_version
if '2.7' in python_version():
    import urllib
else:
    import urllib.parse as urllib
import hashlib
import hmac
import time

class Auth(object):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
    
    def signed_challenge(self, challenge):
        signature = hmac.new(str(self.secret_key).encode(),"{access_key}{challenge}".format(access_key=self.access_key, challenge=challenge).encode(), hashlib.sha256).hexdigest()
        
        return { 'auth': { 'access_key': self.access_key, 'answer': signature } }

    def signed_params(self, verb, path, **params):
        params = self.__format_params(params)

        signature = self.__sign(verb, path, urllib.urlencode(params))
        params['signature'] = signature 
        return params

    def __sign(self, verb, path, params):
        return hmac.new(self.secret_key.encode(), self.__payload(verb, path, params).encode(), hashlib.sha256).hexdigest()

    def __payload(self, verb, path, params):
        return "{verb}|{path}|{params}".format(verb = verb.upper(), path = path, params = params)

    def __format_params(self, params):
        params['access_key'] = self.access_key
        params['tonce'] = int(time.time()) * 1000
        return params
