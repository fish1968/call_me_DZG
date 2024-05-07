import set_project_dir
import time
from ADB_project.functions.local_data import local_device, debugging, json_file_path
# from ADB_project.functions.local_data import local_device, debugging, json_file_path
from ADB_project.functions.json_function import update_local_json_data_to_date, read_json, update_json
from ADB_project.functions.adb_operations import adb_is_game_the_current_activity
from ADB_project.functions.daily_functions import daily_do_once, click_wait, init
from ADB_project.functions.cheng_jiao_functions import xiang_mu_zhao_shang, shang_zhan, daily_cheng_jiao_you_li, daily_ling_qu_yu_gan, click_union_basic_constrcut, daily_xing_shan
from ADB_project.functions.events_functions import da_long, shou_lie, quick_fox
from ADB_project.functions.home_functions import zhi_you_tan_xin, men_sheng_raise_up
from ADB_project.functions.shang_pu_functions import daily_do_jiu_si, daily_do_yao_pu
from ADB_project.functions.basic_dzg_functions import click_exit
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
    update_local_json_data_to_date(json_file_path)
    # obtain whether do xing_shan based on current date
    has_do_xing_shan = read_json(json_file_path, "do_xing_shan")
    if has_do_xing_shan in [0, None]:
        daily_xing_shan(device = device, sleep_time = 1)
        update_json(json_file_path, entry = "do_xing_shan", value = 1)
    end_t = time.time()
    if debugging:
        print(f"Daily_do_once finished in {end_t - begin_t}")
    # Below should be in file
    has_do_once = read_json(json_file_path, entry = "has_do_once")
    has_da_long = read_json(json_file_path, entry = "has_da_long")
    has_seats = read_json(json_file_path, entry = "has_seats")
    has_tan_xin = read_json(json_file_path, entry = "has_tan_xin")
    has_you_li = read_json(json_file_path, entry = "has_you_li")
    did_shang_zhan_this_hour = read_json(json_file_path, entry = "did_shang_zhan_this_hour")
    did_men_sheng_this_hour = read_json(json_file_path, entry = "did_men_sheng_this_hour")
    did_yu_gan_this_hour = read_json(json_file_path, entry = "did_yu_gan_this_hour")
    did_jiu_si_and_yao_pu_this_hour = read_json(json_file_path, entry = "did_jiu_si_and_yao_pu_this_hour")
    did_union_construct = False # Never update
    while True:
        t_hour = time.localtime(time.time()).tm_hour
        print(f" t_hour = {t_hour}")
        if t_hour == 0 and has_do_once in [False, None, 0]:
            daily_do_once(device = device, sleep_time= 2)
            daily_do_once = True
            update_json(json_file_path, entry = "daily_do_once", value = 1)
            click_exit(device= device, sleep_time=0.3, times = 10)
        if t_hour == 20 and (has_da_long in [False, None, 0]):
            da_long(device = device, sleep_time=2)
            click_exit(device= device, sleep_time=0.3, times = 10)
            has_da_long = True
        if (t_hour in [12, 13]): # need improvement
            shou_lie(device = device, sleep_time=2)
        if (t_hour in [2, 5, 8, 11, 14, 18, 22, 23]):
            if has_seats in [False, None, 0]:
                xiang_mu_zhao_shang(device = device, sleep_time= 2)
                has_seats = True
                click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            has_seats = False
        if t_hour in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (did_shang_zhan_this_hour in [False, None, 0]):
                shang_zhan(device = device, sleep_time=2)
                did_shang_zhan_this_hour = True
                click_exit(device= device, sleep_time=0.3, times = 10)
            click_union_basic_constrcut(device = device, sleep_time= 3)
            click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            did_shang_zhan_this_hour = False
        
        if t_hour in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (has_tan_xin == False):
                zhi_you_tan_xin(device = device, sleep_time=2)
                has_tan_xin = True
                click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            has_tan_xin = False
        if t_hour in [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23]:
            if (has_you_li== False):
                daily_cheng_jiao_you_li(device = device, sleep_time=2)
                has_you_li = True
                click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            has_you_li = False
        if t_hour in [1, 5, 7, 11, 14, 18, 21]:
            if (did_men_sheng_this_hour == False):
                men_sheng_raise_up(device = device, sleep_time = 2)
                did_men_sheng_this_hour = True
                click_exit(device= device, sleep_time=0.3, times = 10)
            else:
                did_men_sheng_this_hour = False
        if t_hour in [10, 15, 21]:
            if (did_yu_gan_this_hour == False):
                daily_ling_qu_yu_gan(device = device, sleep_time = 2)
                did_yu_gan_this_hour = True
                click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            did_yu_gan_this_hour = False
        if t_hour in [11, 16, 22]:
            if (did_jiu_si_and_yao_pu_this_hour == False):
                daily_do_jiu_si(device = device, sleep_time = 2)
                daily_do_yao_pu(device = device, sleep_time = 2)
                did_jiu_si_and_yao_pu_this_hour = True
                click_exit(device= device, sleep_time=0.3, times = 10)
        else:
            did_jiu_si_and_yao_pu_this_hour = False
        click_exit(device= device, sleep_time=0.3, times = 10)
        click_wait(total_time = 100, sleep_time = 10, device = local_device)
