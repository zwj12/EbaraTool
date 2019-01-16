import sys
import argparse
import xml.etree.ElementTree as ET
import json
from ws4py.client.threadedclient import WebSocketClient
import requests
from requests.auth import HTTPDigestAuth
from web_service_connection import WebServiceConnection


class PipeGrooveModel:
    def __init__(self):
        self.num_index = 0
        self.num_pipe_groove_type = 0

        self.num_weld_leg_width = 0
        self.num_groove_gap = 0
        self.num_branch_groove_root = 0
        self.num_branch_groove_angle = 0

        self.num_seam_centerX = 0
        self.num_seam_normal_angle = 0

        self.num_header_diameter = 0
        self.num_header_thickness = 0
        self.num_header_material = 0

        self.num_branch_diameter = 0
        self.num_branch_thickness = 0
        self.num_branch_material = 0

        self.num_multi_pass_total = 0
        self.num_cooperative_robots = 0
        self.num_path_source = 0

        self.num_revise_scan_branch_type = 0
        self.num_revise_scan_header_type = 0

        self.bool_continuous = False
        self.bool_use_aligned_STN_by_fixed_value = False

        self.str_ID = ""
        self.str_remark = ""

    # parse format: [1,3,9,3,0,45,955,234.7,318.5,25.4,1,318.5,25.4,1,1,5,3,3,3,TRUE,TRUE,"","product_c"]
    def parse(self, str_pipe_groove_model):
        num_start_index = str_pipe_groove_model.index("[") + 1
        num_stop_index = str_pipe_groove_model.index(",")
        self.num_index = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_pipe_groove_type = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_weld_leg_width = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_groove_gap = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_branch_groove_root = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_branch_groove_angle = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_seam_centerX = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_seam_normal_angle = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_header_diameter = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_header_thickness = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_header_material = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_branch_diameter = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_branch_thickness = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_branch_material = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_multi_pass_total = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_cooperative_robots = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_path_source = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_revise_scan_branch_type = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.num_revise_scan_header_type = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.bool_continuous = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_stop_index = str_pipe_groove_model.index(",", num_start_index)
        self.bool_use_aligned_STN_by_fixed_value = str_pipe_groove_model[num_start_index:num_stop_index]

        num_start_index = num_stop_index + 1
        num_start_index = str_pipe_groove_model.index("\"", num_start_index) + 1
        num_stop_index = num_start_index
        # console.log("num_start_index=" + num_start_index)
        while num_stop_index < len(str_pipe_groove_model):
            num_stop_index = str_pipe_groove_model.index("\"", num_stop_index)
            if str_pipe_groove_model[num_stop_index + 1] != "\"":
                break
            else:
                num_stop_index = num_stop_index + 2
        self.str_ID = str_pipe_groove_model[num_start_index:num_stop_index]
        num_stop_index = str_pipe_groove_model.index(",", num_stop_index + 1)

        num_start_index = num_stop_index + 1
        num_start_index = str_pipe_groove_model.index("\"", num_start_index) + 1
        num_stop_index = num_start_index
        # console.log("num_start_index=" + num_start_index)
        while num_stop_index < len(str_pipe_groove_model):
            num_stop_index = str_pipe_groove_model.index("\"", num_stop_index)
            if str_pipe_groove_model[num_stop_index + 1] != "\"":
                break
            else:
                num_stop_index = num_stop_index + 2
        self.str_remark = str_pipe_groove_model[num_start_index:num_stop_index]
        # num_stop_index = str_pipe_groove_model.index(",", num_stop_index + 1)

        self.num_index = float(self.num_index)
        self.num_pipe_groove_type = int(self.num_pipe_groove_type)
        self.num_weld_leg_width = float(self.num_weld_leg_width)
        self.num_groove_gap = float(self.num_groove_gap)
        self.num_branch_groove_root = float(self.num_branch_groove_root)
        self.num_branch_groove_angle = float(self.num_branch_groove_angle)
        self.num_seam_centerX = float(self.num_seam_centerX)
        self.num_seam_normal_angle = float(self.num_seam_normal_angle)
        self.num_header_diameter = float(self.num_header_diameter)
        self.num_header_thickness = float(self.num_header_thickness)
        self.num_header_material = float(self.num_header_material)
        self.num_branch_diameter = float(self.num_branch_diameter)
        self.num_branch_thickness = float(self.num_branch_thickness)
        self.num_branch_material = float(self.num_branch_material)
        self.num_multi_pass_total = float(self.num_multi_pass_total)
        self.num_cooperative_robots = float(self.num_cooperative_robots)
        self.num_path_source = float(self.num_path_source)
        self.num_revise_scan_branch_type = float(self.num_revise_scan_branch_type)
        self.num_revise_scan_header_type = float(self.num_revise_scan_header_type)
        self.bool_continuous = bool(self.bool_continuous)
        self.bool_use_aligned_STN_by_fixed_value = bool(self.bool_use_aligned_STN_by_fixed_value)

    def to_string(self):
        return "[{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11},{12},{13}" \
               ",{14},{15},{16},{17},{18},{19},{20},\"{21}\",\"{22}\"]".format(
                self.num_index, self.num_pipe_groove_type
                , self.num_weld_leg_width, self.num_groove_gap, self.num_branch_groove_root, self.num_branch_groove_angle
                , self.num_seam_centerX, self.num_seam_normal_angle
                , self.num_header_diameter, self.num_header_thickness, self.num_header_material
                , self.num_branch_diameter, self.num_branch_thickness, self.num_branch_material
                , self.num_multi_pass_total, self.num_cooperative_robots, self.num_path_source
                , self.num_revise_scan_branch_type, self.num_revise_scan_header_type
                , self.bool_continuous, self.bool_use_aligned_STN_by_fixed_value
                , self.str_ID, self.str_remark)

    def get_data_from_web_service(self):
        url = "http://{0}:{1}/rw/rapid/symbol/data/RAPID/T_ROB1/GlobalDataModule/rPipeGrooveModel?json=1"\
            .format(WebServiceConnection.get_host(), WebServiceConnection.get_port())
        resp = WebServiceConnection.get_session().get(url, cookies=WebServiceConnection.get_cookies())
        obj = json.loads(resp.text)
        pipe_groove_model_item = obj["_embedded"]["_state"][0]
        self.parse(pipe_groove_model_item["value"])

    def set_data_to_web_service(self):
        url = "http://{0}:{1}/rw/rapid/symbol/data/RAPID/T_ROB1/GlobalDataModule/rPipeGrooveModel?action=set"\
            .format(WebServiceConnection.get_host(), WebServiceConnection.get_port())
        payload = {"value": self.to_string()}
        WebServiceConnection.get_session().post(url, cookies=WebServiceConnection.get_cookies(), data=payload)
