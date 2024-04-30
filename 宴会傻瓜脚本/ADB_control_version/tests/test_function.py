# testing functions
import subprocess
import time
from ADB_project.functions.functions import *
from ADB_project.functions.local_data import local_device, json_file_path
from ADB_project.functions.obtain_port_number import *
from ADB_project.functions.connect_check import *
from ADB_project.functions.json_function import * 

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
    # start_apk_game
]
st = 0.5
for fun in funs:
    test_function(fun, device = local_device, sleep_time=st)

# start_apk_game(device= local_device)

def need_test():
    # 测试特殊弹窗
    start_game()
    tu_di_raise_up()
    zhi_you_tan_xin()

