import os
import subprocess
import time
import resources_1080_1920
import resources_1080_1920.general
import resources_1080_1920.cheng_jiao
import resources_1080_1920.cheng_jiao.cheng_jiao_data
import resources_1080_1920.home.home_data
import resources_1080_1920.shang_pu
import resources_1080_1920.shang_pu.shang_pu_data
from local_data import local_device

def click_once(x = 0, y = 0, device = local_device, sleep_time = None):
    if device == None:
        adb_command = ["adb", "shell", "input", "tap", str(x), str(y)]
    else:
        adb_command = ["adb", "-s" , device, "shell", "input", "tap", str(x), str(y)]
        
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    if sleep_time != None:
        time.sleep(sleep_time)

def clicks(x = 0, y = 0, device = local_device, sleep_time = 0.1, times = 1):
    for _ in range(times):
        click_once(x=x, y=y, device=device, sleep_time=sleep_time)

def click_painless(device = local_device, sleep_time = None, times = 1):
    for _ in range(times):
        click_once(x=500, y =5, device=device, sleep_time=sleep_time)

def drag_and_move(move_x=0, move_y=0, start_x=500, start_y=1000, device = local_device, duration_ms = 100):
    adb_command = ['adb',"-s", device, 'shell', 'input', 'swipe', str(start_x), str(start_y), str(start_x+move_x), str(start_y+move_y), str(duration_ms)]
    subprocess.run(adb_command)

def click_qian_zhuang_from_home(times = 100, sleep_time = 0.1, device = local_device):
    x, y = resources_1080_1920.home.home_data.home_bar["home_shang-pu"]
    subprocess.Popen(["adb", "-s", device, "shell", "input", "tap", str(x), str(y)])
    time.sleep(5)
    for _ in range(10):
        drag_and_move(move_x=800, move_y=0, start_x=100, start_y=1000, device=device, duration_ms=100)
        time.sleep(0.2)
    x,y = 300, 666
    for _ in range(times):
        subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
        time.sleep(sleep_time)
    
    enter_home(device=device, sleep_time=sleep_time)

def click_union_basic_constrcut(device = local_device, sleep_time = 1):
    # at home click cheng-jiao
    x, y = resources_1080_1920.home.home_data.home_bar["home_cheng-jiao"]
    click_once(x, y, device=device)
    time.sleep(sleep_time)
    # go to union
    x, y = 970, 650
    click_once(x, y, device=device)
    time.sleep(sleep_time)
    # click into construct page
    x, y = 950, 1550
    click_once(x, y, device=device)
    time.sleep(sleep_time)
    # basic construct
    x, y = 300, 950
    click_once(x, y, device=device)
    time.sleep(sleep_time)
    # finish constrcut notice
    click_painless(device=device)
    time.sleep(sleep_time)
    # back home
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device)
    time.sleep(sleep_time)

