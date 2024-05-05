from PIL import Image ,ImageGrab
import os
import win32api
import win32con
import win32gui
import time
from ctypes import *
import cv2
import sys
import imageio
import numpy as np
import datetime
import logging

from local_data import 小程序启动路径
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

fixed_data = {
    # 包括 header 的 y 位置 ！！！ 一定不要乱
    "full_screen": (786, 1439),
    "header": (786, 44),
    "home-entry-kua-fu": (201, 262),
    "home-home": (80, 1380),
    "home-stores": (200, 1380),
    "home-qian-zhuang": (220, 530),
    
    "text_entry": (440, 1290),
    "text-input": (400, 1268),
    "text-send": (680, 1269),
    
    "general_exit": (71, 71),
    
    "home-cheng_jiao": (586, 1372),
    
    "home-xiao-yu": (758, 830),
    "xiao-yu-execute": (437, 1035),
    "xiao-yu-execute-over": (400, 1150),
    
    "painless-point": (400, 80), #可以随便点，无所谓
    
    "yanhui-box": (680, 240),
    "yanhui-open_all_boxes": (400, 1138),
    "yanhui-next": (80, 1295),
    "yanhui-in": (590, 1275), # click to enter yanhui by invitation or in the page
    "yanhui-exit": (40, 80),
    
    "bai-fu_entry": (700, 740),
    "bai-fu_fu-yan": (400, 1350),
    "bai-fu_exit": (730, 210),
    # 财神庙找赞点击
    "cheng_jiao-cai_shen_miao": (360, 600),
    "cheng_jiao-cai_shen_miao-bai_fang": (400, 1250), # not used
    "page_full_screen": (765, 1360),
    
    # 启动
    "kei-dong_li-xian-jiang-li" : (520, 1050),
    "kei-dong_event-page-dou-luo": (730, 220),
    "kei-dong_event-page-xian-shi": (730, 230),
    "kei-dong_go-to-event": (626, 1150),
    "kei-dong_brightness-detect-pos0": (400, 100),
    "kei-dong_brightness-detect-pos1": (400, 700),
        # "home-entry-kua-fu": (203, 259),
        # "home-home": (80, 1380),
        # "home-stores": (200, 1380),
        # "home-qian-zhuang": (220, 530),
        # "yanhui-box": (680, 200),
        # "yanhui-open_all_boxes": (400, 1090),
        # "yanhui-next": (80, 1233),
        # "yanhui-in": (590, 1200), # click to enter yanhui from invitation or in the page
        # "yanhui-exit": (40, 33),
        # "bai-fu_entry": (700, 680),
        # "bai-fu_fu-yan": (400, 1300),
        # "bai-fu_exit": (725, 165),
        # "text_entry": (480, 1230),
        # "text-input": (430, 1210),
        # "text-send": (680, 1210),
        # "painless-point": (350, 80), #可以随便点，无所谓
        # "home-xiao-yu": (750, 830),
        # "xiao-yu-execute": (450, 980),
        # "xiao-yu-execute-over": (400, 1100),
        # # 财神庙找赞点击
        # "home-cheng_jiao": (600, 1325),
        # "cheng_jiao-cai_shen_miao": (370, 570),
        # "cheng_jiao-cai_shen_miao-bai_fang": (400, 1250),
        # "page_full_screen": (765, 1360),
        
        # "general_exit": (40, 35)

}

LONG_TIME = 60*5
MID_TIME = 10
SHT_TIME = 1
EX_SHT_TIME = 0.1



command_list = ["qian_zhuang", 
        "xiao_yu", 
        "home_enter_kua_fu", 
        "do_huodong_enter_yanhuizhengba", 
        "do_yan_hui_page_enter_bai_fu_and_fu_yan",
        "do_exit_to_the_end", 
        "do_click_cai_shen", 
        "do_in_cai_shen_miao_click_points", 
        "go_home_to_cai_shen_miao", 
        "do_from_home_to_do_all_in_cai_shen_miao",
        "do_from_home_do_dian_zan",
        "do_from_home_do_shang_zhan",
        ]

class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]
 
def get_mouse_point():
    po = POINT()
    windll.user32.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
 
def mouse_click(x=None,y=None, to_origin = True, debug = False):
    cur_x, cur_y = get_mouse_point()
    if debug:
        print(f"cursor before move is at {cur_x, cur_y}")
    if not (x is None) and not (y is None):
        mouse_move(x,y)
    else:
        return
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    if to_origin:
        if debug:
            print(f"move back to {cur_x, cur_y}")
        mouse_move(cur_x, cur_y)
    time.sleep(EX_SHT_TIME)

