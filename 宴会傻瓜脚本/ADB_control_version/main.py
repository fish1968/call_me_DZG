import os
import subprocess
import time
from functions import *
from local_data import local_device, json_file_path
from obtain_port_number import *
from connect_check import *
from json_function import * 

def daily_do_once(device = local_device, do_xing_shan = False,
                sleep_time = 1, json_file_path = json_file_path):
    # 启动
    print("daily_do_once 启动 begins")
    # start_apk_game() # 容易卡住

    #挨个进入主页面
    activate_cache(device = device, sleep_time = sleep_time)

    # home
    print("- "*10)
    daily_in_home       (device=device, sleep_time=sleep_time )

    # 城郊
    print("- "*10)
    daily_in_cheng_jiao (device=device, sleep_time=sleep_time , do_xing_shan = do_xing_shan)
    update_xing_shan(json_file_path, to_do=False)

    # 商铺
    print("- "*10)
    daily_in_shang_pu   (device=device, sleep_time=sleep_time )

    # 日常闯荡一次
    print("- "*10)
    ri_chang_chuang_dang(device=device, sleep_time=sleep_time )
    
    # wait 10 minutes
    print("- "*10)
    for _ in range(3):
        click_wait(total_time=60*10, sleep_time=50, device=device)
        click_union_basic_constrcut(device=device)
    for _ in range(4):
        click_wait(total_time=1800, sleep_time=50, device=device)
        shang_zhan(device=device)
    print("daily_do_once ends")
    print("- " * 20)

if __name__ == "__main__":
    # check connectivity
    while is_adb_server_on() == False:
        subprocess.run(["adb", "start-server"])

    if not is_device_connected(device=local_device):
        local_device = "localhost:"+str(find_available_port(5555, 5560))
        is_device_connected(device=local_device)

    start = time.time()

    # check whether do xing_shan
    do_xing_shan = check_need_and_update_time(file_path=json_file_path)
    daily_do_once(device=local_device, do_xing_shan=do_xing_shan)

    end = time.time()
    print(end-start)

    while True:
        click_wait(total_time = 100, sleep_time = 10, device = local_device)