def daily_click_home_shang_cheng_ling_qu(device = local_device, sleep_time = 1):
    # 进入主页
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 从主页点击商城
    x, y = resources_1080_1920.home.home_data.home_right_low_list["home_shang-cheng"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # 点击道具
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["dao-ju"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 点击精力丹两次
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["dao-ju_jing-li-dan"]
    for _ in range(2):
        click_once(x, y, device=device, sleep_time=sleep_time)
    # 点击礼包
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["li-bao"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 点击免费的
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["li-bao_free"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # click painless
    for _ in range(2):
        click_painless(device=device, sleep_time=sleep_time)
    # 点击观影有礼
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["guan-ying-you-li"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 点击几次领取
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["guan-ying-you-li_ling-qu"]
    for _ in range(6):
        click_once(x, y, device=device, sleep_time=0.2)
        for _ in range(2):
            click_painless(device=device, sleep_time=sleep_time)
    # 点击领取资质丹
    x, y = resources_1080_1920.home.home_data.home_Shang_cheng["guan-ying-you-li_zi-zhi"]
    for _ in range(4):
        click_once(x, y, device=device, sleep_time=0.2)
    
    # 回到主页
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
def daily_click_xian_shi_chong_zhi(device= local_device, sleep_time = 1):
    # 主页
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)

    # 点击限时充值
    x, y = resources_1080_1920.home.home_data.home_upper_list["home_xian-shi-chong-zhi"]
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
    x, y = resources_1080_1920.general.general_pos["exit"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
# 需要修改，貌似如果程序过早退出，照片会搬运不完整，如何保证搬移完整后再退出程序？
def obtain_screenshot(img_name = "test.png", device = local_device):
    # yet implemented
    # ref: https://blog.csdn.net/fxdaniel/article/details/45846333
    # ref2: https://www.cnblogs.com/shaosks/p/14043177.html
    # bug 截图下半部分加载不完整
    adb_command = ["adb", "-s", device, "shell", "screencap -p", "/sdcard/" + img_name]
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    time.sleep(1)
    adb_command = ["adb", "-s", device, "pull", "/sdcard/"+img_name, "./"+img_name]
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    time.sleep(1)
    pass

def test_move_screenshot(img_name = "test.png", device = local_device):
    adb_command = ["adb", "-s", device, "pull", "/sdcard/"+img_name, "./"+img_name]
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    time.sleep(1)
    
def daily_click_qian_dao(device = local_device, sleep_time = 1):
    # eneter shang pu
    x, y = resources_1080_1920.home.home_data.home_bar["home_shang-pu"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # click 签到
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_dao["entry"]   
    click_once(x, y, device=device, sleep_time=sleep_time*2)
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_dao["qian-dao"]
    # click 退出签到
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_dao["exit"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # 回到 home
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)

def daily_click_qian_zhuang_wei_ren(device = local_device, sleep_time = 1):
    # eneter shang pu
    x, y = resources_1080_1920.home.home_data.home_bar["home_shang-pu"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    for _ in range(5):
        drag_and_move(move_x=500, move_y=0, start_x=500, start_y=1000, device=device)
        time.sleep(0.2)
    # enter qian zhuang
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["entry"]   
    click_once(x, y, device=device, sleep_time=sleep_time*3)
    
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["wan-cheng"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)
    click_painless(device=device, sleep_time=sleep_time, times=5)
    
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["yi-jian-wei-ren"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)


    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["wei-ren"]
    click_once(x, y, device=device, sleep_time=sleep_time*2)
    # 退出 wei-ren pagd
    click_painless(device=device, sleep_time=sleep_time)
    
    # click center
    x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["middle"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    # 迎财 10 次
    for _ in range(10):
        x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["ying-cai"]
        click_once(x, y, device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    
    # click 退出
    x, y = resources_1080_1920.general.general_pos["exit"]
    click_once(x, y, device=device, sleep_time=sleep_time)

    # 回到 home
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)

def remove_local_file(img_file_path="test.png"):
    if os.path.exists(img_file_path):
        os.remove(img_file_path)
    else:
        pass

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    x, y = resources_1080_1920.home.home_data.home_bar["home_cheng-jiao"]
    click_once(x,y, device=device, sleep_time=sleep_time)

def enter_home(device = local_device, sleep_time = 1):
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x,y, device=device, sleep_time=sleep_time)

def daily_click_rank(device = local_device, sleep_time = 1):
    ex, ey = resources_1080_1920.general.general_pos["exit"]
    enter_cheng_jiao(device=    device, sleep_time=sleep_time)
    
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["entry"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["ben_fu"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["enter_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["yi_jian_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    click_painless(device=device, sleep_time=sleep_time, times=8)
    
    # 点赞
    for _ in range(10):
        drag_and_move(move_x= 0, move_y=-800, start_x= 500, start_y=1200, device=device, duration_ms=200)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["person_pos"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    click_once(x,y+100,device=device,sleep_time=sleep_time)
    click_once(x,y+200,device=device,sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["person_bai_fang"]
    click_once(x,y,device=device,sleep_time=sleep_time*3)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["bai_fang_like"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["bai_fang_back"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    
    #进入跨服    
    click_once(ex,ey, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["kua_fu"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["enter_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.rank["yi_jian_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    click_painless(device=device, sleep_time=sleep_time, times=8)
    
    for _ in range(3):
        click_once(ex,ey, device=device, sleep_time=sleep_time)
    enter_home(device=device, sleep_time=sleep_time)

def daily_xing_yun_duo_bao_2(device = local_device, sleep_time = 1):
    # 赠送的幸运夺宝两次
    enter_home(device=  device, sleep_time=sleep_time)
    # 入口汇编会变！
    x, y = resources_1080_1920.home.home_data.xing_yun_duo_bao["entry"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    
    x, y = resources_1080_1920.home.home_data.xing_yun_duo_bao["duo_bao_five"]
    jx, jy = resources_1080_1920.home.home_data.xing_yun_duo_bao["tiao_guo"]
    for _ in range(2):
        click_once(x, y, device=device,sleep_time=sleep_time)
        click_once(jx, jy, device=device,sleep_time=sleep_time)
        
        click_painless(device=device, sleep_time=sleep_time, times=2)
    x, y = resources_1080_1920.general.general_pos["exit"]
    click_once(x, y, device=device, sleep_time=sleep_time)

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    x, y = resources_1080_1920.home.home_data.home_bar["home_cheng-jiao"]
    click_once(x, y, device=device, sleep_time=sleep_time)

def shang_zhan(device= local_device,sleep_time = 1):
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shang_zhan["entry"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*3)
    # 领取 money
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shang_zhan["money"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time)
    
    # 不检查是否点击了一键，做两次
    # 点击fight check
    for _ in range(2):
        x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shang_zhan["fight_check"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time)
        x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shang_zhan["fight"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time*3)
        x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shang_zhan["confirm_fight"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time)
        
        click_painless(device=device, sleep_time=sleep_time, times=2)
    enter_home(device=device, sleep_time=sleep_time)

def tu_di_raise_up(device = local_device, sleep_time = 1):
    # 容易出现弹窗，导致卡死。。。
    cx, cy = resources_1080_1920.home.home_data.tu_di["check"]
    delta = resources_1080_1920.home.home_data.tu_di["delta"]
    ex, ey = resources_1080_1920.general.general_pos["exit"]
    enter_home(device = device)
    for _ in range(5):
        drag_and_move(move_x=-500, move_y=0, start_x=600, start_y=1000, device=device, duration_ms=100)
        time.sleep(0.2)
    x, y = resources_1080_1920.home.home_data.tu_di["entry"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time)
    
    # 不检查是否 一键选中，做两次
    for _ in range(2):
        click_once(x = cx, y = cy, device= device, sleep_time=sleep_time)
        x, y = resources_1080_1920.home.home_data.tu_di["child0"]
        click_once(x, y, device= device, sleep_time=sleep_time)
        click_once(x = 500, y = 500, device= device, sleep_time=sleep_time)
        
        time.sleep(10)
        
        for _ in range(4):
            x += delta
            click_once(x, y, device= device, sleep_time=sleep_time)
            click_once(x = 500, y = 500, device= device, sleep_time=sleep_time)
            time.sleep(10)
    click_once(ex, ey, device= device, sleep_time=sleep_time)
    
def ri_chang_ren_wu_zhen_shou_five():
    # 珍兽技能五次
    pass
def guan_zhong_mao_yi():
    # 关中贸易
    pass
def ri_chang_ren_wu_zhi_you_five():
    # 挚友技能提升五次
    pass
def ri_chang_ren_wu_zhi_you_two():
    # 挚友赠送两次
    pass
def ri_chang_ren_wu_qian_zhuang_20(device = local_device, sleep_time = 0.1):
    click_qian_zhuang_from_home(times=20*2, sleep_time=sleep_time)
def ri_chang_ren_wu_zhi_you_tan_xin_five():
    # 挚友谈心五次
    pass
def ri_chang_ren_wu_tu_di_100():
    # 徒弟培养100次
    pass
