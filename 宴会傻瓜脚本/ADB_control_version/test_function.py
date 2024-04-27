# testing functions

import os
import subprocess
import time
from functions import *
from local_data import local_device, do_xing_shan, json_file_path
from obtain_port_number import *
from connect_check import *
from json_function import * 

def test_function(function_head, device = local_device, sleep_time = 1):
    function_head(device = device, sleep_time=sleep_time)

test_function(function_head=daily_cai_shen_miao_like, device=local_device, sleep_time=0.3)
# y = 1680
# for x in range(500, 800, 10):
#     print(f"click at {x} {y}")
#     click_once(x, y, device = local_device, sleep_time=0.5)

