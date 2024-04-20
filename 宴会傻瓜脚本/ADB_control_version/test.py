import os
import subprocess
import time
import resources_1080_1920
from functions import *
from local_data import local_device


def need_test():
    obtain_screenshot()

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

start = time.time()
click_qian_zhuang_from_home(20, 0.1)
end = time.time()
print(end-start)