def mouse_dclick(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(-1.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
def mouse_move(x,y):
    windll.user32.SetCursorPos(x, y)

def mouse_roll_up(times, rev = False, wait_time = EX_SHT_TIME, x0 = None, y0 = None):
    # roll up / down(rev = True) for times and wait wait_time for each time
    if x0 == None and y0 == None:
        x0, y0 = get_da_zhang_gui_pos()
    cur_x, cur_y = get_mouse_point()
    mouse_move(x0+400, y0 + 200) # 光标需要在画面内才能 执行滚动成功
    time.sleep(wait_time)
    for _ in range(times):
        if rev == False:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1, 0)
        time.sleep(wait_time)
    mouse_move(cur_x, cur_y)
def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(-1.01)

class ImageTest:
    commands = []
    def __init__(self):
        self.mouse = mouse_click()
        self.keyboard =key_input()
    #定义APP启动
    def START_APP(self, cmd):
        os.system('START /b %s' % cmd)
        time.sleep(SHT_TIME)
        print('*************start successfully!**************')
    
    #单击图片
    def on_click(self,target):
            x,y = self.match.find_img(target)
            self.mouse_click(x,y)
            print('在[%d,%d]位置单击1次'%(x,y,target))
    
    def starttest(self, commands=[]):
        # start 小程序，并等待合理时间
        print("BEGIN")
        self.START_APP(小程序启动路径)
        time.sleep(MID_TIME)
        ImageTest.commands = commands
        print(ImageTest.commands)
        
        # one time event
        while(len(ImageTest.commands) != 0):
            command = ImageTest.commands.pop(0) # retrive the front event idx
            print("Current command is ", command)
            test_command = command_list[command]
            do_based_on_task_command(test_command)
            time.sleep(SHT_TIME)
        
        # inf looping
        process_pre_defined_event_with_interrupt_event()

def click_picture(picture, target, left = 0, right = 0, top = 764, bottom = 1404, acc_threshold = 0.8):
    '''单击图片'''
    base_path = os.path.join(picture)
    im_screen = ImageGrab.grab().crop((left, top, right, bottom))
    source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
    # im_screen.save(r'Test.png')
    # source = cv2.imread(r'Test.png')
    target = cv2.imread(base_path)
    results = cv2.minMaxLoc(cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED))
    acc = results[1]  # 测试两幅图像精确度
    pic_pos = results[3]
    x = int(pic_pos[0]) + int(target.shape[1] / 2) + left
    y = int(pic_pos[1]) + int(target.shape[0] / 2) + top
    if acc >= acc_threshold:
        # print(picture)
        print("执行点击成功：",picture,"，坐标：(",x,",",y,")  accuracy = ", f"{acc:1.4f}")
        if "fu" in picture:
            logging.info(f"当前时间是 {0}，现在识别到了图片1，准确率是 {acc:1.4f}".format(datetime.datetime.now()))
            # 多点击几次
            for _ in range(3):
                mouse_click(x,y)
                time.sleep(SHT_TIME)
        elif "exit" in picture or "7_x" in picture:
            while (acc>acc_threshold):
                mouse_click(x,y)
                im_screen = ImageGrab.grab().crop((left, top, right, bottom))
                source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
                results = cv2.minMaxLoc(cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED))
                acc = results[1]
                x,y = results[3][0] + left, results[3][1] + top
                time.sleep(SHT_TIME)
        else:
            mouse_click(x,y)
            
        time.sleep(EX_SHT_TIME)
    else:
        print(f"未识别出目标 {picture}, accuracy = {acc:1.4f}", datetime.datetime.now())
        if "kua" in picture:
            x_dx = x + 200
            y_dy = y + 256
            mouse_click(x_dx, y_dy)
            time.sleep(SHT_TIME * 5) # waits longer for internet delay

def click_pictures(pictures=[], targets=[], accuracy_threshold = 0.75, x0=0, y0=0,window_length = 764, window_height = 1404):
    if len(targets) == 0:
        for picture in pictures:
            base_path = os.path.join(picture)
            template = cv2.imread(base_path)
            targets.append(template)
            logging.debug("reading templates")
    target_index = 0
    # Define the coordinates of the region of interest
    left = x0  # X-coordinate of the left edge of the region
    top = y0  # Y-coordinate of the top edge of the region
    right = x0 + window_length  # X-coordinate of the right edge of the region
    bottom = y0 + window_height  # Y-coordinate of the bottom edge of the region
    ext_index = 5
    for picture in pictures:
        '''单击图片'''
        if "exit" in picture:
            ext_index = (ext_index+1)% 10
            if ext_index == 0:
                click_picture(picture = picture, target = targets[target_index], left = left, right = right, top = top, bottom = bottom, acc_threshold=0.75)
        else:
            click_picture(picture = picture, target = targets[target_index], left = left, right = right, top = top, bottom = bottom, acc_threshold=0.75)
        target_index += 1

