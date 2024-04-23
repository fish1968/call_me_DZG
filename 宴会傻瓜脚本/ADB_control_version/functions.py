import os
import subprocess
import time
import resources_1080_1920
import resources_1080_1920.chuang_dang
import resources_1080_1920.chuang_dang.chuang_dang_data
import resources_1080_1920.general
import resources_1080_1920.cheng_jiao
import resources_1080_1920.cheng_jiao.cheng_jiao_data
import resources_1080_1920.home.home_data
import resources_1080_1920.shang_pu
import resources_1080_1920.shang_pu.shang_pu_data
from local_data import local_device, debugging, apk_start_path

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

def move_to_end(left =0, right = 0, top = 0, bottom = 0, sleep_time = .5, device = local_device):
    move_x = 0
    move_y = 0
    if left == 1:
        move_x = 4000
        print("    move to the left")
    elif right == 1:
        move_x = -4000
        print("    move to the right")
    elif top == 1:
        move_y = 8000
        print("    move to the top")
    elif bottom == 1:
        move_y = -8000
        print("    move to the bottom")
    else:
        print("    No move")
    drag_and_move(move_x=move_x, move_y=move_y, device=device, duration_ms=int(sleep_time*1000))
    time.sleep(sleep_time)
    print("    move ends")

def start_apk_game(game_path = apk_start_path, start_up_time = 120, device = local_device):
    res = subprocess.run('START /b %s' %game_path, shell=True)
    if res.returncode == 0:
        print("Enter game sucess")
    else:
        print("Failed to enter Game!!!!")
        exit()
    print("等待 虚拟机启动")
    time.sleep(30)
    print("ADB 尝试连接")
    cmd = ["adb", "connect" , device]
    res = subprocess.run(cmd, shell=True)
    res = subprocess.run(cmd, shell=True)
    if res.returncode == 0:
        print("adb 连接成功")
    else:
        print("adb 连接失败，尝试 locahost:5556")
        cmd[-1] = "localhost:5556"
        device = "localhost:5556"
        res = subprocess.run(cmd, shell=True)
        if res.returncode == 0:
            print('adb 连接成功')
        else:
            print("adb 再次连接失败")
            exit()
    print("android 开启等待")
    time.sleep(start_up_time) # android start time
    print("游戏 开启等待")
    
    time.sleep(60) # game wait time
    # do with first page
    print("\t点击开始界面")
    click_painless(device=device, sleep_time=1, times = 10)
    
    # click enter 
    from resources_1080_1920.general import game, general_pos
    print("\t点击开始")
    start = game["start"]
    clicks(start[0], start[1], device=device, sleep_time=0.5, times = 10)
    time.sleep(10)
    ex = general_pos["exit"]
    # do with init home page 
    for _ in range(4):
        print("\t\t点击离线收益")
        clicks(700, 1380, device=device, sleep_time=1, times = 2) # 离线收益
        
        print("\t\t点击进入活动")
        clicks(950, 1540, device=device, sleep_time=1, times = 2) # 离线收益
        clicks(300, 1540, device=device, sleep_time=1, times = 2) # 离线收益
        clicks(1020, 220, device=device, sleep_time=1, times = 2) # 首充礼包 容易点到特权 卡死
        print("\t\t无痛点击")
        click_painless(device=device, sleep_time=0.5, times = 5)
        print("\t\t点击退出")
        clicks(ex[0], ex[1], device=device, sleep_time=1, times = 3) 
    click_painless(device=device, sleep_time=0.5, times = 5)
    print("start_apk_game  启动游戏结束")

def click_qian_zhuang_from_home(times = 100, sleep_time = 0.1, device = local_device):
    if debugging: 
        print(f"click_qian_zhuang_from_home: times = {times}, sleep_time: {sleep_time}, device: {device}")
    enter_shang_pu(device=device, sleep_time=sleep_time)
    for _ in range(10):
        drag_and_move(move_x=800, move_y=0, start_x=100, start_y=1000, device=device, duration_ms=100)
        time.sleep(0.2)
    x,y = 300, 666
    for _ in range(times):
        subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
        time.sleep(sleep_time)
    if debugging: 
        print(f"click_qian_zhuang_from_home: end")
    
    enter_home(device=device, sleep_time=sleep_time)

