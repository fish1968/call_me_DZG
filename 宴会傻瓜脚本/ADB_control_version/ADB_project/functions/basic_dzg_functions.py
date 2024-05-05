import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
import subprocess, time
import ADB_project
from ADB_project.functions.local_data import local_device, debugging, adb_debugging, game_package_name, json_file_path
from ADB_project.functions.local_data import local_device
from ADB_project.functions.adb_operations import clicks, click_once, move_to_left, drag_and_move, adb_start_activity
from ADB_project.functions.adb_operations import find_available_port, is_device_connected
############ MOSTLY USED DZG Basic Operations ######################
def click_exit(device = local_device, sleep_time = 1, times = 1):
    from ADB_project.resources_1080_1920.general import general_pos
    ex = general_pos["exit"]
    clicks(ex[0], ex[1], device = device, sleep_time=sleep_time, times = times)

def click_painless(device = local_device, sleep_time = None, times = 1):
    for _ in range(times):
        click_once(x=500, y =5, device=device, sleep_time=sleep_time)

def click_wait(total_time = 1000, sleep_time = 10, device = local_device):
    if debugging:
        print(f"click_wait with total time: {total_time}, sleep_time: {sleep_time}")
    while total_time > 0:
        click_painless(device=device, sleep_time=sleep_time, times = 3)
        total_time -= sleep_time
    if debugging:
        print("click_wait ends")

########## ENTER X ################
def enter_home(device = local_device, sleep_time = 1):
    if debugging:
        print("\tenter_home 进入首页界面 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_home"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    if debugging:
        print("\tenter_home 进入首页界面 end")

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    if debugging:
        print("\tenter_cheng_jiao 进入城郊界面 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_cheng-jiao"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    if debugging:
        print("\tenter_cheng_jiao 进入城郊界面 end")

def enter_men_ke(device = local_device, sleep_time = 1):
    if debugging:
        print("\tenter_men_ke 进入门客界面 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_men-ke"]
    click_once(x, y, device = device, sleep_time=sleep_time)
    if debugging:
        print("\tenter_men_ke 进入门客界面 ends")

def enter_shang_pu(device = local_device, sleep_time = 1, wait_ratio = 5):
    if debugging:
        print("\tenter_shang_pu 商铺 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_shang-pu"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*wait_ratio)
    if debugging:
        print("\tenter_shang_pu 商铺 end")

def enter_chuang_dang(device = local_device, sleep_time = 1):
    if debugging:
        print("\tenter_chuang_dang 闯荡 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_chuang-dang"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*3)
    if debugging:
        print("\tenter_chuang_dang 闯荡 end")

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    if debugging:
        print("\tenter_cheng_jiao 进入城郊界面 begin")
    
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    x, y = home_bar["home_cheng-jiao"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    if debugging:
        print("\tenter_cheng_jiao 进入城郊界面 end")

def enter_bei_bao(device = local_device, sleep_time = 1):
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    if debugging:
        print("\tenter_bei_bao 进入背包界面 begin")
    x, y = home_bar["home_bei-bao"]
    click_once(x, y, device = device, sleep_time=sleep_time)
    if debugging:
        print("\tenter_bei_bao 进入背包界面 ends")

def enter_zhi_you(device = local_device, sleep_time = 1):
    if debugging: 
        print("\tenter_zhi_you 进入挚友界面 begin")
    from ADB_project.resources_1080_1920.home.home_data import zhi_you
    # enter home
    enter_home(device=device, sleep_time=sleep_time)
    # 进入挚友界面
    if zhi_you["move_to_left"] == True:
        move_to_left(device = device)
    drag_and_move(move_x=zhi_you["move_x"], move_y=0,device=device, duration_ms=zhi_you["duration_ms"])
    entry = zhi_you["entry"]
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    if debugging: 
        print("\tenter_zhi_you 进入挚友界面 ends")
    
########## GAME and EMULATOR ###############
@future_care
def start_emulator(emulator_path = ADB_project.functions.local_data.emulator_path):
    res = subprocess.run('START /b "%s"' %emulator_path, shell=True)
    if res.returncode == 0:
        print("Enter emulator successfully")
        return True
    else:
        print("Failed to enter emulator!!!!")
        return False

@future_care
def start_game(game_package = game_package_name, start_up_time = 60, device = local_device, sleep_time = None):
        
    if is_device_connected(device = device) == False:
        device = "localhost:"+str(find_available_port(5555, 5560))
    # check connectivity of the device found
    if not is_device_connected(device=device):
        print(f"{device} is not connected")
        class DeviceNotFoundException(Exception):
            pass 
        raise DeviceNotFoundException("No adb connected device was found")

    while (False == adb_start_activity(device= device, game_package=game_package)):
        if adb_debugging:
            print("last adb start game cmd was not success")
    # waits the game start
    # modified to image processing one
    time.sleep(start_up_time)
    
    # do with first page
    # modified to image processing one
    adb_start_activity(device = device, game_package = game_package)
    print("\t点击开始界面")
    click_painless(device=device, sleep_time=1, times = 10)
    
    # click Enter
    from ADB_project.resources_1080_1920.general import game 
    print("\t点击开始")
    start = game["start"]
    click_painless(device = device, sleep_time = 0.5, times = 10)
    clicks(start[0], start[1], device=device, sleep_time=0.5, times =4)
    click_wait(total_time=10, sleep_time = 1, device = device)
    
    print("等待进入home界面, 离线收益...")
    
    time.sleep(20)
    # do with init home page 
    print("\t\t点击离线收益")
    clicks(700, 1380, device=device, sleep_time=1, times = 1) # 离线收益
    enter_men_ke(device = device, sleep_time=1)
    print("\t\t点击进入活动")
    clicks(950, 1540, device=device, sleep_time=1, times = 1) # 离线收益
    click_exit(device = device, sleep_time = 1, times = 1)
    enter_men_ke(device = device, sleep_time=1)
    clicks(300, 1540, device=device, sleep_time=1, times = 1) # 离线收益
    click_exit(device = device, sleep_time = 1, times = 1)
    enter_men_ke(device = device, sleep_time=1)
    clicks(1020, 220, device=device, sleep_time=1, times = 1) # 首充礼包 容易点到特权 卡死
    click_exit(device = device, sleep_time = 1, times = 1)
    enter_men_ke(device = device, sleep_time=1)
    enter_home(device = device, sleep_time = 1)
    click_painless(device=device, sleep_time=0.5, times = 5)
    print("start_apk_game  启动游戏结束")
    return device

def activate_cache(device = local_device, sleep_time = 1):
    # build up cache in the game to avoid long loading time caused error
    funcs = [enter_chuang_dang, enter_cheng_jiao, enter_shang_pu, enter_home]
    for fun in funcs:
        fun(device = device, sleep_time = sleep_time)
        click_wait(total_time = 3, sleep_time = sleep_time, device = device)

