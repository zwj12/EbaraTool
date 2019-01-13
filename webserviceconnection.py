from requests.auth import HTTPDigestAuth
import requests
import xml.etree.ElementTree as ET
import json


class WebServiceConnection:
    __session = None
    __host = None
    __port = 80
    __username = None
    __password = None
    __cookies = None
    __system_name = None
    __rw_version = None
    __sysid = None
    __ctrl_name = None
    __ctrl_type = False
    __namespace = '{http://www.w3.org/1999/xhtml}'

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

    @staticmethod
    def get_ctrl_name() -> bool:
        if WebServiceConnection.__ctrl_name is None:
            raise Exception("No Control Name!")
        else:
            return WebServiceConnection.__ctrl_name

    @staticmethod
    def get_ctrl_type() -> bool:
        if WebServiceConnection.__ctrl_type is None:
            raise Exception("No Control Type!")
        else:
            return WebServiceConnection.__ctrl_type

    @staticmethod
    def get_system_name():
        if WebServiceConnection.__sysid is None:
            raise Exception("No System Name!")
        else:
            return WebServiceConnection.__system_name

    @staticmethod
    def get_system_guid():
        if WebServiceConnection.__sysid is None:
            raise Exception("No System Guid!")
        else:
            return WebServiceConnection.__sysid

    @staticmethod
    def get_rw_version():
        if WebServiceConnection.__rw_version is None:
            raise Exception("No Robot Ware Version!")
        else:
            return WebServiceConnection.__rw_version

    def __init__(self, host, port, username, password):
        WebServiceConnection.__session = requests.Session()
        WebServiceConnection.__host = host
        WebServiceConnection.__port = port
        WebServiceConnection.__username = username
        WebServiceConnection.__password = password
        digest_auth = HTTPDigestAuth(username, password)
        # For json format data
        url = "http://{0}:{1}/rw/system?json=1".format(host, port)
        resp = WebServiceConnection.__session.get(url, auth=digest_auth)
        WebServiceConnection.__cookies = resp.cookies
        obj = json.loads(resp.text)
        WebServiceConnection.__system_name = obj["_embedded"]["_state"][0]["name"]
        WebServiceConnection.__rw_version = obj["_embedded"]["_state"][0]["rwversion"]
        WebServiceConnection.__sysid = obj["_embedded"]["_state"][0]["sysid"]
        # For xml format data
        url = "http://{0}:{1}/ctrl".format(host, port)
        resp = WebServiceConnection.__session.get(url, auth=digest_auth)
        WebServiceConnection.__cookies = resp.cookies
        root = ET.fromstring(resp.text)
        if root.findall(".//{0}li[@class='ctrl-identity-info-li']".format(WebServiceConnection.__namespace)):
            WebServiceConnection.__ctrl_name = root.find(
                ".//{0}li[@class='ctrl-identity-info-li']/{0}span[@class='ctrl-name']"
                .format(WebServiceConnection.__namespace)).text
            controller_type = root.find(
                ".//{0}li[@class='ctrl-identity-info-li']/{0}span[@class='ctrl-type']"
                    .format(WebServiceConnection.__namespace)).text
            if controller_type == "Virtual Controller":
                WebServiceConnection.__ctrl_type = True
            else:
                WebServiceConnection.__ctrl_type = False

