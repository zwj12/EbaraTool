from requests.auth import HTTPDigestAuth
import requests
import xml.etree.ElementTree as ET


class WebServiceConnection:
    __session = None
    __host = None
    __username = None
    __password = None
    __cookies = None

    @staticmethod
    def get_session():
        if WebServiceConnection.__session is None:
            raise Exception("No Session!")
        else:
            return WebServiceConnection.__session

    @staticmethod
    def get_host():
        if WebServiceConnection.__host is None:
            raise Exception("No Host!")
        else:
            return WebServiceConnection.__host

    @staticmethod
    def get_cookies():
        if WebServiceConnection.__cookies is None:
            raise Exception("No Cookies!")
        else:
            return WebServiceConnection.__cookies

    def __init__(self, host, username, password):
        if WebServiceConnection.__session is None:
            WebServiceConnection.__session = requests.Session()
            WebServiceConnection.__host = host
            WebServiceConnection.__username = username
            WebServiceConnection.__password = password
            url = "http://{0}/users".format(host)
            digest_auth = HTTPDigestAuth(username, password)
            resp = WebServiceConnection.__session.get(url, auth=digest_auth)
            WebServiceConnection.__cookies = resp.cookies
        else:
            return
