# Web socket client using https://ws4py.readthedocs.org/en/latest/
import sys, argparse
import xml.etree.ElementTree as ET
from ws4py.client.threadedclient import WebSocketClient
import requests
from requests.auth import HTTPDigestAuth

namespace = '{http://www.w3.org/1999/xhtml}'


def print_event(evt):
    root = ET.fromstring(evt)
    if root.findall(".//{0}li[@class='pnl-ctrlstate-ev']".format(namespace)):
        print("\tController State : " + root.find(".//{0}li[@class='pnl-ctrlstate-ev']/{0}span".format(namespace)).text)
    if root.findall(".//{0}li[@class='pnl-opmode-ev']".format(namespace)):
        print("\tOperation Mode : " + root.find(".//{0}li[@class='pnl-opmode-ev']/{0}span".format(namespace)).text)
    if root.findall(".//{0}li[@class='pnl-speedratio-ev']".format(namespace)):
        print("\tSpeed Ratio : " + root.find(".//{0}li[@class='pnl-speedratio-ev']/{0}span".format(namespace)).text)


# This class encapsulates the Web Socket Callbacks functions.
class RobWebSocketClient(WebSocketClient):
    def opened(self):
        print("Web Sockect connection established")

    def closed(self, code, reason=None):
        print("Closed down", code, reason)

    def received_message(self, event_xml):
        if event_xml.is_text:
            print("Events : ")
            print_event(event_xml.data.decode("utf-8"))
        else:
            print("Received Illegal Event " + str(event_xml))


# The main RobotWare Panel class
class RWPanel:

    def __init__(self, host, username, password):
        self.host = host
        self.username = username
        self.password = password
        self.digest_auth = HTTPDigestAuth(self.username, self.password)
        self.subscription_url = 'http://{0}/subscription'.format(self.host)

    def subscribe(self):
        # Create a payload to subscribe on RobotWare Panel Resources with high priority
        payload = {'resources': ['1', '2', '3'],
                   '1': '/rw/panel/speedratio',
                   '1-p': '1',
                   '2': '/rw/panel/ctrlstate',
                   '2-p': '1',
                   '3': '/rw/panel/opmode',
                   '3-p': '1'}

        resp = requests.post(self.subscription_url, auth=self.digest_auth, data=payload)
        print("Initial Events : ")
        print_event(resp.text)
        if resp.status_code == 201:
            self.location = resp.headers['Location']
            self.cookie = 'ABBCX={0}'.format(resp.cookies['ABBCX'])
            return True
        else:
            print('Error subscribing ' + str(resp.status_code))
            return False

    def start_recv_events(self):
        # It is not enough to just send the Cookie. The Authorization header should be included for Web Socket Upgrade
        # request otherwise we get an Unauthorized error.
        header = [('Cookie', self.cookie),
                  ('Authorization', self.digest_auth.build_digest_header("GET", self.subscription_url))]
        self.ws = RobWebSocketClient(self.location,
                                     protocols=['robapi2_subscription'],
                                     headers=header)
        self.ws.connect()
        self.ws.run_forever()

    def close(self):
        self.ws.close()


def enable_http_debug():
    import logging
    import http.client
    http.client.HTTPConnection.debuglevel = 1
    logging.basicConfig()  # Initialize logging
    logging.getLogger().setLevel(logging.DEBUG)
    requests_log = logging.getLogger("requests.packages.urllib3")
    requests_log.setLevel(logging.DEBUG)
    requests_log.propagate = True


def main(argv):
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("-host", help="The host to connect. Defaults to localhost on port 80",
                            default='localhost:8680')
        parser.add_argument("-user", help="The login user name. Defaults to default user name", default='Default User')
        parser.add_argument("-passcode", help="The login password. Defaults to default password", default='robotics')
        parser.add_argument("-debug", help="Enable HTTP level debugging.", action='store_true')
        args = parser.parse_args()

        if args.debug:
            enable_http_debug()

        rwpanel = RWPanel(args.host, args.user, args.passcode)
        if rwpanel.subscribe():
            rwpanel.start_recv_events()
    except KeyboardInterrupt:
        rwpanel.close()


if __name__ == "__main__":
    main(sys.argv[1:])







