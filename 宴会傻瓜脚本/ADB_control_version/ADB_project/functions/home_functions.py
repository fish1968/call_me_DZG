import time
import ADB_project
from ADB_project.functions.set_funcs_dir import future_care
from ADB_project.functions.local_data import local_device, debugging 
from ADB_project.functions.adb_operations import click_once
from ADB_project.functions.adb_operations import start_adb, is_device_connected, find_available_port, adb_start_activity, click_once, drag_and_move
from ADB_project.functions.basic_dzg_functions import enter_home, enter_bei_bao,enter_cheng_jiao, enter_chuang_dang, enter_men_ke, enter_shang_pu, enter_zhi_you, click_exit, activate_cache, click_painless, click_wait, clicks, click_painless, click_exit
from ADB_project.functions.adb_operations import obtain_screenshot, remove_local_file, move_to_bottom, move_to_end, move_to_left
########## home ###############

def daily_xing_yun_duo_bao_2(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_xing_yun_duo_bao_2 幸运夺宝 begin")
    from ADB_project.resources_1080_1920.home.home_data import xing_yun_duo_bao
    # 赠送的幸运夺宝两次
    enter_home(device=  device, sleep_time=sleep_time)
    # 入口汇编会变！
    entry = xing_yun_duo_bao["entry"]
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    
    duo_bao_five_entry = xing_yun_duo_bao["duo_bao_five"]
    skip = xing_yun_duo_bao["tiao_guo"]
    for _ in range(2):
        click_once(duo_bao_five_entry[0], duo_bao_five_entry[1], device=device,sleep_time=sleep_time)
        click_once(skip[0], skip[1], device=device,sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times=2)
    
    click_exit(device = device, sleep_time = sleep_time)
    if debugging:
        print("daily_xing_yun_duo_bao_2 幸运夺宝 end")

def daily_profile_yuan_bao(device = local_device, sleep_time = 1):
    print("enter daily_profile_yuan_bao 身份元宝")
    from ADB_project.resources_1080_1920.home.home_data import profile
    from ADB_project.resources_1080_1920.general import general_pos
    entry = profile["entry"]
    obtain = profile["obtain"]
    click_painless(device=device, sleep_time=sleep_time,times=2)
    enter_home(device=device,sleep_time=sleep_time)
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    clicks(obtain[0], obtain[1], device=device, sleep_time=sleep_time, times=2)
    click_painless(device=device, sleep_time=sleep_time,times=2)
    click_exit(device = device, sleep_time = sleep_time)
    print("enter daily_profile_yuan_bao 身份元宝 ends")
def daily_mail_process(device = local_device, sleep_time  = 1):
    if debugging:
        print("daily_mail_process begins")
    enter_home(device, sleep_time)
    from ADB_project.resources_1080_1920.home.home_data import mail_list
    mail = mail_list["mail"]
    del_read = mail_list["del_read"]
    one_click = mail_list["one_click"]
    toggle_hide = mail_list["toggle_hide"]
    toggle_open = mail_list["toggle_open"]
    click_once(toggle_hide[0], toggle_hide[1], device=device, sleep_time=sleep_time)
    click_once(toggle_open[0], toggle_open[1], device=device, sleep_time=sleep_time)
    click_once(mail[0], mail[1], device=device, sleep_time=sleep_time)
    click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time)
    clicks(del_read[0], del_read[1], device=device, sleep_time=sleep_time, times = 3)
    click_painless(device=device, sleep_time=sleep_time/5, times=3)
    if debugging:
        print("daily_mail_process ends")

@future_care
def tu_di_raise_up_fixed_slow_version(device = local_device, sleep_time = 1):
    if debugging:
        print("tu_di_raise_up 徒弟培养 ")
    # 容易出现弹窗，导致卡死。。。
    from ADB_project.resources_1080_1920.home.home_data import tu_di
    check = tu_di["check"]
    delta = tu_di["delta"]
    entry = tu_di["entry"]
    child0 = tu_di["child0"]
    enter_home(device = device)
    for _ in range(5):
        drag_and_move(move_x=-500, move_y=0, start_x=600, start_y=1000, device=device, duration_ms=100)
        # time.sleep(0.2)
    click_once(x = entry[0], y = entry[1], device= device, sleep_time=sleep_time)
    
    # 不检查是否 一键选中，做两次
    x, y = child0
    for _ in range(2):
        click_once(x = check[0], y = check[1], device= device, sleep_time=sleep_time)
        click_once(child0[0], child0[1], device= device, sleep_time=sleep_time)
        click_once(x = 500, y = 500, device= device, sleep_time=sleep_time)
        
        time.sleep(10)
        
        for _ in range(4):
            x += delta
            click_once(x, y, device= device, sleep_time=sleep_time)
            click_once(x = 500, y = 500, device= device, sleep_time=sleep_time)
            time.sleep(10)
    click_exit(device= device, sleep_time=sleep_time)

