import hashlib
import time
import urllib

class Auth(object):
    def __init__(self, access_key, secret_key):
        self.access_key = access_key
        self.secret_key = secret_key
    
    def signed_challenge(self, challenge):
        signature = hashlib.pbkdf2_hmac('sha256', self.secret_key,"{access_key}{challenge}".format(access_key = self.access_key, challenge = challenge), 100000 )
        
        return { 'auth': { 'access_key': self.access_key, 'answer': signature } }

    def signed_params(self, verb, path, params = {}):
        params = self.__format_params(params)

        signature = self.__sign(verb, path, urllib.urlencode(params))
        params['signature'] = signature 
        return params

    def __sign(self, verb, path, params):
        return hashlib.pbkdf2_hmac('sha256', self.secret_key, self.__payload(verb, path, params), 100000)

    def __payload(self, verb, path, params):
        return "#{verb}|#{path}|#{params}".format(verb = verb.upper(), path = path, params = params)

    def __format_params(self, params):
        params['access_key'] = self.access_key
        params['tonce'] = int(time.time()) * 1000
        return params
