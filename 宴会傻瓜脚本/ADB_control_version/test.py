import subprocess
import re
import time
import resources_1080_1920.home.home_data

def click_once(x = 0, y = 0):
    
    adb_command = ["adb", "shell", "input", "tap", str(x), str(y)]
    subprocess.Popen(adb_command, stdout=subprocess.PIPE)


def click_qian_zhuang_from_home(times = 100):
    x, y = resources_1080_1920.home_bar.home_data.home_bar["home_shang-pu"]
    subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
    time.sleep(5)
    x,y = 300, 666
    for _ in range(times):
        subprocess.Popen(["adb", "shell", "input", "tap", str(x), str(y)])
        time.sleep(0.1)

def obtain_screenshot(x0 = 0, y0 = 0, x1 = 1080, y1 = 1920):
    # yet implemented
    # ref: https://blog.csdn.net/fxdaniel/article/details/45846333
    # ref2: https://www.cnblogs.com/shaosks/p/14043177.html
    pass

start = time.time()
click_qian_zhuang_from_home(100)

end = time.time()
print(end-start)
