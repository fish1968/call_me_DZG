import set_project_dir
import time
from ADB_project.functions.local_data import local_device, debugging, json_file_path
# from ADB_project.functions.local_data import local_device, debugging, json_file_path
from ADB_project.functions.json_function import update_local_json_data_to_date
from ADB_project.functions.adb_operations import adb_is_game_the_current_activity
from ADB_project.functions.daily_functions import daily_do_once, click_wait, init
from ADB_project.functions.cheng_jiao_functions import xiang_mu_zhao_shang, shang_zhan, daily_cheng_jiao_you_li
from ADB_project.functions.events_functions import da_long, shou_lie, quick_fox
from ADB_project.functions.home_functions import zhi_you_tan_xin
if __name__ == "__main__":
    init_begin = time.time()
    # if current_acitivity is not dzg
    #   start quick_fox
    if not (adb_is_game_the_current_activity()):
        quick_fox()
    device = init()
    init_end = time.time()
    if debugging:
        print(f"\nEmulator is on and connected by {device}, init time = {init_end - init_begin}\n")

    begin_t = time.time()
    # obtain whether do xing_shan based on current date
    end_t = time.time()
    if debugging:
        print(f"Daily_do_once finished in {end_t - begin_t}")
    # Below should be in file
    has_da_long = False
    has_seats = False
    has_shang_zhan = 3
    has_tan_xin = False
    has_you_li = False
    did_shang_zhan_this_hour = True
    while True:
        t_hour = time.localtime(time.time()).tm_hour
        print(f" t_hour = {t_hour}")
        if t_hour == 20 and (has_da_long == False):
            da_long(device = device, sleep_time=2)
            has_da_long = True
        if (t_hour in [12, 13]): # need improvement
            shou_lie(device = device, sleep_time=2)
        if (t_hour in [2, 5, 8, 11, 14, 18, 22, 23]):
            if has_seats == False:
                xiang_mu_zhao_shang(device = device, sleep_time= 2)
                has_seats = True
        else:
            has_seats = False
        if t_hour in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (did_shang_zhan_this_hour == False):
                shang_zhan(device = device, sleep_time=2)
                did_shang_zhan_this_hour = True
        else:
            did_shang_zhan_this_hour = False
        
        if t_hour in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (has_tan_xin == False):
                zhi_you_tan_xin(device = device, sleep_time=2)
                has_tan_xin = True
        else:
            has_tan_xin = False
        if t_hour in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (has_you_li== False):
                daily_cheng_jiao_you_li(device = device, sleep_time=2)
                has_you_li = True
        else:
            has_you_li = False
            
        click_wait(total_time = 100, sleep_time = 10, device = local_device)
