# testing functions

import os
import subprocess
import time
from functions import *
from local_data import local_device, json_file_path
from obtain_port_number import *
from connect_check import *
from json_function import * 

def test_function(function_head, device = local_device, sleep_time = 1):
    start = time.time()
    # check connectivity
    while is_adb_server_on() == False:
        subprocess.run(["adb", "start-server"])

    if not is_device_connected(device=device):
        device  = "localhost:"+str(find_available_port(5555, 5560))
        is_device_connected(device=device)
    function_head(device = device, sleep_time=sleep_time)
    end = time.time()
    print(end-start)

# test_function(function_head=daily_cai_shen_miao_like, device=local_device, sleep_time=0.3)
funs = [
    # daily_cai_shen_miao_like
    # click_union_basic_constrcut
    # obtain_screenshot
    # test_move_screenshot
    
]
st = 0.5
for fun in funs:
    test_function(fun, device = local_device, sleep_time=st)

# start_apk_game(device= local_device)

def need_test():
    obtain_screenshot()
    tu_di_raise_up(device=local_device) # 弹窗——导致卡死， 需要修改，现在有一键培养
    start_apk_game()

def passed_test():
    click_qian_zhuang_from_home(100)
    click_union_basic_constrcut()
    test_move_screenshot()
    remove_local_file()
    daily_click_home_shang_cheng_ling_qu(device=local_device, sleep_time=1)
    daily_click_xian_shi_chong_zhi(device=local_device, sleep_time=1)
    daily_click_qian_dao(device=local_device, sleep_time=1)
    daily_click_qian_zhuang_wei_ren(device=local_device, sleep_time=1)
    daily_click_rank(local_device, 1)
    daily_qian_zhuang_20()
    daily_xing_yun_duo_bao_2()