def daily_click_xian_shi_chong_zhi(device= local_device, sleep_time = 1):
    if debugging:
        print("daily_click_xian_shi_chong_zhi begin")
    # 主页
    from ADB_project.resources_1080_1920.home.home_data import home_upper_list
    enter_home(device=device, sleep_time=sleep_time)

    # 点击限时充值
    x, y = home_upper_list["home_xian-shi-chong-zhi"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 不管顺序了，两个都点一次
    x, y = (120, 270)
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = (900, 550)
    click_once(x, y, device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time)
    x, y = (300, 270)
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    x, y = (900, 550)
    click_once(x, y, device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time)
    
    # exit
    click_exit(x, y, device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_click_xian_shi_chong_zhi end")
def daily_click_home_shang_cheng_ling_qu(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_click_home_shang_cheng_ling_qu 商城领取 begin")
    from ADB_project.resources_1080_1920.home.home_data import home_right_low_list, home_Shang_cheng
    # 进入主页
    enter_home(device = device, sleep_time = sleep_time)
    # 从主页点击商城
    shang_cheng = home_right_low_list["home_shang-cheng"]
    click_once(shang_cheng[0], shang_cheng[1], device=device, sleep_time=sleep_time)
    # 点击道具
    dao_ju = home_Shang_cheng["dao-ju"]
    click_once(dao_ju[0], dao_ju[1], device=device, sleep_time=sleep_time)
    
    # 点击精力丹两次
    x, y = home_Shang_cheng["dao-ju_jing-li-dan"]
    clicks(x, y, device=device, sleep_time=sleep_time, times = 2)
    # 点击礼包
    x, y = home_Shang_cheng["li-bao"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    cancel = (365, 1050)
    click_once(cancel[0], cancel[1], device=device, sleep_time=sleep_time) # 点击过的情况 会进入购买，需要取消退出
    # 点击免费的
    x, y = home_Shang_cheng["li-bao_free"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = home_Shang_cheng["cancel_buy"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # click painless
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    # 点击观影有礼
    x, y = home_Shang_cheng["guan-ying-you-li"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 点击几次领取
    x, y = home_Shang_cheng["guan-ying-you-li_ling-qu"]
    for _ in range(6):
        click_once(x, y, device=device, sleep_time=0.2)
        click_painless(device=device, sleep_time=sleep_time, times = 2)
    # 点击领取资质丹
    x, y = home_Shang_cheng["guan-ying-you-li_zi-zhi"]
    clicks(x, y, device=device, sleep_time=0.2, times = 4)
    
    # 回到主页
    enter_home(device=device, sleep_time=sleep_time)
    
    if debugging:
        print("daily_click_home_shang_cheng_ling_qu 商城领取 end")

@future_care
def daily_recruit_10(device = local_device, sleep_time = 1):
    mu_1_path = r"ADB_project\resources_1080_1920\home\imgs\mu1.png"
    screen_name = "screen.png"
    enter_home(device = device, sleep_time = sleep_time)
    enter_bei_bao(device = device, sleep_time = sleep_time)
    # by default it enters dao-ju page
    drag_and_move(move_x = 0, move_y = -800, device = device, duration_ms = 500)
    from ADB_project.functions.img_robots import ImgRobot
    robo_mu_1 = ImgRobot(mu_1_path)
    obtain_screenshot(screen_name, local_dir = "./")
    robo_screen = ImgRobot(screen_name)
    res = robo_screen.find_image_position_with_robot(robo_mu_1)
    if res != None:
        click_once(res[0], res[1], device = device, sleep_time = sleep_time)
    x, y = 882, 1138
    clicks(x, y, device = local_device, sleep_time=sleep_time/4, times = 10)
    x, y = 541, 1282
    click_once(x, y, device = local_device, sleep_time=sleep_time)
    enter_home(device, sleep_time=sleep_time)
    remove_local_file(screen_name)

@DeprecationWarning
def daily_recruit_10_fix(device = local_device, sleep_time = 1):
    # 位置写死，有图像识别更好
    enter_home(device = device, sleep_time = sleep_time)
    enter_bei_bao(device, sleep_time=sleep_time)
    x, y = 197, 197
    click_once(x, y, device = local_device, sleep_time=sleep_time)
    x, y = 941, 1586
    click_once(x, y, device = local_device, sleep_time=sleep_time)
    x, y = 882, 1138
    clicks(x, y, device = local_device, sleep_time=sleep_time/4, times = 10)
    x, y = 541, 1282
    click_once(x, y, device = local_device, sleep_time=sleep_time)
    enter_home(device, sleep_time=sleep_time)

@future_care
def zhen_shou_raise(device = local_device, sleep_time = 1, times = 5):
    # 珍兽技能五次
    if debugging:
        print("zhen_shou_raise begins")
    enter_men_ke(device=device, sleep_time=sleep_time)
    x, y = 682, 1664
    click_once(x, y, device = device, sleep_time=sleep_time)
    move_to_bottom(local_device)
    x, y = 562, 768
    click_once(x, y, device = device, sleep_time=sleep_time)
    x, y = 120, 1200 
    click_once(x, y, device = device, sleep_time=sleep_time)
    x, y = 552, 1250
    click_once(x, y, device = device, sleep_time=sleep_time)
    x, y = 661, 1386
    click_once(x, y, device = device, sleep_time=sleep_time)
    x, y = 896, 1674
    clicks(x, y, device = device, sleep_time=sleep_time, times = times+1)
    click_exit(device = device, sleep_time=sleep_time, times = 4)
    if debugging:
        print("zhen_shou_raise ends")

@future_care
def zhi_you_skills(device = local_device, sleep_time = 1, times = 5):
    # 挚友技能提升 5 次
    if debugging: 
        print(f"zhi_you_skills 挚友技能 {times}次 begin")
    from ADB_project.resources_1080_1920.home.home_data import zhi_you
    # 进入挚友界面
    enter_zhi_you(device=device, sleep_time=sleep_time)
    
    one_zhi_you = 800, 480
    click_once(one_zhi_you[0], one_zhi_you[1], device=device, sleep_time=sleep_time)
    ji_neng = 98, 1042
    one_skill = 424, 933
    do_skill = 856, 1240
    # 点击技能页面
    click_once(ji_neng[0], ji_neng[1], device=device, sleep_time=sleep_time)
    # 点击一个技能槽
    click_once(one_skill[0], one_skill[1], device=device, sleep_time=sleep_time)
    # 点击提升skill
    clicks(do_skill[0], do_skill[1], device=device, sleep_time=sleep_time, times = times)
    click_exit(device = device, sleep_time = sleep_time, times = 3)
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    if debugging: 
        print(f"zhi_you_skills 挚友技能 {times}次 ends")

@future_care
def zhi_you_gift(device = local_device, sleep_time = 1, times = 2):
    # 挚友赠送 >= times 次
    if debugging: 
        print(f"zhi_you_gift 挚友赠送 {times}次 begin")
    from ADB_project.resources_1080_1920.home.home_data import zhi_you
    # enter home
    enter_home(device=device, sleep_time=sleep_time)
    # 进入挚友界面
    enter_zhi_you(device = device, sleep_time = sleep_time)
    one_zhi_you = 800, 480
    click_once(one_zhi_you[0], one_zhi_you[1], device=device, sleep_time=sleep_time)
    mu_shu = 184, 1794
    one_click = 329, 646
    do = 920, 1781
    do_times = int(times/5) + int(times/2) + 1
    for _ in range(do_times):
        click_once(mu_shu[0], mu_shu[1], device=device, sleep_time=sleep_time)
        click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time)
        click_once(do[0], do[1], device=device, sleep_time=sleep_time)
    click_exit(device = device, sleep_time = sleep_time, times = 3)
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    if debugging: 
        print(f"zhi_you_gift 挚友赠送 {times}次 ends")

def zhi_you_tan_xin(device = local_device, sleep_time = 1):
    if debugging:
        print("zhi_you_tan_xin 挚友谈心 begin")
    from ADB_project.resources_1080_1920.home.home_data import zhi_you
    enter_home(device=device, sleep_time=sleep_time)
    if zhi_you["move_to_left"] == True:
        move_to_left(device = device)
    drag_and_move(move_x=zhi_you["move_x"], move_y=0,device=device, duration_ms=zhi_you["duration_ms"])
    entry = zhi_you["entry"]
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    # 点击谈心
    tan_xin = zhi_you["tan_xin"]
    one_click = zhi_you["one_click"]
    for _ in range(4):
        click_once(x=tan_xin[0], y = tan_xin[1], device = device, sleep_time = sleep_time)
        click_painless(device=device, sleep_time = sleep_time, times = 10)
        # 一键谈心 按钮
        click_once(x = one_click[0], y = one_click[1], device = device, sleep_time = sleep_time)
    click_exit(device = device, sleep_time = sleep_time, times = 3)
    enter_home(device = device, sleep_time=sleep_time)
    if debugging:
        print("zhi_you_tan_xin 挚友谈心 ends")

def tu_di_raise_up(device = local_device, sleep_time = 1):
    from ADB_project.resources_1080_1920.home.home_data import tu_di
    # enter home
    enter_home(device = device, sleep_time = sleep_time)
    if tu_di["move_left"] == True:
        move_to_left(device = device)
    drag_and_move(move_x=tu_di["move_x"], device=device, duration_ms=tu_di["duration_ms"])
    entry = tu_di["entry"]
    click_once(entry[0], entry[1], device = device, sleep_time = sleep_time)
    for _ in range(2):
        click_once(tu_di["info"][0], tu_di["info"][1], device = device, sleep_time = sleep_time)
        click_once(tu_di["toggle"][0], tu_di["toggle"][1], device = device, sleep_time = sleep_time)
        click_painless(device, sleep_time, times = 3)
        for _ in range(2):
            click_once(tu_di["one_click"][0], tu_di["one_click"][1], device = device, sleep_time = sleep_time)
            clicks(tu_di["do"][0], tu_di["do"][1], device = device, sleep_time = sleep_time/3, times = 3)
            click_painless(device, sleep_time=sleep_time/2, times = 3)
            time.sleep(sleep_time*4)
    click_exit(device, sleep_time = sleep_time , times = 3)
    enter_home(device = device, sleep_time=sleep_time)

