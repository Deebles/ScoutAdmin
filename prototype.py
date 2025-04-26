import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
import tomllib


def main():

    with open("config.toml", mode="rb") as f:
        config = tomllib.load(f)
    with open("keys.toml", mode="rb") as g:
        keys = tomllib.load(g)
    
    client_id = keys["admin_test_beavers"]["id"]
    client_secret = keys["admin_test_beavers"]["secret"]
    token_url = config["auth"]["token"]
    client = BackendApplicationClient(client_id=client_id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=token_url, client_id=client_id, client_secret=client_secret)
    
    #https://www.onlinescoutmanager.co.uk/ext/generic/startup/?action=getData
    #https://onlinescoutmanager.co.uk/ext/members/contact/?action=getListOfMembers?sectionid=77901
    res = oauth.get("https://www.onlinescoutmanager.co.uk/ext/generic/startup/?action=getData")

    print(res.content)

if __name__=="__main__":
    main()