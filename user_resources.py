from requests.auth import HTTPDigestAuth
import requests
import xml.etree.ElementTree as ET
from web_service_connection import WebServiceConnection


class UserResources:
    def __init__(self, host, session, cookies):
        self.host = host
        self.session = session
        self.cookies = cookies

    def get_user_resources(self):
        str_url = "http://{0}/users".format(self.host)
        resp = self.session.get(str_url, cookies=self.cookies)
        print(resp.text)

    def get_user_actions(self):
        str_url = "http://{0}/users?action=show".format(self.host)
        resp = self.session.get(str_url, cookies=self.cookies)
        print(resp.text)

    # Supported in boot server mode
    def register_user(self):
        str_url = "http://{0}/users".format(self.host)
        payload = {"username": "xyz",
                   "application": "RobotStudio",
                   "location": "IN - BLR - 0000",
                   "ulocale": "remote"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)

    # Supported in boot server mode
    def impersonate_user(self):
        str_url = "http://{0}/users?action=impersonate".format(self.host)
        payload = {"uid": "9"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)

    def login_as_local_user(self):
        str_url = "http://{0}/users?action=set-locale".format(self.host)
        payload = {"type": "local"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)

    def get_user_grants(self):
        str_url = "http://{0}/users/grants".format(self.host)
        resp = self.session.get(str_url, cookies=self.cookies)
        print(resp.text)

    # RMMP stands for Request Manual Mode Privileges.
    def get_rmmp_state(self):
        str_url = "http://{0}/users/rmmp".format(self.host)
        resp = self.session.get(str_url, cookies=self.cookies)
        print(resp.text)

    def get_rmmp_actions(self):
        str_url = "http://{0}/users/rmmp?action=show".format(self.host)
        resp = self.session.get(str_url, cookies=self.cookies)
        print(resp.text)

    def request_actions(self):
        str_url = "http://{0}/users/rmmp".format(self.host)
        payload = {"privilege": "modify"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)

    def grant_rmmp_request(self):
        str_url = "http://{0}/users/rmmp?action=set".format(self.host)
        payload = {"uid": "11"
                   , "privilege": "modify"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)

    def deny_rmmp_request(self):
        str_url = "http://{0}/users/rmmp?action=set".format(self.host)
        payload = {"uid": "11"
                   , "privilege": "deny"}
        resp = self.session.post(str_url, cookies=self.cookies, data=payload)
        print(resp.status_code)


host = "127.0.0.1:8680"
username = "Default User"
password = "robotics"

web_service_connection = WebServiceConnection(host, username, password)

user_resources = UserResources(WebServiceConnection.get_host()
                               , WebServiceConnection.get_session()
                               , WebServiceConnection.get_cookies())
user_resources.get_user_resources()
