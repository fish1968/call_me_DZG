import os
import socket
import subprocess
import time
import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
from ADB_project.functions.local_data import local_device, debugging, adb_debugging, game_package_name, json_file_path
import ADB_project.data.constant as constant

########## ADB Command ################
def click_once(x:int = 0, y:int = 0, device:str = local_device, sleep_time = None):
    if device == None:
        adb_command = ["adb", "shell", "input", "tap", str(x), str(y)]
    else:
        adb_command = ["adb", "-s" , device, "shell", "input", "tap", str(x), str(y)]
        
    subprocess.run(adb_command)
    if sleep_time != None:
        time.sleep(sleep_time)

def clicks(x: int = 0, y: int = 0, device = local_device, sleep_time = 0.1, times = 1):
    for _ in range(times):
        click_once(x=x, y=y, device=device, sleep_time=sleep_time)

def drag_and_move(
        move_x: int=0, 
        move_y: int=0, 
        start_x: int=500, 
        start_y: int=1000, 
        device = local_device, 
        duration_ms: int = 100
        ):
    
    adb_command = ['adb',"-s", device, 'shell', 'input', 'swipe', str(start_x), str(start_y), str(start_x+move_x), str(start_y+move_y), str(int(duration_ms))]
    subprocess.run(adb_command)
    time.sleep(int(duration_ms/500)) # is this needed?
    if adb_debugging:
        print(adb_command)

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

def move_to_left(device = local_device):
    move_to_end(left = 1, sleep_time=0.5,device = device)

def move_to_right(device = local_device):
    move_to_end(right= 1, sleep_time=0.5,device = device)

def move_to_top(device = local_device):
    move_to_end( top = 1,sleep_time=0.5,device = device)

def move_to_bottom(device = local_device):
    move_to_end(bottom= 1, sleep_time=0.5,device = device)

########## ADB Screenshot ################
def obtain_screenshot(img_name = constant.TEST_IMG,local_dir=r"./imgs",device = local_device):
    if debugging:
        print(f"obtain_screenshot: img_name = {img_name}")
    # ref: https://blog.csdn.net/fxdaniel/article/details/45846333
    # ref2: https://www.cnblogs.com/shaosks/p/14043177.html
    adb_screenshot = ["adb", "-s", device, "shell", "screencap -p", constant.ANDROID_BASE_DIR + img_name]
    subprocess.run(adb_screenshot)
    adb_pass_image = ["adb", "-s", device, "pull", constant.ANDROID_BASE_DIR + img_name, local_dir+r"/"+img_name]
    subprocess.run(adb_pass_image)
    # remove image from the android
    adb_rm_img = ["adb", "-s", device, "shell", "rm", "/sdcard/"+img_name]
    subprocess.run(adb_rm_img)
    
    if debugging:
        print(f"obtain_screenshot: img_name = {img_name} end")

def test_move_screenshot(img_name = "test.png", device = local_device, sleep_time = None):
    if debugging:
        print(f"test_move_screenshot: img_name = {img_name} begin")
    adb_command = ["adb", "-s", device, "pull", "/sdcard/"+img_name, "./"+img_name]
    subprocess.run(adb_command)
    # time.sleep(1)
    if debugging:
        print(f"test_move_screenshot: img_name = {img_name} end")

def remove_local_file(img_file_path="test.png"):
    if debugging:
        print(f"remove_local_file img_path = {img_file_path} begin")
    if os.path.exists(img_file_path):
        os.remove(img_file_path)
    if debugging:
        print(f"remove_local_file img_path = {img_file_path} end")

########## ADB fundamental ################
@future_care
def find_available_port(start_port, end_port):
    # Not working as expected, this logic is problematic
    # find available port for adb
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return port
            except OSError:
                continue

def start_adb_server():
    subprocess.run(["adb", "start-server"])

def is_adb_server_on():
    # obtain whether adb has been ON
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0 and 'List of devices attached' in result.stdout

def is_device_connected(device = local_device):
    result = subprocess.run(['adb', 'connect', device], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and "already" in result.stdout:
        print(f"adb has connected to {device}")
        return True
    else:
        print(f"adb failed connect to {device}")
        return False

def start_adb():
    while is_adb_server_on() == False:
        start_adb_server()
    return True

@future_care
def adb_start_activity(device = local_device, game_package = game_package_name):
    res = subprocess.run(["adb", "-s", device,"shell", "am", "start", game_package])
    if res.returncode == 0:
        print(f"Enter game {game_package} successfully")
        return True
    else:
        print("Failed to enter Game!!!!")
        return False

@future_care
def adb_is_game_the_current_activity(device=local_device, expected_package= game_package_name):
    command = f"adb -s {device} shell dumpsys activity top | findstr ACTIVITY"
    results = subprocess.getoutput(command)
    last_result = results.splitlines()[-1]
    if expected_package not in last_result:
        return False
    else:
        return True
@future_care
def adb_obtain_all_activities(device=local_device):
    command = f"adb -s {device} shell dumpsys activity top | findstr ACTIVITY"
    results = subprocess.getoutput(command)
    return results
@future_care
def adb_obtain_front_activity(device=local_device):
    result = adb_obtain_all_activities(device = device)[-1]
    return result


def start_apk_package(device= local_device, apk_package = "com.zx.a2_quickfox"):
    print("Starting APK package...")
    command = f"adb -s {device} shell monkey -p {apk_package} 1"
    subprocess.run(command, shell=True)
    print(f"Started and processed {apk_package}")

if __name__ == "__main__":
    is_device_connected()
    print("- "*10)
    is_device_connected(device="localhost:5555")
    # Usage
    print("- "*10)
    if is_adb_server_on():
        print("ADB is connected.")
    else:
        print("ADB is not connected.")

