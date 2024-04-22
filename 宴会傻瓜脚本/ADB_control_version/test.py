import os
import subprocess
import time
from functions import *
from local_data import local_device


def need_test():
    obtain_screenshot()
    tu_di_raise_up(device=local_device) # 弹窗 导致卡死

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
    
    ri_chang_ren_wu_qian_zhuang_20()
    daily_xing_yun_duo_bao_2()

def daily_once(device = local_device):
    click_union_basic_constrcut(device=device)
    daily_click_home_shang_cheng_ling_qu(device=device, sleep_time=1)
    daily_cai_shen_miao_like(device=device, sleep_time=1)
    daily_click_rank(device=device, sleep_time=1)
    ri_chang_chuang_dang(device=device, sleep_time=1)
    daily_click_qian_zhuang_wei_ren(device=device, sleep_time=1)
    daily_xing_yun_duo_bao_2(device=device)
    daily_cheng_jiao_you_li(device=device)
    daily_ling_qu_yu_gan(device = device, sleep_time = 1)
    ri_chang_ren_wu_qian_zhuang_20(device=device)
    shang_zhan(device=device)
    daily_xing_shan(device=device)
    for _ in range(3):
        time.sleep(60*10)
        click_painless(device=device, times = 10)
        click_union_basic_constrcut(device=device)
    time.sleep(3600 - 3  * 60 * 10)
    click_painless(device=device, times=10)
    shang_zhan(device=device)
    time.sleep(3600)
    click_painless(device=device, times=10)
    shang_zhan(device=device)

start = time.time()
# daily_cheng_jiao_you_li()
# daily_once(device=local_device)
# click_qian_zhuang_from_home(30)
# daily_click_rank()
# tu_di_raise_up(device=local_device)
# daily_ling_qu_yu_gan(device = local_device, sleep_time = 1)
# shou_lie(device=local_device, sleep_time=1)
# ri_chang_chuang_dang()
# daily_xing_shan()
# shang_zhan()
# move_to_end(bottom=1)
# daily_cai_shen_miao_like()
time.sleep(3)
end = time.time()
print(end-start)

while True:
    click_painless(device=local_device, sleep_time=100,times=1000)
