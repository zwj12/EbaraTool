import sys
import argparse
import xml.etree.ElementTree as ET
import json
from ws4py.client.threadedclient import WebSocketClient
import requests
from requests.auth import HTTPDigestAuth

namespace = '{http://www.w3.org/1999/xhtml}'


class WeldTarget:
    def __init__(self):
        self.num_rob = 0
        self.num_layer = 0
        self.num_index = 0

        self.num_angle = 0
        self.num_process_type = 0

        self.num_tcs_offset_x = 0
        self.num_tcs_offset_y = 0
        self.num_tcs_offset_z = 0
        self.num_tcs_rotation_x = 0
        self.num_tcs_rotation_y = 0
        self.num_tcs_rotation_z = 0
        self.str_weld_procedure_id = ""
        self.str_remark = ""

        self.num_w_obj_x = 0
        self.num_w_obj_y = 0
        self.num_w_obj_z = 0
        self.num_w_obj_ez = 0
        self.num_w_obj_ey = 0
        self.num_w_obj_ex = 0

    # parse format: [0,1,0,0,0,0,0,0,"","",133.7,0,133.7,0,-135,0]
    def parse(self, str_weld_target):
        num_start_index = str_weld_target.index("[") + 1
        num_stop_index = str_weld_target.index(",")
        self.num_angle = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_process_type = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_offset_x = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_offset_y = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_offset_z = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_rotation_x = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_rotation_y = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_tcs_rotation_z = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_start_index = str_weld_target.index("\"", num_start_index) + 1
        num_stop_index = num_start_index
        # console.log("num_start_index=" + num_start_index)
        while num_stop_index < len(str_weld_target):
            num_stop_index = str_weld_target.index("\"", num_stop_index)
            if str_weld_target[num_stop_index + 1] != "\"":
                break
            else:
                num_stop_index = num_stop_index + 2
        self.str_weld_procedure_id = str_weld_target[num_start_index:num_stop_index]
        num_stop_index = str_weld_target.index(",", num_stop_index + 1)

        num_start_index = num_stop_index + 1
        num_start_index = str_weld_target.index("\"", num_start_index) + 1
        num_stop_index = num_start_index
        # console.log("num_start_index=" + num_start_index)
        while num_stop_index < len(str_weld_target):
            num_stop_index = str_weld_target.index("\"", num_stop_index)
            if str_weld_target[num_stop_index + 1] != "\"":
                break
            else:
                num_stop_index = num_stop_index + 2
        self.str_remark = str_weld_target[num_start_index:num_stop_index]
        num_stop_index = str_weld_target.index(",", num_stop_index + 1)

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_w_obj_x = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_w_obj_y = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_w_obj_z = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_w_obj_ez = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index(",", num_start_index)
        self.num_w_obj_ey = str_weld_target[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_weld_target.index("]", num_start_index)
        self.num_w_obj_ex = str_weld_target[num_start_index:num_stop_index]

        self.num_angle = float(self.num_angle)
        self.num_process_type = int(self.num_process_type)
        self.num_tcs_offset_x = float(self.num_tcs_offset_x)
        self.num_tcs_offset_y = float(self.num_tcs_offset_y)
        self.num_tcs_offset_z = float(self.num_tcs_offset_z)
        self.num_tcs_rotation_x = float(self.num_tcs_rotation_x)
        self.num_tcs_rotation_y = float(self.num_tcs_rotation_y)
        self.num_tcs_rotation_z = float(self.num_tcs_rotation_z)
        self.num_w_obj_x = float(self.num_w_obj_x)
        self.num_w_obj_y = float(self.num_w_obj_y)
        self.num_w_obj_z = float(self.num_w_obj_z)
        self.num_w_obj_ez = float(self.num_w_obj_ez)
        self.num_w_obj_ey = float(self.num_w_obj_ey)
        self.num_w_obj_ex = float(self.num_w_obj_ex)

    def to_string(self):
        return "[{0:.0f},{1},{2},{3},{4},{5},{6},{7},\"{8}\",\"{9}\",{10},{11},{12},{13},{14},{15}]".format(
            self.num_angle, self.num_process_type
            , self.num_tcs_offset_x, self.num_tcs_offset_y, self.num_tcs_offset_z
            , self.num_tcs_rotation_x, self.num_tcs_rotation_y, self.num_tcs_rotation_z
            , self.str_weld_procedure_id, self.str_remark
            , self.num_w_obj_x, self.num_w_obj_y, self.num_w_obj_z
            , self.num_w_obj_ez, self.num_w_obj_ey, self.num_w_obj_ex
        )

    def get_data_from_web_service(self, num_rob, num_layer, num_index, host, username, password):
        self.num_rob = num_rob
        self.num_layer = num_layer
        self.num_index = num_index
        digest_auth = HTTPDigestAuth(username, password)
        str_prefix = "http://{0}/rw/rapid/symbol/data/RAPID/T_ROB1/GlobalDataModule".format(host)
        str_request = "{0}/rRob{1}Layer{2}{{{3}}}?json=1".format(str_prefix, num_rob, num_layer, num_index)
        resp = requests.get(str_request, auth=digest_auth)
        obj = json.loads(resp.text)
        weld_target_item = obj["_embedded"]["_state"][0]
        self.parse(weld_target_item["value"])

    def set_data_to_web_service(self, host, username, password):
        digest_auth = HTTPDigestAuth(username, password)
        str_prefix = "http://{0}/rw/rapid/symbol/data/RAPID/T_ROB1/GlobalDataModule".format(host)
        str_post_url = "{0}/rRob{1}Layer{2}{{{3}}}?action=set".format(str_prefix, self.num_rob, self.num_layer,
                                                                      self.num_index)
        payload = {"value": self.to_string()}
        requests.post(str_post_url, auth=digest_auth, data=payload)


weld_target = WeldTarget()
"""
input_weld_target = "[0,1,0,0,0,0,0,0,\"\",\"\",133.7,0,133.7,0,-135,0]"
print(input_weld_target)
weld_target.parse(input_weld_target)
print(weld_target.to_string())
"""

parser = argparse.ArgumentParser()
parser.add_argument("-host", help="The host to connect. Defaults to localhost on port 80",
                    default='127.0.0.1:8661')
parser.add_argument("-user", help="The login user name. Defaults to default user name",
                    default='Default User')
parser.add_argument("-passcode", help="The login password. Defaults to default password",
                    default='robotics')
parser.add_argument("-debug", help="Enable HTTP level debugging.", action='store_true')
args = parser.parse_args()
weld_target.get_data_from_web_service(1, 1, 1, args.host, args.user, args.passcode)
print(weld_target.to_string())

weld_target.num_angle = 15
weld_target.set_data_to_web_service(args.host, args.user, args.passcode)

weld_target.get_data_from_web_service(1, 1, 1, args.host, args.user, args.passcode)
print(weld_target.to_string())
