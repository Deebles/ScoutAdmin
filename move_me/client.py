import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import tomllib


class OauthClient:
    def __init__(self, id, secret):
        self._id = id
        self._secret = secret
    
    def connection(self):

        
        return oauth