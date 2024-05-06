import ADB_project.functions.set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
from ADB_project.functions.local_data import local_device, debugging 
from ADB_project.functions.adb_operations import start_adb, is_device_connected, find_available_port, adb_start_activity, click_once, drag_and_move, start_apk_package
from ADB_project.functions.basic_dzg_functions import enter_home, enter_bei_bao,enter_cheng_jiao, enter_chuang_dang, enter_men_ke, enter_shang_pu, enter_zhi_you, click_exit, activate_cache, click_painless, click_wait, clicks
import subprocess
########## events ###############
def shou_lie(device = local_device, sleep_time = 1):
    if debugging:
        print("shou_lie begin")
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import shou_lie
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    # move to shou_lie
    move_x, move_y = shou_lie["drag_to_shou_lie"]
    drag_and_move(move_x=move_x, move_y=move_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    entry = shou_lie["entry"]
    enter = shou_lie["enter"]
    auto = shou_lie["auto"]
    
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    # 进入 狩猎 page
    click_once(enter[0], enter[1], device=device, sleep_time=sleep_time)
    click_once(auto[0], auto[1], device=device, sleep_time=sleep_time)
    
    # 点击自动
    period = shou_lie["period"]
    for _ in range(50):
        click_painless(device=device, sleep_time=period)
    
    x_help, y_help = shou_lie["shang_hui_help"]
    x2_help, y2_help = shou_lie["shang_hui_help_page"]
    x0, y0 = shou_lie["help_00"]
    dx, dy = shou_lie["help_delta"]
    x_con, y_con = shou_lie["confirm"]
    do = shou_lie["do"]
    
    for index in range(4, -1, -1): # 0 -> 4
        y_t = index // 3
        x_t = index % 3
        x, y = x_t * dx * x_t + x0, dy * y_t + y0
        click_once(x_help, y_help, device=device, sleep_time=sleep_time)
        click_once(x2_help, y2_help, device=device, sleep_time=sleep_time)
        click_once(x, y, device=device, sleep_time=sleep_time)
        click_once(x_con, y_con, device=device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time = sleep_time)
        click_painless(device=device, sleep_time=period/3, times = 4)
    
    click_exit(device = device, sleep_time = sleep_time, times = 3)
    
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("shou_lie 中午狩猎结束 ends")

def da_long(device = local_device, sleep_time = 1):
    # 晚上八点钟打龙
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import da_long
    if debugging:
        print("da_long begin")
    entry = da_long["entry"]
    enter = da_long["enter"]
    auto = da_long["auto"]
    wait_click = da_long["wait_click"]
    exit_num = da_long["exit_num"]
    
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    
    # move to shou_lie
    move_x, move_y = da_long["drag_to_shou_lie"]
    drag_and_move(move_x=move_x, move_y=move_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    
    # 进入 狩猎 page
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    clicks(enter[0], enter[1], device=device, sleep_time=sleep_time, times = 2)
    click_painless(device=device, sleep_time=sleep_time, times = 4)
    # 点击自动出兵
    click_once(auto[0], auto[1], device=device, sleep_time=sleep_time)
    clicks(enter[0], enter[1], device=device, sleep_time=sleep_time, times = 2)
    
    # wait for some times till it ends
    click_wait(total_time = sleep_time * wait_click, sleep_time = sleep_time/2, device = device)
    
    # back home
    click_exit(device=device, sleep_time=sleep_time, times=exit_num)
    enter_home(device = device, sleep_time=sleep_time)
    
    if debugging:
        print("da_long 打龙结束 ends")

@future_care
def quick_fox(device = local_device, sleep_time = 2):
    print("quick fox hasn't been implemented")
    quick_fox_package = "com.zx.a2_quickfox"
    start_apk_package(device = device, apk_package = quick_fox_package)
    click_painless(device = device, sleep_time=sleep_time, times = 3)
    clicks(540, 1000, times = 3, sleep_time=3)
    #click ad
    clicks(540, 1290, device = device, sleep_time = sleep_time, times = 3)
    #click skip
    click_painless(device = device, sleep_time=sleep_time, times = 5)
    print(f"Need a function to implement start and processing {quick_fox_package}")