# 获取 大掌柜 小程序的左上角位置
def get_da_zhang_gui_pos(da_zhang_gui_img_path = "da_zhang_gui_wx.jpg", window_length = 764,window_height = 1404):
    s = 0
    while (s < 0.7):
        im_screen = ImageGrab.grab()  # 保存
        im_screen.save(r'./temp.png')
        source = cv2.imread(r'./temp.png')
        template = cv2.imread(da_zhang_gui_img_path)
        result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
        pos_start = cv2.minMaxLoc(result)[3]
        s = cv2.minMaxLoc(result)[1]  # 测试两幅图像精确度
        x = int(pos_start[0]) + int(template.shape[1] / 2)
        y = int(pos_start[1])
        time.sleep(SHT_TIME)
    x = int(x-window_length/2)
    print("include-header position",x,y,s)
    return (x, y)
    
def do_公屏粘贴发言(type=True):
    x0,y0 = get_da_zhang_gui_pos()
    # 骗赞
    # go to home
    x,y = fixed_data["home-home"]
    mouse_click(x + x0, y + y0)
    time.sleep(SHT_TIME)
    # 点击 entry for text
    x,y = fixed_data["text_entry"]
    mouse_click(x + x0, y + y0)
    time.sleep(SHT_TIME)
    # 激活文本输入
    x,y = fixed_data["text-input"]
    mouse_click(x + x0, y + y0)
    time.sleep(SHT_TIME)
    if type:
        # Delay between key presses (in seconds)
        # Press and release 'r' key
        win32api.keybd_event(ord('R'), 0, 0, 0)
        win32api.keybd_event(ord('R'), 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(EX_SHT_TIME)

        # Press and release 'o' key
        win32api.keybd_event(ord('O'), 0, 0, 0)
        win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(EX_SHT_TIME)

        # Press and release 'b' key
        win32api.keybd_event(ord('B'), 0, 0, 0)
        win32api.keybd_event(ord('B'), 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(EX_SHT_TIME)

        # Press and release 'o' key
        win32api.keybd_event(ord('O'), 0, 0, 0)
        win32api.keybd_event(ord('O'), 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(EX_SHT_TIME)

        # Press and release 't' key
        win32api.keybd_event(ord('T'), 0, 0, 0)
        win32api.keybd_event(ord('T'), 0, win32con.KEYEVENTF_KEYUP, 0)
        time.sleep(EX_SHT_TIME)
        # # Press and release '?' key
        # win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)  # Press Shift key
        # win32api.keybd_event(ord('?')-32, 0, 0, 0)  # Press '?' key
        # time.sleep(key_delay)
        # win32api.keybd_event(ord('?')-32, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release '?' key
        # win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)  # Release Shift key
        # Press Enter key
        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        # Release Enter key
        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
    else:
        # Press Ctrl key
        win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
        # Press V key
        win32api.keybd_event(0x56, 0, 0, 0)
        time.sleep(SHT_TIME)
        # Release V key
        win32api.keybd_event(0x56, 0, win32con.KEYEVENTF_KEYUP, 0)
        # Release Ctrl key
        win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
        # Press Enter key
        win32api.keybd_event(win32con.VK_RETURN, 0, 0, 0)
        # Release Enter key
        win32api.keybd_event(win32con.VK_RETURN, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(SHT_TIME)
    # 发送
    x, y = fixed_data["text-send"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 回到主页
    x, y = fixed_data["home-home"]
    for _ in range(2):
        mouse_click(x+x0, y+y0)
        time.sleep(EX_SHT_TIME)
    
# 主页 -> 主页 府邸
def do_enter_home(x0 = 0, y0 = 0):
    # 点击府邸
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["home-home"]
    mouse_click(x+x0, y+y0)
# 主页 -> 商城
def do_enter_stores(x0 = 0, y0 = 0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["home-stores"]
    mouse_click(x+x0, y+y0)
# 商城 点击钱庄
def do_at_stores_click_qian_zhuang(x0 = 0, y0 = 0, times = 20):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["home-qian-zhuang"]
    for _ in range(times):
        mouse_click(x+x0, y+y0)
        # time.sleep(EX_SHT_TIME)
# 小玉执行
def do_xiao_yu(x0=0,y0 = 0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    # 在主页
    do_enter_home(x0, y0)
    time.sleep(SHT_TIME)
    # 点击小玉
    print(f"x0 ,y0 = {x0, y0}")
    x,y = fixed_data["home-xiao-yu"]
    print(f"home xiaoyu: x ,y = {x, y}")
    mouse_click(x+x0, y+y0)
    time.sleep(MID_TIME) # 需要等待长一点
    # 点击执行
    x,y = fixed_data["xiao-yu-execute"]
    mouse_click(x+x0, y+y0)
    for _ in range(20):
        do_painless_click(x0,y0)
        time.sleep(SHT_TIME)
    # 点击确定
    x,y = fixed_data["xiao-yu-execute-over"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 退出界面
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
# 主页 -> 跨服
def do_home_enter_kua_fu(x0=0, y0=0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["home-entry-kua-fu"]
    print(x,y)
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
# 跨服 -> 宴会争霸
def do_kua_fu_enter_yanhuizhengba(x0=0, y0= 0, yanhui_picture_path = "img_templates/10_yanhui_zhengba.jpg",acc_threshold = 0.7):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    target_path = os.path.join(yanhui_picture_path)
    print(target_path)
    target = cv2.imread(target_path)
    acc = 0
    pic_pos = (0,0)
    while (acc < acc_threshold):
        im_screen = ImageGrab.grab().crop((x0,y0,x0+fixed_data["full_screen"][0],y0+fixed_data["full_screen"][1]))
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        results = cv2.minMaxLoc(cv2.matchTemplate(source,target,cv2.TM_CCORR_NORMED))
        acc = results[1]
        pic_pos = results[3]
    x,y = pic_pos
    x += int(target.shape[1] / 2)
    y += int(target.shape[0] / 2)
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME*2)
# 宴会争霸 -> 执行百宴 -> 跨服争霸
def do_yan_hui_page_enter_bai_fu_and_fu_yan(x0=0, y0=0):
    # 宴会争霸界面 开始 到结束
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["bai-fu_entry"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["bai-fu_fu-yan"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["bai-fu_exit"]
    mouse_click(x+x0, y+y0)
# 点左上角 退出，直到不能再退出，或者超过最高次数
def do_exit_to_the_end(x0 = 0, y0 = 0, exit_picture_path = "img_templates/13_exit.jpg",acc_threshold = 0.8, round = 4):
    # 一直退出，预期到主页
    # 由于图片比较小，很容易错误识别，因此精确度权重提高
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["yanhui-exit"]
    acc = 1
    round = round
    target_path = os.path.join(exit_picture_path)
    target = cv2.imread(target_path)
    while (acc > acc_threshold):
        im_screen = ImageGrab.grab().crop((x0,y0,x0+fixed_data["full_screen"][0],y0+fixed_data["yanhui-exit"][1]*5))
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        results = cv2.minMaxLoc(cv2.matchTemplate(source,target,cv2.TM_CCORR_NORMED))
        acc = results[1]
        # pic_pos = results[3]
        # x,y = pic_pos
        x,y = fixed_data["general_exit"]
        if acc < acc_threshold:
            break
        mouse_click(x+x0, y+y0)
        time.sleep(MID_TIME)
        print(f"Exit position found as {(x+x0, y+y0)} with acc {acc:1.4f}")
        round -= 1
        if round == 0:
            print("Too many rounds, wrongly detected")
            break
        # x,y = pic_pos # x y unchanged 
    # meaningless point
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)
    time.sleep(EX_SHT_TIME)
    do_enter_home(x0 = x0, y0 = y0) #点一下 home
    time.sleep(EX_SHT_TIME)

def do_painless_click(x0 = 0, y0 = 0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)

def do_click_cai_shen(x0=0, y0=0):
    do_painless_click(x0, y0)

def do_click_all_templates(x0 = 0, y0 = 0, template_pic_path = "img_templates/red_point.png",acc_threshold = 0.8, round = 10, delay_time = MID_TIME):
    # 一直点击 target (对于小图标，非常失败)
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    x,y = fixed_data["yanhui-exit"]
    acc = 1
    target_path = os.path.join(template_pic_path)
    target = cv2.imread(target_path)
    while (round > 0):
        im_screen = ImageGrab.grab().crop((x0,y0,x0+fixed_data["page_full_screen"][0],y0+fixed_data["page_full_screen"][1]))
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        results = cv2.minMaxLoc(cv2.matchTemplate(source,target,cv2.TM_CCORR_NORMED))
        acc = results[1]
        pic_pos = results[3]
        x, y = pic_pos
        print(f"Target position found as {pic_pos} with acc {acc:1.4f}")
        round -= 1
        if acc > acc_threshold:
            mouse_click(x+x0, y+y0)
        else:
            break
        if round == 0:
            print("Too many rounds, wrongly detected")
            break
        time.sleep(delay_time)
        # x,y = pic_pos # x y unchanged 
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)
    time.sleep(EX_SHT_TIME)
    do_enter_home(x0 = x0, y0 = y0) #点一下 home
    time.sleep(EX_SHT_TIME)

def do_in_cai_shen_miao_click_points(x0=0, y0 = 0, red_imag_path = "img_templates/red_point.png"):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    # inside cai shen miao page, do one by one carelessly
    # all without header counted
    cai_shen_exit =     (730, 210)
    cai_shen_bu_pos =   (90, 1200)
    dian_zan_pos =      (400, 1150)

    y_move = 1100
    
    huge_like = (680, 1220)
    qi_lin = (414, 432)
    xuan_wu = (617, 345)
    qing_long = (667, 582)
    cai_shen_ye_1 = (407, 766)
    cai_shen_ye_2 = (189, 1107)
    cai_shen_ye_3 = (415, 1095)
    cai_shen_ye_4 = (627, 1058)
    cai_shen_ye_top2 = (414, 934)
    
    cai_shen_low_1 = (260,320)
    cai_shen_low_2 = (550,320)
    cai_shen_low_31 = (80,500)
    cai_shen_low_32 = (240,500)
    cai_shen_low_33 = (565,500)
    cai_shen_low_34 = (716,500)
    cai_shen_low_35 = (400,580)
    cai_shen_low_41 = (151,820)
    cai_shen_low_42 = (399,820)
    cai_shen_low_43 = (639,820)
    cai_shen_low_51 = (161,1010)
    cai_shen_low_52 = (394,1010)
    cai_shen_low_53 = (629,1010)

    miao_list_up = [    
        xuan_wu, 
        qi_lin,
        qing_long,
        cai_shen_ye_1,
        cai_shen_ye_2,
        cai_shen_ye_3,
        cai_shen_ye_4,
        cai_shen_ye_top2,
    ]
    miao_list_down = [
        cai_shen_low_1,
        cai_shen_low_2,
        cai_shen_low_31,
        cai_shen_low_32,
        cai_shen_low_33,
        cai_shen_low_34,
        cai_shen_low_35,
        cai_shen_low_41,
        cai_shen_low_42,
        cai_shen_low_43,
        cai_shen_low_51,
        cai_shen_low_52,
        cai_shen_low_53
    ]
    # 拖拽 移动
    def drag_and_move_up(y_move=y_move):
        # Simulate mouse down
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)

        # Move the mouse up for 1000 units in the y-axis
        current_position = win32api.GetCursorPos()
        new_position = (current_position[0], current_position[1] -y_move)
        win32api.SetCursorPos(new_position)
        time.sleep(SHT_TIME)
        # Simulate mouse up
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)

        # Wait for a short period of time
        time.sleep(SHT_TIME)  # Adjust the sleep duration as needed


    # x0, y0 include-header position (NO header)
    def click_one_miao(x,y,x0,y0, count_header = True):
        print(f"x,y and x0,y0 = {x,y, x0, y0}")
        if count_header == True:
            y_off = fixed_data["header"][1]
        else:
            y_off = 0
        # 点击财神庙
        mouse_click(x+x0,y+y0+y_off, to_origin=True)
        time.sleep(SHT_TIME*2)
        # 点击财神簿
        mouse_click(x0+cai_shen_bu_pos[0],y0+cai_shen_bu_pos[1]+y_off, to_origin=True)
        time.sleep(SHT_TIME*2)
        # 点击点赞
        mouse_click(x0+dian_zan_pos[0],y0+dian_zan_pos[1]+y_off, to_origin=True)
        time.sleep(SHT_TIME*2)
        # exit
        for _ in range(4): # 需要点赞 与 没有点赞的情况各需要 1-2次
            do_painless_click(x0=x0, y0=y0)
            time.sleep(EX_SHT_TIME)
        # time.sleep(SHT_TIME)
        # mouse_click(x0 + cai_shen_exit[0], y0+cai_shen_exit[1]+y_off)
        time.sleep(SHT_TIME)
        print(f"x0,y0 = {x0, y0}")
        print(x0+fixed_data['general_exit'][0], y0 + fixed_data['general_exit'][1])
        mouse_click(x0+fixed_data["general_exit"][0], y0+fixed_data["general_exit"][1], to_origin=False)
        time.sleep(SHT_TIME)
    # 大点赞
    x, y = huge_like
    mouse_click(x+x0, y+y0)
    for _ in range(4):
        do_painless_click(x0, y0)
        time.sleep(SHT_TIME)
    # 上层庙宇点赞
    for miao_pos in miao_list_up:
        print(f"CLICK ONE MIAO x0, y0 = {x0, y0}")
        click_one_miao(miao_pos[0], miao_pos[1], x0, y0)

    time.sleep(SHT_TIME)
    # move mouse to a lower position on the page (for later dragging event)
    # mouse_move(x0+cai_shen_ye_4[0], y0+cai_shen_ye_4[1])
    # time.sleep(SHT_TIME)
    do_painless_click(x0, y0)
    time.sleep(SHT_TIME)
    print("drag begin")
    logging.info("drag starts")
    mouse_roll_up(20, rev=True, wait_time=EX_SHT_TIME)
    # drag_and_move_up()
    logging.info("drag finished")
    print("drag end")
    
    for miao_pos in miao_list_down:
        click_one_miao(miao_pos[0], miao_pos[1], x0, y0)

def go_home_to_cai_shen_miao(x0 =0 , y0 =0 ):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    pos = fixed_data["home-cheng_jiao"]
    x,y = pos
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    mouse_roll_up(20, rev = False, wait_time = EX_SHT_TIME)
    time.sleep(SHT_TIME)
    x,y = fixed_data["cheng_jiao-cai_shen_miao"]
    mouse_click(x+x0, y+y0)

# 从主页进入财神庙，并依次点赞
def do_from_home_to_do_all_in_cai_shen_miao(x0=0, y0=0, red_imag_path="img_templates/red_point.png"):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    # 从 home 进入财神庙
    go_home_to_cai_shen_miao(x0, y0)
    time.sleep(SHT_TIME)
    time.sleep(SHT_TIME)
    # 再财神庙进行点击
    do_in_cai_shen_miao_click_points(x0,y0,red_imag_path)
    # 返回 home
    time.sleep(SHT_TIME)
    do_enter_home(x0, y0)

def do_after_invited(x0=0, y0 = 0):
    # 在收到邀请后 进行如宴会，并退出到主页
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    for _ in range(10): # do 10 times to secure all if any
        for _ in range(3):
            x,y = fixed_data["yanhui-in"]
            print(f"x0 y0 at {(x0,y0)}")
            print(f"Invite at {(x+x0,y+y0)}")
            mouse_click(x+x0, y+y0)
            time.sleep(SHT_TIME)
        for _ in range(3): # odd number is safer than even
            x,y = fixed_data["yanhui-box"]
            mouse_click(x+x0, y+y0)
            time.sleep(SHT_TIME)
        x,y = fixed_data["yanhui-open_all_boxes"]
        mouse_click(x+x0, y+y0)
        time.sleep(SHT_TIME)
        do_painless_click(x0, y0) # exit from openning boxes
        time.sleep(SHT_TIME)
        x,y = fixed_data["yanhui-next"]
        mouse_click(x+x0, y+y0)
        time.sleep(SHT_TIME)
    do_exit_to_the_end(x0, y0)

def do_from_home_do_dian_zan(x0 = 0, y0 = 0, debug = False):
    fixed_data['cheng-jiao_pai-hang-bang_yi-jian-dian-zan'] = (680, 1380)
    fixed_data['cheng-jiao_pai-hang-bang'] = (150, 970)
    fixed_data['cheng-jiao_pai-hang-bang_enter-one'] = (400, 400)
    fixed_data['cheng-jiao_pai-hang-bang_enter-kua-fu'] = (350,150)
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    # 进入城郊
    x, y = fixed_data['home-cheng_jiao']
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 进入排行榜页面
    x, y = fixed_data['cheng-jiao_pai-hang-bang']
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 进入可点赞页面
    x, y = fixed_data["cheng-jiao_pai-hang-bang_enter-one"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 点击一键点击
    x, y = fixed_data["cheng-jiao_pai-hang-bang_yi-jian-dian-zan"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 点击几次完成
    for _ in range(8):
        do_painless_click(x0, y0)
        time.sleep(SHT_TIME)
    time.sleep(SHT_TIME)
    # 退出当前点赞页面
    x, y = fixed_data["general_exit"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 进入跨服点赞页面
    x, y = fixed_data["cheng-jiao_pai-hang-bang_enter-kua-fu"]
    time.sleep(SHT_TIME)
    mouse_click(x+x0, y+y0)
    # 进入可点赞页面
    x, y = fixed_data["cheng-jiao_pai-hang-bang_enter-one"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 点击一键点击
    x, y = fixed_data["cheng-jiao_pai-hang-bang_yi-jian-dian-zan"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 点击几次完成
    for _ in range(8):
        do_painless_click(x0, y0)
        time.sleep(SHT_TIME)
    # 退出当前点赞页面
    for _ in range(2):
        x, y = fixed_data["general_exit"]
        mouse_click(x+x0, y+y0)
        time.sleep(SHT_TIME)
    # 返回 home
    do_enter_home(x0, y0)

# 根据图片推测状态,返回状态，以及对应状态的绝对位置（if any）
def obtain_status(x0 = 0, y0 = 0, acc_threshold = 0.7):
    # 测试中
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    # print(f"x0 = {x0}, y0 = {y0}")
    # 财神 or 主页 or 邀请赴宴 or 进入游戏状态
    template_names = {
        "cai_shen" : "status_templates/5_cai_shen_test.png",
        "home" : "status_templates/home.png",
        "invite" : "status_templates/0_fu_yan.png",
        "enter_game" : "status_templates/0000_hoi_ci_yau_si.png" 
    }
    status_list = list(template_names.keys())
    
    if True:
        print(f"Source: pos left, top, right, down {x0, y0,}", x0 + fixed_data["full_screen"][0], y0+ fixed_data["full_screen"][1])
        im_screen = ImageGrab.grab().crop((x0, y0, x0 + fixed_data["full_screen"][0], y0+ fixed_data["full_screen"][1]))
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        
    max_status = None
    max_status_pos = (0,0)
    max_acc = acc_threshold
    for status in status_list:
        target = cv2.imread(os.path.join(template_names[status]))
        results = cv2.minMaxLoc(cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED))
        acc = results[1]  # 测试两幅图像精确度
        pic_pos = results[3]
        x = int(pic_pos[0]) + int(target.shape[1] / 2) + x0
        y = int(pic_pos[1]) + int(target.shape[0] / 2) + y0
        print(f"{status} At pos {x,y} with acc {acc:1.4f}")
        if acc > max_acc:
            print(f"DEBUG: At pos {(pic_pos[0]+x0, pic_pos[1]+y0)} with acc {acc:1.4f}")
            max_acc = acc
            max_status = status
            max_status_pos = (x,y)
    print(f"Max likelihood status: {max_status}, at {max_status_pos}, with acc {max_acc:1.4f}")
    return max_status, max_status_pos

# 查看是否有 宴会入口
def find_if_yanhui_opened(x0 = 0, y0 = 0, yan_hui_entry_path = "status_templates/01_fu_yan.png"):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    im_screen = ImageGrab.grab().crop((x0, y0, x0 + fixed_data["full_screen"][0], y0+ fixed_data["full_screen"][1]))
    source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
    target = cv2.imread(os.path.join(yan_hui_entry_path))
    results = cv2.minMaxLoc(cv2.matchTemplate(source, target, cv2.TM_CCOEFF_NORMED))
    acc = results[1]  # 测试两幅图像精确度
    pic_pos = results[3]
    return (acc, pic_pos)

def obtain_screen_x_y_brightness(x, y):
    im_screen = ImageGrab.grab()  # 保存
    im_screen.save(r'./temp.png')
    image = cv2.imread(r'./temp.png')
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Access the pixel value at the specified point
    brightness = gray_image[y, x]
    return brightness

def obtain_screen_x_y_pixel(x, y):
    im_screen = ImageGrab.grab()  # 保存
    im_screen.save(r'./temp.png')
    image = cv2.imread(r'./temp.png')
    pixel = image[y, x] # image bgr
    return pixel

def do_enter_game(x0 = 0, y0 = 0, debug = False):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
    status_info = obtain_status(x0, y0, acc_threshold=0.7)
    x,y = status_info[1]
    
    if status_info[0] == "enter_game":
        mouse_click(x, y)
        time.sleep(SHT_TIME)
        if debug:
            print(f"do_enter_game: click enter at x = {x}, y = {y}")
    # wait until color changed
    x,y = fixed_data["kei-dong_brightness-detect-pos0"]
    x,y = x+x0, y+y0
    cur_pixel = obtain_screen_x_y_pixel(x, y)
    if debug:
        print(f"pixel at x = {x}, y = {y} is {cur_pixel}")
    nxt_pixel = cur_pixel
    max_times = 40
    print(f"nxt_pixel = {nxt_pixel}")
    while(nxt_pixel[0] == cur_pixel[0] and nxt_pixel[1] == cur_pixel[1] and nxt_pixel[2] == cur_pixel[2]  and max_times > 0):
        time.sleep(SHT_TIME)
        nxt_pixel = obtain_screen_x_y_pixel(x,y)
        if debug:
            print(f"pixel at x = {x}, y = {y} is {nxt_pixel}")
        max_times -= 1
    max_time = 5 # 
    time.sleep(MID_TIME)
    if debug:
        print(f"waited {MID_TIME} seconds before detecting enter-game status")
    while(max_time != 0):
        x, y = fixed_data['kei-dong_brightness-detect-pos0']
        brightness0 = obtain_screen_x_y_brightness(x+x0, y+y0)
        if debug:
            print(f"Brightness detected at {x+x0, y+y0} is {brightness0}")
        x, y = fixed_data['kei-dong_brightness-detect-pos1']
        brightness1 = obtain_screen_x_y_brightness(x+x0, y+y0)
        if debug:
            print(f"Brightness detected at {x+x0, y+y0} is {brightness1}")
        if brightness1 - brightness0 <= 70 or brightness0 >= 100: 
            return True
        else:    
            x,y = fixed_data['kei-dong_li-xian-jiang-li']
            mouse_click(x+x0, y+y0)
            if debug:
                print(f"do_enter_game: click enter at x = {x+x0}, y = {y+y0}")
            x,y = fixed_data['kei-dong_event-page-dou-luo']
            mouse_click(x+x0, y+y0)
            if debug:
                print(f"do_enter_game: click enter at x = {x+x0}, y = {y+y0}")
            x,y = fixed_data['kei-dong_go-to-event']
            mouse_click(x+x0, y+y0)
            if debug:
                print(f"do_enter_game: click enter at x = {x+x0}, y = {y+y0}")
        max_time -= 1
        time.sleep(SHT_TIME)
    if debug:
        print(f"Unexpected exit function: do_enter_game(x0 = {x0}, y0 = {y0})")
    return False

def do_from_home_do_shang_zhan(x0 = None, y0 = None, debug = False):
    if x0 == None or y0 == None:
        x0, y0 = get_da_zhang_gui_pos()
    do_enter_home(x0, y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["home-cheng_jiao"]
    mouse_click(x+x0, y+y0, debug = debug)
    time.sleep(SHT_TIME)
    fixed_data["cheng-jiao_shang-zhan"] = (650, 800)
    x,y = fixed_data["cheng-jiao_shang-zhan"]
    mouse_roll_up(20, rev = False, wait_time=EX_SHT_TIME, x0 = x0, y0 = y0)
    mouse_click(x+x0, y+y0, debug = debug)
    time.sleep(SHT_TIME)
    
    fixed_data["cheng-jiao_shang-zhan_zhan-dou"] = (700, 1060)
    x,y = fixed_data["cheng-jiao_shang-zhan_zhan-dou"]
    mouse_click(x+x0, y+y0, debug = debug)
    time.sleep(SHT_TIME)
    
    fixed_data["cheng-jiao_shang-zhan_zhan-dou_quick"] = (400, 1130)
    x,y = fixed_data["cheng-jiao_shang-zhan_zhan-dou_quick"]
    mouse_click(x+x0, y+y0, debug = debug)
    time.sleep(SHT_TIME)
    
    for _ in range(3):
        do_painless_click(x0, y0)
    
    # go back home
    do_enter_home(x0, y0)
    
# 检测状态，根据结果执行提前编辑的内容
def process_pre_defined_event_with_interrupt_event():
    _round = 990 #0-999
    while True:
        x0,y0 = get_da_zhang_gui_pos()
        status_info = obtain_status(x0, y0, acc_threshold=0.7)
        click_pos = status_info[1]
        x,y = click_pos
        if status_info[0] == "invite":
            logging.info("Get invitations")
            do_after_invited(x0, y0)
            do_exit_to_the_end()
        elif status_info[0] == "cai_shen":
            logging.info("DO Cai Shen")
            do_painless_click(x0, y0)
        elif status_info[0] == "enter_game":
            logging.info("Enter Game")
            mouse_click(x, y) #
            time.sleep(MID_TIME) # waits longer
            if do_enter_game(x0, y0, True) == False:
                print("do_enter_failed")
            time.sleep(SHT_TIME)
        elif status_info[0] == "home":
            logging.info("Click home-home") # meaningless
            x,y = fixed_data["home-home"]
            mouse_click(x+x0, y+y0)
            if False:
                if _round >= 990:
                    do_公屏粘贴发言()
                    do_enter_home()
        else: # None
            do_painless_click(x0, y0)
        logging.info(f"Do {status_info[0]} at {status_info[1]}")
        print(f"Do {status_info[0]} at {status_info[1]}")
        time.sleep(MID_TIME)
        # round = 0 跨服宴会时点一下
        if _round == 0:
            logging.info("At round = 0, enter home, enter fuyan")
            print("At round = 0, enter home, enter fuyan")
            acc_threshold = 0.75
            results = find_if_yanhui_opened()
            acc = results[0]
            click_pos = results[1]
            x, y = click_pos
            if acc >= acc_threshold:
                mouse_click(x+x0, y+y0)
                time.sleep(MID_TIME)
                mouse_click(x+x0, y+y0)
                time.sleep(MID_TIME)
                do_after_invited(x0, y0)
        else:
            logging.info(f"round {_round} finished")
            print(f"round = {_round} finished")
        _round = (_round+1)%1000

def do_based_on_task_command(task_command):
    x0, y0 = get_da_zhang_gui_pos()
    if task_command == "qian_zhuang":
        do_enter_stores(x0=x0, y0=y0)
        time.sleep(SHT_TIME)
        mouse_roll_up(5, rev = False, wait_time=EX_SHT_TIME)
        time.sleep(SHT_TIME)
        do_at_stores_click_qian_zhuang(x0=x0, y0=y0, times=1000)
    elif task_command == "xiao_yu":
        do_xiao_yu(x0=x0, y0=y0)
    elif task_command == "home_enter_kua_fu":
        do_home_enter_kua_fu(x0=x0,y0=y0)
    elif task_command == "do_huodong_enter_yanhuizhengba":
        do_kua_fu_enter_yanhuizhengba(x0=x0, y0=y0)
    elif task_command == "do_yan_hui_page_enter_bai_fu_and_fu_yan":
        do_yan_hui_page_enter_bai_fu_and_fu_yan()
    elif task_command == "do_exit_to_the_end":
        do_exit_to_the_end()
    elif task_command == "do_in_cai_shen_miao_click_points":
        do_in_cai_shen_miao_click_points()
    elif task_command == "go_home_to_cai_shen_miao":
        go_home_to_cai_shen_miao()
    elif task_command == "do_from_home_to_do_all_in_cai_shen_miao":
        do_from_home_to_do_all_in_cai_shen_miao()
    elif task_command == "do_from_home_do_dian_zan":
        do_from_home_do_dian_zan()
    elif task_command == "do_from_home_do_shang_zhan":
        do_from_home_do_shang_zhan(x0, y0)
