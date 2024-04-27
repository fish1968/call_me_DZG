import os
import subprocess
import time
from functions import *
from local_data import local_device, do_xing_shan, json_file_path
from obtain_port_number import *
from connect_check import *
from json_function import * 

def need_test():
    obtain_screenshot()
    tu_di_raise_up(device=local_device) # 弹窗——导致卡死， 需要修改，现在有一键培养
    start_apk_game() # 容易点到特权

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

def test_yu_gan():
    # 鱼竿测试，发现有偏移现象
    st = 1.3
    for _ in range(10):
        print(f"st = {st}")
        daily_ling_qu_yu_gan(sleep_time = st)
        st -= 0.1

def daily_do_once(device = local_device, do_xing_shan = do_xing_shan,
                sleep_time = 1, json_file_path = json_file_path):
    # 启动
    print("daily_do_once 启动")
    # start_apk_game() # 容易卡住
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
    
    print("- "*10)
    # wait 10 minutes
    for _ in range(3):
        click_wait(total_time=60*10, sleep_time=50, deivce=device)
        click_union_basic_constrcut(device=device)
    for _ in range(4):
        click_wait(total_time=1800, sleep_time=50, deivce=device)
        shang_zhan(device=device)
    print("daily_do_once ends")
    print("- " * 20)


start = time.time()
# check connectivity
while is_adb_connected() == False:
    subprocess.run(["adb", "start-server"])

if not is_device_connected(device=local_device):
    local_device = "localhost:"+str(find_available_port(5555, 5560))
    is_device_connected(device=local_device)

# check whether do xing_shan
do_xing_shan = check_need_and_update_time(file_path=json_file_path)

daily_do_once(device=local_device, do_xing_shan=do_xing_shan)

if False:
    # daily_do_shang_pu_qian_dao()
    # click_union_basic_constrcut()
    # daily_mail_process()
    # daily_cai_shen_miao_like(sleep_time=0.6)
    # daily_cheng_jiao_you_li()
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
    # daily_qiao_qian()
    # time.sleep(3)
    # daily_profile_yuan_bao()
    # start_apk_game()
    # daily_do_yi_guan()
    # daily_do_jiu_si()
    # daily_do_yao_pu()
    pass
end = time.time()

print(end-start)

while True:
    click_painless(device=local_device, sleep_time=10,times=1000)
