import os
import subprocess
import re
import time
import resources_1080_1920.home.home_data

# just for my debug
local_device = "localhost:5555"
# my debug part end

def click_once(x = 0, y = 0, device = local_device, sleep_time = None):
    if device == None:
        adb_command = ["adb", "shell", "input", "tap", str(x), str(y)]
    else:
        adb_command = ["adb", "-s" , device, "shell", "input", "tap", str(x), str(y)]
        
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)
    if sleep_time != None:
        time.sleep(sleep_time)

def click_painless(device = local_device, sleep_time = None):
    click_once(x=500, y =5, device=device, sleep_time=sleep_time)

def click_qian_zhuang_from_home(times = 100, sleep_time = 0.1):
    x, y = resources_1080_1920.home_bar.home_data.home_bar["home_shang-pu"]
    subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
    time.sleep(5)
    x,y = 300, 666
    for _ in range(times):
        subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
        time.sleep(sleep_time)


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

def remove_local_file(img_file_path="test.png"):
    if os.path.exists(img_file_path):
        os.remove(img_file_path)
    else:
        pass
start = time.time()
remove_local_file()
end = time.time()
print(end-start)

def need_test():
    obtain_screenshot()

def passed_test():
    click_qian_zhuang_from_home(100)
    
    
    click_union_basic_constrcut()

    test_move_screenshot()
