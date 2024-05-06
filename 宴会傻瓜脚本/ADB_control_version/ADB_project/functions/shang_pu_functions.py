import ADB_project
import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
import time
from ADB_project.functions.local_data import local_device, debugging
from ADB_project.functions.adb_operations import start_adb, is_device_connected, find_available_port, adb_start_activity, click_once, drag_and_move, obtain_screenshot, remove_local_file, move_to_bottom, move_to_end, move_to_left 
from ADB_project.functions.basic_dzg_functions import enter_home, enter_bei_bao,enter_cheng_jiao, enter_chuang_dang, enter_men_ke, enter_shang_pu, enter_zhi_you, click_exit, activate_cache, click_painless, click_wait, clicks, click_painless, click_exit

########## shang—pu ###############
@future_care
def shang_pu_four_hour_click():
    # 商铺四小时领取,的点击
    from ADB_project.functions.img_robots import ImgRobot
    screen_img = "my_screen.png"
    target_img = "frog_man.png"
    obtain_screenshot(img_name=screen_img, local_dir="./")
    robot_screen = ImgRobot(screen_img)
    robot_target = ImgRobot(target_img)
    print(robot_target.get_image_shape())
    print(robot_screen.get_brightness())
    result = robot_screen.find_image_position_with_robot(robot_target, threshold = 0.6)
    print(result)
    remove_local_file(screen_img)
    if result != None:
        for i in range(10, 500, 40):
            click_once(result[0] + i, result[1], sleep_time = 0.01)
        remove_local_file(screen_img)
        return True
    else: 
        remove_local_file(screen_img)
        return False

def click_qian_zhuang_from_home(times = 100, sleep_time = 0.1, device = local_device):
    if debugging: 
        print(f"click_qian_zhuang_from_home: times = {times}, device: {device}")
    enter_shang_pu(device=device, sleep_time=1)
    for _ in range(2):
        move_to_left(device = device)
    x,y = 300, 666
    clicks(x, y, device = device, sleep_time = sleep_time, times = times)
    if debugging: 
        print("click_qian_zhuang_from_home: end")
    
    enter_home(device=device, sleep_time=sleep_time)

def daily_qian_zhuang_20(device = local_device, sleep_time = 0.1):
    click_painless(device=device,sleep_time=sleep_time/3, times = 5)
    click_qian_zhuang_from_home(times=20*2, sleep_time=sleep_time, device = device)

def daily_do_shang_pu_qian_dao(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_do_shang_pu_qian_dao 商铺签到 begin")
    from ADB_project.resources_1080_1920.shang_pu.shang_pu_data import qian_dao
    toggle_open = qian_dao["toggle_open"]
    toggle_close = qian_dao["toggle_close"]
    do = qian_dao["do"]
    qian_dao_pos = qian_dao["qian_dao"]
    click_painless(device=device, sleep_time=sleep_time/3, times = 3)
    enter_shang_pu(device , sleep_time=sleep_time*3)
    move_to_left(device= device)
    
    click_once(toggle_close[0], toggle_close[1], device=device, sleep_time=sleep_time)
    click_once(toggle_open[0], toggle_open[1], device=device, sleep_time=sleep_time)
    click_once(qian_dao_pos[0], qian_dao_pos[1], device=device, sleep_time=sleep_time*3)
    clicks(do[0], do[1], device=device, sleep_time=sleep_time/2, times = 4)
    click_painless(device=device, sleep_time=sleep_time/2, times = 4)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_do_shang_pu_qian_dao 商铺签到 ends")
 
def daily_do_yi_guan(device = local_device, sleep_time = 1):
    from ADB_project.resources_1080_1920.shang_pu.shang_pu_data import yi_guan
    from ADB_project.resources_1080_1920.general import general_pos
    if debugging:
        print("    daily_do_yi_guan 医馆 starts")
    ex = general_pos["exit"]
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_left(device=device)
    one_click = yi_guan["one_click"]
    entry = yi_guan["entry"]
    do = yi_guan["do"]
    painless = yi_guan["painless"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        clicks(painless[0], painless[1], device=device, sleep_time=sleep_time, times = 3)
    click_exit(device = device, sleep_time = sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print("    daily_do_yi_guan 医馆 ens")

def daily_do_jiu_si (device = local_device, sleep_time = 1):
    if debugging:
        print("    daily_do_jiu_si 酒肆 begin")
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_left(device=device)
    from ADB_project.resources_1080_1920.shang_pu.shang_pu_data import jiu_si
    from ADB_project.resources_1080_1920.general import general_pos
    move = jiu_si["drag_move"]
    drag_and_move(move[0], move[1], device=device, duration_ms=500)
    one_click = jiu_si["one_click"]
    entry = jiu_si["entry"]
    do = jiu_si["do"]
    painless = jiu_si["painless"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        # click_painless(device=device, sleep_time=sleep_time, times = 3) # This would tricker unexpected
        clicks(x = painless[0], y = painless[1], device= device, sleep_time = sleep_time , times = 3)
    click_exit(device = device, sleep_time = sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print("    daily_do_jiu_si 酒肆 ends")

def daily_do_yao_pu (device = local_device, sleep_time = 1):
    if debugging:
        print("    daily_do_yao_pu 药铺 begin")
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_left(device=device)
    from ADB_project.resources_1080_1920.shang_pu.shang_pu_data import yao_pu
    from ADB_project.resources_1080_1920.general import general_pos
    move = yao_pu["drag_move"]
    drag_and_move(move[0], move[1], device=device, duration_ms=500)
    click_exit(device = device, sleep_time = sleep_time)
    one_click = yao_pu["one_click"]
    entry = yao_pu["entry"]
    do = yao_pu["do"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times = 3)
    click_exit(device = device, sleep_time = sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print("    daily_do_yao_pu 药铺 ends")

def daily_click_qian_zhuang_wei_ren(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_click_qian_zhuang_wei_ren begin")
    from ADB_project.resources_1080_1920.home.home_data import home_bar
    from ADB_project.resources_1080_1920.shang_pu.shang_pu_data import qian_zhuang
    # eneter shang pu
    enter_shang_pu(device = device, sleep_time = sleep_time * 5)
    move_to_left(device = device)
    time.sleep(sleep_time)
    # enter qian zhuang
    x, y = qian_zhuang["entry"]   
    click_once(x, y, device=device, sleep_time=sleep_time*3)
    
    x, y = qian_zhuang["wan-cheng"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)
    click_painless(device=device, sleep_time=sleep_time, times=5)
    x, y = qian_zhuang["yi-jian-wei-ren"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)


    x, y = qian_zhuang["wei-ren"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)
    # 退出 wei-ren page
    click_painless(device=device, sleep_time=sleep_time)
    
    # click center
    x, y = qian_zhuang["middle"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 迎财 5 次
    for _ in range(5):
        x, y = qian_zhuang["ying-cai"]
        click_once(x, y, device=device, sleep_time=sleep_time/2)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    
    # click 退出
    click_exit(device=device, sleep_time=sleep_time)

    # 回到 home
    x, y = home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)

    if debugging:
        print("daily_click_qian_zhuang_wei_ren end")