def click_union_basic_constrcut(device = local_device, sleep_time = 1):
    if debugging:
        print(f"click_union_basic_constrcut begin")
    # at home click cheng-jiao
    enter_home(device=device, sleep_time=sleep_time*3)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*3)
    # go to union
    x, y = 970, 650
    click_once(x, y, device=device, sleep_time=sleep_time)
    # click into construct page
    x, y = 950, 1550
    click_once(x, y, device=device, sleep_time=sleep_time)
    # basic construct
    x, y = 300, 950
    click_once(x, y, device=device, sleep_time=sleep_time)
    # finish constrcut notice
    click_painless(device=device, sleep_time=sleep_time)
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print(f"click_union_basic_constrcut end")

def daily_click_home_shang_cheng_ling_qu(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_click_home_shang_cheng_ling_qu 商城领取 begin")
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
    cancel = (365, 1050)
    click_once(cancel[0], cancel[1], device=device, sleep_time=sleep_time) # 点击过的情况 会进入购买，需要取消退出
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
    
    if debugging:
        print(f"daily_click_home_shang_cheng_ling_qu 商城领取 end")

def daily_click_xian_shi_chong_zhi(device= local_device, sleep_time = 1):
    if debugging:
        print(f"daily_click_xian_shi_chong_zhi begin")
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
    if debugging:
        print(f"daily_click_xian_shi_chong_zhi end")
    
# 需要修改，貌似如果程序过早退出，照片会搬运不完整，如何保证搬移完整后再退出程序？
def obtain_screenshot(img_name = "test.png", device = local_device):
    if debugging:
        print(f"obtain_screenshot: img_name = {img_name}")
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
    if debugging:
        print(f"obtain_screenshot: img_name = {img_name} end")


def test_move_screenshot(img_name = "test.png", device = local_device):
    if debugging:
        print(f"test_move_screenshot: img_name = {img_name} begin")
    adb_command = ["adb", "-s", device, "pull", "/sdcard/"+img_name, "./"+img_name]
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    time.sleep(1)
    if debugging:
        print(f"test_move_screenshot: img_name = {img_name} end")
    
def daily_click_qian_dao(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_click_qian_dao: begin")
    
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

    if debugging:
        print(f"daily_click_qian_dao: end")

def daily_click_qian_zhuang_wei_ren(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_click_qian_zhuang_wei_ren begin")
    # eneter shang pu
    x, y = resources_1080_1920.home.home_data.home_bar["home_shang-pu"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    drag_and_move(move_x=500*10, move_y=0, start_x=500, start_y=1000, device=device, duration_ms=sleep_time*1000)
    time.sleep(sleep_time)
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
    
    # 迎财 5 次
    for _ in range(5):
        x, y = resources_1080_1920.shang_pu.shang_pu_data.qian_zhuang["ying-cai"]
        click_once(x, y, device=device, sleep_time=sleep_time/2)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    
    # click 退出
    x, y = resources_1080_1920.general.general_pos["exit"]
    click_once(x, y, device=device, sleep_time=sleep_time)

    # 回到 home
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x, y, device=device, sleep_time=sleep_time)

    if debugging:
        print(f"daily_click_qian_zhuang_wei_ren end")
def remove_local_file(img_file_path="test.png"):
    if debugging:
        print(f"remove_local_file img_path = {img_file_path} begin")
    if os.path.exists(img_file_path):
        os.remove(img_file_path)
    else:
        pass
    if debugging:
        print(f"remove_local_file img_path = {img_file_path} end")

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    if debugging:
        print(f"    enter_cheng_jiao 进入城郊界面 begin")
    x, y = resources_1080_1920.home.home_data.home_bar["home_cheng-jiao"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    if debugging:
        print(f"    enter_cheng_jiao 进入城郊界面 end")

def enter_home(device = local_device, sleep_time = 1):
    if debugging:
        print(f"    enter_home 进入首页界面 begin")
    x, y = resources_1080_1920.home.home_data.home_bar["home_home"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    if debugging:
        print(f"    enter_home 进入首页界面 end")

def enter_cheng_jiao(device = local_device, sleep_time = 1):
    if debugging:
        print(f"    enter_cheng_jiao 进入城郊界面 begin")
    x, y = resources_1080_1920.home.home_data.home_bar["home_cheng-jiao"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    if debugging:
        print(f"    enter_cheng_jiao 进入城郊界面 end")

def enter_chuang_dang(device = local_device, sleep_time = 1):
    if debugging:
        print(f"    ente_chuang_dang 城郊 begin")
    x, y = resources_1080_1920.home.home_data.home_bar["home_chuang-dang"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*3)
    if debugging:
        print(f"    ente_chuang_dang 闯荡 end")

def enter_shang_pu(device = local_device, sleep_time = 1, wait_ratio = 5):
    if debugging:
        print(f"    ente_shang_pu 商铺 begin")
    x, y = resources_1080_1920.home.home_data.home_bar["home_shang-pu"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*wait_ratio)
    if debugging:
        print(f"    ente_shang_pu 商铺 end")

def daily_do_yi_guan(device = local_device, sleep_time = 1):
    from resources_1080_1920.shang_pu.shang_pu_data import yi_guan
    from resources_1080_1920.general import general_pos
    if debugging:
        print(f"    daily_do_yi_guan 医馆 starts")
    ex = general_pos["exit"]
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_end(left = 1, sleep_time=sleep_time, device=device)
    one_click = yi_guan["one_click"]
    entry = yi_guan["entry"]
    do = yi_guan["do"]
    painless = yi_guan["painless"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        clicks(painless[0], painless[1], device=device, sleep_time=sleep_time, times = 3)
    click_once(ex[0], ex[1], device = device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print(f"    daily_do_yi_guan 医馆 ens")

def daily_do_jiu_si (device = local_device, sleep_time = 1):
    if debugging:
        print(f"    daily_do_jiu_si 酒肆 begin")
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_end(left = 1, sleep_time=sleep_time, device=device)
    from resources_1080_1920.shang_pu.shang_pu_data import jiu_si
    from resources_1080_1920.general import general_pos
    move = jiu_si["drag_move"]
    ex = general_pos["exit"]
    drag_and_move(move[0], move[1], device=device, duration_ms=500)
    one_click = jiu_si["one_click"]
    entry = jiu_si["entry"]
    do = jiu_si["do"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times = 3)
    click_once(ex[0], ex[1], device = device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print(f"    daily_do_jiu_si 酒肆 ends")
def daily_do_yao_pu (device = local_device, sleep_time = 1):
    if debugging:
        print(f"    daily_do_yao_pu 药铺 begin")
    click_painless(device=device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    enter_shang_pu(device=device, sleep_time=sleep_time)
    move_to_end(left = 1, sleep_time=sleep_time, device=device)
    from resources_1080_1920.shang_pu.shang_pu_data import yao_pu
    from resources_1080_1920.general import general_pos
    move = yao_pu["drag_move"]
    ex = general_pos["exit"]
    drag_and_move(move[0], move[1], device=device, duration_ms=500)
    one_click = yao_pu["one_click"]
    entry = yao_pu["entry"]
    do = yao_pu["do"]
    click_once(ex[0], ex[1], device = device, sleep_time=sleep_time)
    one_click = yao_pu["one_click"]
    entry = yao_pu["entry"]
    do = yao_pu["do"]
    click_once(entry[0], entry[1], device = device, sleep_time=sleep_time*10)
    for _ in range(2):
        click_once(one_click[0], one_click[1], device = device, sleep_time=sleep_time)
        click_once(do[0], do[1], device = device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times = 3)
    click_once(ex[0], ex[1], device = device, sleep_time=sleep_time)
    enter_home(device=device,sleep_time=sleep_time)
    if debugging:
        print(f"    daily_do_yao_pu 药铺 ends")

def daily_click_rank(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_click_rank 排行榜点赞 begin")
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
    for _ in range(3):
        drag_and_move(move_x= 0, move_y=-3000, start_x= 500, start_y=1200, device=device, duration_ms=200)
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
    if debugging:
        print(f"daily_click_rank 排行榜点赞 end")

def daily_xing_yun_duo_bao_2(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_xing_yun_duo_bao_2 幸运夺宝 begin")
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

    if debugging:
        print(f"daily_xing_yun_duo_bao_2 幸运夺宝 end")

def daily_profile_yuan_bao(device = local_device, sleep_time = 1):
    print("enter daily_profile_yuan_bao 身份元宝")
    from resources_1080_1920.home.home_data import profile
    from resources_1080_1920.general import general_pos
    ex = general_pos["exit"]
    entry = profile["entry"]
    obtain = profile["obtain"]
    click_painless(device=device, sleep_time=sleep_time,times=2)
    enter_home(device=device,sleep_time=sleep_time)
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    clicks(obtain[0], obtain[1], device=device, sleep_time=sleep_time, times=2)
    click_painless(device=device, sleep_time=sleep_time,times=2)
    click_once(ex[0], ex[1], device=device, sleep_time=sleep_time)
    print("enter daily_profile_yuan_bao 身份元宝 ends")
    
def daily_qiao_qian(device = local_device, sleep_time = 1):
    
    from resources_1080_1920.cheng_jiao.cheng_jiao_data import qiao_qian
    print("daily_qiao_qian begin")
    enter_home(device= device, sleep_time=sleep_time)
    enter_cheng_jiao(device= device, sleep_time=sleep_time)
    entry = qiao_qian["entry"]
    low_like = qiao_qian["low_like"]
    huang_like = qiao_qian["huang_like"]
    huang_entry = qiao_qian["huang_entry"]
    qin_entry = qiao_qian["qin_entry"]
    bei_shan_entry = qiao_qian["bei_shan_entry"]
    move_y = qiao_qian["bei_shan_move_y"]
    ex = resources_1080_1920.general.general_pos["exit"]
    click_once(x=entry[0], y = entry[1], device=device,sleep_time=sleep_time*2)
    
    click_once(huang_entry[0], huang_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(huang_like[0], huang_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_once(ex[0], ex[1], device=device,sleep_time=sleep_time)
    
    click_once(qin_entry[0], qin_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(low_like[0], low_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_once(ex[0], ex[1], device=device,sleep_time=sleep_time)

    drag_and_move(move_y=move_y, device=device,duration_ms=sleep_time*1000)
    time.sleep(sleep_time)
    click_once(bei_shan_entry[0], bei_shan_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(low_like[0], low_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_once(ex[0], ex[1], device=device,sleep_time=sleep_time)

    enter_home(device= device, sleep_time=sleep_time)
    print("daily_qiao_qian ends")

def daily_mail_process(device = local_device, sleep_time  = 1):
    enter_home(device, sleep_time)
    from resources_1080_1920.home.home_data import mail_list
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
    
    
def shang_zhan(device= local_device,sleep_time = 1):
    if debugging:
        print(f"shang_zhan 商战")
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
        
        click_painless(device=device, sleep_time=sleep_time, times=4)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print(f"shang_zhan 商战 end now at home")

def tu_di_raise_up(device = local_device, sleep_time = 1):
    if debugging:
        print(f"tu_di_raise_up 徒弟培养 ")
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

    if debugging:
        print(f"tu_di_raise_up 徒弟培养 end")

def daily_cheng_jiao_you_li(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_cheng_jiao_you_li 城郊游历")
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*2)

    # 进入游历
    move_x, move_y = resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["drag_move"]
    drag_and_move(move_x=move_x, move_y=move_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    x, y =resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["entry"]
    click_once(x, y , device=device, sleep_time=sleep_time*3) # easily blocked
    # 赠礼
    gift_entry =resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["shi_jiao_gift"] 
    donate =resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["shi_jiao_give"] 
    obtain =resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["shi_jiao_obtain"] 
    click_once(gift_entry[0], gift_entry[1], device=device, sleep_time=sleep_time*3)
    click_once(donate[0], donate[1], device=device, sleep_time=sleep_time)
    click_once(obtain[0], obtain[1], device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times =  2)
    
    cx, cy = resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["ya_jiu"] # center position
    mx, my = resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["men_ke_xuan_ze"] # men position
    dx, dy = resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["drink"] # drink wine
    x, y =resources_1080_1920.cheng_jiao.cheng_jiao_data.you_li["you_li_5"]
    for _ in range(2):
        click_once(x, y , device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times=3)
        click_once(mx, my, device=device, sleep_time=sleep_time)
        click_once(dx, dy, device=device, sleep_time=sleep_time)
        click_once(cx, cy, device=device, sleep_time=sleep_time)
    
    for _ in range(10):
        click_once(cx, cy, device=device, sleep_time=sleep_time)
        click_once(dx, dy, device=device, sleep_time=sleep_time)
        click_once(mx, my, device=device, sleep_time=sleep_time)
        click_painless(device, sleep_time=sleep_time, times=2)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print(f"daily_cheng_jiao_you_li 城郊游历 end")

def daily_cai_shen_miao_like(device = local_device, sleep_time = 1):
    # usual sleep_time 0.6 +
    from resources_1080_1920.cheng_jiao.cheng_jiao_data import cai_shen_miao
    print("daily_cai_shen_miao_like begin")
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    # enter miao
    cai_shen = cai_shen_miao["pos"]
    click_once(cai_shen[0], cai_shen[1], device, sleep_time=sleep_time)
    ex = resources_1080_1920.general.general_pos["exit"]
    cai_shen_pu = cai_shen_miao["cai_shen_pu"]
    cai_shen_like = cai_shen_miao["cai_shen_like"]
    big_like = cai_shen_miao["like"]
    # 点大赞
    click_once(big_like[0], big_like[1], device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time/2, times = 3)
    
    # 点赞上方的庙宇
    for pos in cai_shen_miao["ups"]:
        click_once(pos[0], pos[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_pu[0], cai_shen_pu[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_like[0], cai_shen_like[1], device=device, sleep_time=sleep_time*2)
        click_painless(device=device, sleep_time=sleep_time/2, times = 3)
        click_once(ex[0], ex[1], device=device, sleep_time=sleep_time*2)
    
    # 点赞下方的庙宇
    move_to_end(bottom=1, sleep_time=0.5)
    for pos in cai_shen_miao["lows"]:
        click_once(pos[0], pos[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_pu[0], cai_shen_pu[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_like[0], cai_shen_like[1], device=device, sleep_time=sleep_time*2)
        click_painless(device=device, sleep_time=sleep_time/2, times = 3)
        click_once(ex[0], ex[1], device=device, sleep_time=sleep_time*2)
    
    enter_home(device=device, sleep_time=sleep_time)
    print("daily_cai_shen_miao_like ends")

def daily_ling_qu_yu_gan(device = local_device, sleep_time = 1):
    if debugging:
        print(f"daily_ling_qu_yu_gan 领取鱼竿")
    # 领取鱼竿
    # 经常领取不到，多做几次
    from resources_1080_1920.cheng_jiao.cheng_jiao_data import zhuang_yuan
    
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    x, y = zhuang_yuan["entry"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    move_to_end(left=1, sleep_time=sleep_time)
    move_x, move_y = zhuang_yuan["drag_to_yu_gan"]
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    
    yu_x, yu_y = zhuang_yuan["yu_gan"]
    for _ in range(2):
        for i in range(-5, 5, 1):
            # often has x axis random bias
            clicks(yu_x + i * 20, yu_y, device=device, sleep_time=sleep_time*0.1, times=4)
        click_painless(device=device, sleep_time=sleep_time, times=2)
    x, y = zhuang_yuan["shou_huo"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = zhuang_yuan["shou_huo_confirm"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print(f"daily_ling_qu_yu_gan 领取鱼竿 end")

def daily_xing_shan(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_xing_shan begin")
    enter_home  (device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*2)
    mv_x, mv_y = resources_1080_1920.cheng_jiao.cheng_jiao_data.xing_shan["drag"]
    drag_and_move(mv_x, mv_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    entry_x, entry_y = resources_1080_1920.cheng_jiao.cheng_jiao_data.xing_shan["entry"]
    click_once(entry_x, entry_y, device=device, sleep_time=sleep_time*3)
    
    do = resources_1080_1920.cheng_jiao.cheng_jiao_data.xing_shan["do"]
    one_click = resources_1080_1920.cheng_jiao.cheng_jiao_data.xing_shan["one_click"]
    for _ in range(2):
        click_painless(device=device, sleep_time=sleep_time, times=2)
        click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time/3)
        for _ in range(19):
            click_once(do[0], do[1], device=device, sleep_time=sleep_time)
            click_once(do[0], do[1], device=device, sleep_time=sleep_time)
            click_painless(device=device, sleep_time=sleep_time, times=2)
        
    confirm = resources_1080_1920.cheng_jiao.cheng_jiao_data.xing_shan["confirm"]
    for _ in range(4):
        click_once(do[0], do[1], device=device, sleep_time=sleep_time)
        click_once(confirm[0], confirm[1], device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times=2)
        click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time/3)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    
    enter_home(device=device, sleep_time=sleep_time)   
    if debugging:
        print("daily_xing_shan end")
xing_shan = {
    "entry" : (950, 670),
    "do" : (920, 1520),
    "click_times": 20,
    "period": 2,
    "confirm": (720, 1050),
    "drag": (-1000, 0),
}

def shou_lie(device = local_device, sleep_time = 1):
    if debugging:
        print(f"shou_lie begin")
    enter_home(device=device, sleep_time=sleep_time)
    ex, ey = resources_1080_1920.general.general_pos["exit"]
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    # move to shou_lie
    move_x, move_y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["drag_to_shou_lie"]
    drag_and_move(move_x=move_x, move_y=move_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["entry"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # 进入 狩猎 page
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["enter"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["auto"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    # 点击自动
    period = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["period"]
    for _ in range(50):
        click_painless(device=device, sleep_time=period)
    
    x_help, y_help = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["shang_hui_help"]
    x2_help, y2_help = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["shang_hui_help_page"]
    x0, y0 = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["help_00"]
    dx, dy = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["help_delta"]
    
    x_con, y_con = resources_1080_1920.cheng_jiao.cheng_jiao_data.shou_lie["confirm"]
    
    for index in range(4, -1, -1): # 0 -> 4
        y_t = index // 3
        x_t = index % 3
        x, y = x_t * dx * x_t + x0, dy * y_t + y0
        click_once(x_help, y_help, device=device, sleep_time=sleep_time)
        click_once(x2_help, y2_help, device=device, sleep_time=sleep_time)
        click_once(x_con, y_con, device=device, sleep_time=sleep_time)
        click_once(x_t, y_t, device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=period, times = 2)
    
    click_once(ex, ey, device=device, sleep_time=sleep_time, times = 2)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print(f"shou_lie end")

def ri_chang_chuang_dang(device = local_device, sleep_time = 1):
    if debugging:
        print(f"ri_chang_chuang_dang begin")
    from resources_1080_1920.chuang_dang.chuang_dang_data import guan_ka
    from resources_1080_1920.general import general_pos
    ex, ey = general_pos["exit"]
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
        print(f"    ri_chang_chuang_dang end")
    
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
