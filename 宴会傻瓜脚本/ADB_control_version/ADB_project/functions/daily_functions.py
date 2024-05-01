import ADB_project
import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
from ADB_project.functions.shang_pu_functions import daily_do_shang_pu_qian_dao, daily_click_qian_zhuang_wei_ren, daily_do_jiu_si, daily_do_yi_guan, daily_do_yao_pu,daily_qian_zhuang_20
from ADB_project.functions.adb_operations import start_adb, is_device_connected, find_available_port, adb_start_activity, click_once
from ADB_project.functions.basic_dzg_functions import activate_cache, click_wait, start_emulator, start_game, click_painless, enter_home , enter_bei_bao, enter_cheng_jiao, enter_chuang_dang, enter_men_ke, enter_shang_pu, enter_zhi_you
from ADB_project.functions.cheng_jiao_functions import click_union_basic_constrcut, shang_zhan
from ADB_project.functions.home_functions import daily_click_home_shang_cheng_ling_qu, daily_mail_process, daily_profile_yuan_bao, daily_recruit_10, daily_xing_yun_duo_bao_2, tu_di_raise_up, zhi_you_gift, zhi_you_skills, zhi_you_tan_xin, zhen_shou_raise
from ADB_project.functions.cheng_jiao_functions import daily_cai_shen_miao_like, daily_cheng_jiao_you_li, daily_click_rank, daily_ling_qu_yu_gan, daily_qiao_qian, daily_xing_shan
from ADB_project.functions.local_data import local_device, json_file_path, game_package_name, debugging
########## daily X ###############
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
    ADB_project.functions.json_function.update_xing_shan(json_file_path, to_do=False)

    # 商铺
    print("- "*10)
    daily_in_shang_pu   (device=device, sleep_time=sleep_time )

    # 日常闯荡一次
    print("- "*10)
    daily_in_chuang_dang(device=device, sleep_time=sleep_time )
    
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

def init(device = local_device):
    # start adb server, start emulator
    # return connected device (str localhost:xxxx)
    start_adb()
    was_emulator_on = is_device_connected(device)
    while start_emulator() == False:
        continue
    while is_device_connected(device) == False:
        device = "localhost:"+str(find_available_port(5555, 5560))
    if was_emulator_on == False:
        start_game(device=device)
    else: 
        adb_start_activity(device = device, game_package=game_package_name)
    return device



def daily_in_home(device = local_device, sleep_time = 1):
    if debugging:
       print("daily_in_home 执行home日常任务")
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    enter_home(device=device, sleep_time=sleep_time)
    # 身份元宝领取
    daily_profile_yuan_bao(device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 幸运夺宝
    daily_xing_yun_duo_bao_2(device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 免费商城领取
    daily_click_home_shang_cheng_ling_qu(device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 日常邮件
    daily_mail_process(device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 招聘10人
    daily_recruit_10(device = device, sleep_time = sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 徒弟培养
    tu_di_raise_up(device = device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 挚友谈心
    zhi_you_tan_xin(device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 挚友技能
    zhi_you_skills(device = device, sleep_time = sleep_time, times = 5)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 珍兽
    zhen_shou_raise(device = device, sleep_time = sleep_time, times = 5)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 挚友赠送
    zhi_you_gift(device=device, sleep_time = sleep_time, times = 2)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    
    if debugging:
       print("daily_in_home 执行home日常任务 ends")

def daily_in_cheng_jiao         (device= local_device, sleep_time=1, do_xing_shan = False):
    if debugging:
       print("daily_in_cheng_jiao 执行城郊日常任务")
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    enter_cheng_jiao            (device=device, sleep_time=sleep_time)
    # 行善
    if do_xing_shan == True:
        click_painless(device=device, sleep_time=sleep_time/3, times = 6)
        daily_xing_shan             (device=device, sleep_time=sleep_time)
    # 商会建设
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    click_union_basic_constrcut (device=device, sleep_time=sleep_time)
    # 商战
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    shang_zhan                  (device=device, sleep_time=sleep_time)
    # 排行榜点赞与上门点赞
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    daily_click_rank            (device=device, sleep_time=sleep_time)
    # 城郊游历
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    daily_cheng_jiao_you_li     (device=device, sleep_time=sleep_time)
    # 庄园与鱼竿领取
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    daily_ling_qu_yu_gan        (device=device, sleep_time=1)
    # 乔迁点赞
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    daily_qiao_qian             (device=device, sleep_time=sleep_time*0.8)
    # 财神庙点赞
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    daily_cai_shen_miao_like    (device=device, sleep_time=sleep_time*0.8)
    # back home
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    enter_home                  (device=device, sleep_time=sleep_time)
    if debugging:
       print("daily_in_cheng_jiao 执行城郊日常任务 ends")

def daily_in_shang_pu (device = local_device, sleep_time = 1):
    if debugging:
        print("daily_in_shang_pu 执行商铺日常任务")
    # 商铺签到
    daily_do_shang_pu_qian_dao  (device= device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 商铺-医馆
    daily_do_yi_guan            (device= device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 商铺-酒肆
    daily_do_jiu_si             (device= device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 商铺-药铺
    daily_do_yao_pu             (device= device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 商铺-钱庄20
    daily_qian_zhuang_20        (device= device, sleep_time=0.1)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    # 日常钱庄委任更换
    daily_click_qian_zhuang_wei_ren(device=device, sleep_time=1)
    click_painless(device=device, sleep_time=sleep_time/3, times = 6)
    
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_in_shang_pu 执行商铺日常任务 ends")

def daily_in_chuang_dang(device = local_device, sleep_time = 1):
    if debugging:
        print("ri_chang_chuang_dang begin")
    from ADB_project.resources_1080_1920.chuang_dang.chuang_dang_data import guan_ka
    # 日常闯荡
    enter_chuang_dang(device=device, sleep_time=sleep_time)
    # 进入关卡
    entry = guan_ka["entry"]
    do = guan_ka["do"]
    argue = guan_ka["argue"]
    later = guan_ka["later"]
    click_once(entry[0], entry[1], device, sleep_time=sleep_time*3)
    click_once(do[0], do[1], device=device, sleep_time=sleep_time*3)
    for _ in range(4):
        click_once(later[0], later[1], device=device, sleep_time=sleep_time)
        click_once(argue[0], argue[1], device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time/2, times = 2)
    # 不考虑 满的情况
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("    ri_chang_chuang_dang end")

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
    ADB_project.functions.json_function.update_xing_shan(json_file_path, to_do=False)

    # 商铺
    print("- "*10)
    daily_in_shang_pu   (device=device, sleep_time=sleep_time )

    # 日常闯荡一次
    print("- "*10)
    daily_in_chuang_dang(device=device, sleep_time=sleep_time )
    
    # wait 10 minutes
    print("- "*10)
    for _ in range(3):
        click_wait(total_time=60*10, sleep_time=50, device=device)
        click_union_basic_constrcut(device=device)
    for _ in range(4):
        click_wait(total_time=1800, sleep_time=50, device=device)
        sz_data(device=device)
    print("daily_do_once ends")
    print("- " * 20)

