import sys
import argparse
import xml.etree.ElementTree as ET
import json
from ws4py.client.threadedclient import WebSocketClient
import requests
from requests.auth import HTTPDigestAuth
import time

digest_auth = HTTPDigestAuth("Default User", "robotics")
import sys
import argparse
import xml.etree.ElementTree as ET
import json
from ws4py.client.threadedclient import WebSocketClient
import requests
from requests.auth import HTTPDigestAuth
import time

s = requests.Session()
digest_auth = HTTPDigestAuth("Default User", "robotics")
str_url = "http://{0}/users".format("localhost:8680")
payload = {"privilege": "modify"}
resp = s.get(str_url, auth=digest_auth)
print(resp.text)
print(resp.cookies)
cookies = resp.cookies
str_url = "http://{0}/users?action=show".format("localhost:8680")
resp = s.get(str_url, cookies=cookies)
print(resp.text)
resp = s.get(str_url, cookies=cookies)
print(resp.text)
# time.sleep(10)

str_url = "http://{0}/users/rmmp".format("localhost:8680")
payload = {"privilege": "modify"}
s.post(str_url, cookies=cookies, data=payload)

str_url = "http://{0}/rw/mastership?action=request".format("localhost:8680")
s.post(str_url, cookies=cookies)


