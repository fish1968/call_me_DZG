
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
# import keypad
# import ddt
import datetime
#----All refferred to a CSDN Blog: https://blog.csdn.net/luoyir1997/article/details/119117168

import logging
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

小程序启动路径 = r"C:\Users\YabinLabtop\Desktop\叫我大掌柜.lnk"

fixed_data = {
    "full_screen": (786, 1395),
    "header": (765, 44),
    "home-entry-kua-fu": (205, 213),
    "home-home": (80, 1323),
    "home-stores": (200, 1330),
    "home-qian-zhuang": (200, 500),
    "yanhui-box": (680, 20),
    "yanhui-next": (80, 1325),
    "yanhui-in": (640, 1233),
    "yanhui-exit": (40, 33),
    "bai-fu_entry": (700, 680),
    "bai-fu_fu-yan": (400, 1300),
    "bai-fu_exit": (725, 165),
    "text_entry": (480, 1230),
    "text-input": (430, 1210),
    "text-send": (680, 1210),
    "painless-point": (350, 80), #可以随便点，无所谓
    "home-xiao-yu": (750, 830),
    "xiao-yu-execute": (450, 980),
    "xiao-yu-execute-over": (400, 1100),
    # 财神庙找赞点击
    "home-cheng_jiao": (600, 1325),
    "cai_shen_miao": (370, 570),
    "cai_shen_miao-bai_fang": (400, 1250),
    "page_full_screen": (765, 1360),
    
    "general_exit": (40, 35)
}

LONG_TIME = 60*5
MID_TIME = 5
SHT_TIME = 1
EX_SHT_TIME = 0.1

class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]
 
def get_mouse_point():
    po = POINT()
    windll.user31.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
 
def mouse_click(x=None,y=None, to_origin = True):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(EX_SHT_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    if to_origin:
        mouse_move(0,0)
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

def key_input(str=''):
    for c in str:
        win32api.keybd_event(VK_CODE[c],0,0,0)
        win32api.keybd_event(VK_CODE[c],0,win32con.KEYEVENTF_KEYUP,0)
        time.sleep(-1.01)
 
class ImageTest:
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
    
    def starttest(self):
        self.START_APP(小程序启动路径)
 

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
            x = x0 + 200
            y = y0 + 256
            mouse_click(x,y)
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

def get_da_zhang_gui_pos(da_zhang_gui_img_path = "da_zhang_gui_wx.jpg", window_length = 704,window_height = 1404):
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
        print(x,y,s)
    print(x,y,s)
    return (int(x-window_length/2-30), y)
    
def 公屏粘贴发言(type=True):
    
    x0,y0 = get_da_zhang_gui_pos()
    # 骗赞
    mouse_click(x0+400, y0+1230)
    time.sleep(SHT_TIME)
    mouse_click(x0+400, y0+1230)
    time.sleep(SHT_TIME)
    mouse_click(x0+400, y0+1230)
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
    mouse_click(x0+680, y0+1230)
    time.sleep(SHT_TIME)
    mouse_click(x0+740, y0+320)

def do_enter_home(x0 = 0, y0 = 0):
    # 点击府邸
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["home-home"]
    mouse_click(x+x0, y+y0)

def do_enter_stores(x0 = 0, y0 = 0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["home-stores"]
    mouse_click(x+x0, y+y0)
    
def do_click_qian_zhuang(x0 = 0, y0 = 0, times = 20):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]

    x,y = fixed_data["home-qian-zhuang"]
    for _ in range(times):
        mouse_click(x+x0, y+y0)
        # time.sleep(EX_SHT_TIME)
def do_xiao_yu(x0=0,y0 = 0):
    # 在主页
    # 点击小玉
    x,y = fixed_data["home-xiao-yu"]
    mouse_click(x+x0, y+y0)
    time.sleep(MID_TIME) # 需要等待长一点
    # 点击执行
    x,y = fixed_data["xiao-yu-execute"]
    mouse_click(x+x0, y+y0)
    time.sleep(MID_TIME)
    # 点击确定
    x,y = fixed_data["xiao-yu-execute-over"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    # 退出界面
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
def do_home_enter_kua_fu(x0=0, y0=0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["home-entry-kua-fu"]
    print(x,y)
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)

def do_huodong_enter_yanhuizhengba(x0=0, y0= 0, yanhui_picture_path = "img_templates/10_yanhui_zhengba.jpg",acc_threshold = 0.7):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
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
    x += int(target.shape[0] / 2)
    y += int(target.shape[1] / 2)
    mouse_click(x+x0, y+y0)
    time.sleep(MID_TIME)

def do_yan_hui_page_enter_bai_fu_and_fu_yan(x0=0, y0=0):
    # 宴会争霸界面 开始 到结束
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["bai-fu_entry"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["bai-fu_fu-yan"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["bai-fu_exit"]
    mouse_click(x+x0, y+y0)

def do_exit_to_the_end(x0 = 0, y0 = 0, exit_picture_path = "img_templates/13_exit.jpg",acc_threshold = 0.8):
    # 一直退出，预期到主页
    # 由于图片比较小，很容易错误识别，因此精确度权重提高
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["yanhui-exit"]
    acc = 1
    round = 4
    target_path = os.path.join(exit_picture_path)
    target = cv2.imread(target_path)
    while (acc > acc_threshold):
        mouse_click(x+x0, y+y0,to_origin=True)
        time.sleep(MID_TIME)
        im_screen = ImageGrab.grab().crop((x0,y0,x0+fixed_data["full_screen"][0],y0+fixed_data["yanhui-exit"][1]*3))
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        results = cv2.minMaxLoc(cv2.matchTemplate(source,target,cv2.TM_CCORR_NORMED))
        acc = results[1]
        pic_pos = results[3]
        print(f"Exit position found as {pic_pos} with acc {acc:1.4f}")
        round -= 1
        if round == 0:
            print("Too many rounds, wrongly detected")
            break
        # x,y = pic_pos # x y unchanged 
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)
    time.sleep(EX_SHT_TIME)
    do_enter_home(x0 = x0, y0 = y0) #点一下 home
    time.sleep(EX_SHT_TIME)

def do_painless_click(x0 = 0, y0 = 0):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["painless-point"]
    mouse_click(x+x0, y+y0)

def do_click_cai_shen(x0=0, y0=0):
    do_painless_click(x0, y0)

def do_click_all_templates(x0 = 0, y0 = 0, template_pic_path = "img_templates/red_point.png",acc_threshold = 0.8, round = 10, delay_time = MID_TIME):
    # 一直点击 target (对于小图标，非常失败)
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
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
            mouse_click(x+x0, y+y0,to_origin=False)
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
    # inside cai shen miao page, do one by one carelessly
    cai_shen_bu_pos = (90, 1150)
    dian_zan_pos = (380, 1100)
    xuan_wu = (520, 360)
    qi_lin = (380, 480)
    qing_long = (650, 600)
    cai_shen_ye_1 = (380, 800)
    cai_shen_ye_2 = (400, 950)
    cai_shen_ye_3 = (400, 1100)
    cai_shen_ye_4 = (180, 1100)
    cai_shen_ye_5 = (615, 1050)
    y_move = 1100
    cai_shen_low_1 = (250, 380  - fixed_data["header"][1])
    cai_shen_low_2 = (550, 380  - fixed_data["header"][1])
    cai_shen_low_31 = (80, 550  - fixed_data["header"][1])
    cai_shen_low_32 = (220, 550 - fixed_data["header"][1])
    cai_shen_low_33 = (550, 550 - fixed_data["header"][1])
    cai_shen_low_34 = (700, 550 - fixed_data["header"][1])
    cai_shen_low_35 = (400, 600 - fixed_data["header"][1])
    cai_shen_low_41 = (150 , 850- fixed_data["header"][1])
    cai_shen_low_42 = (400, 860 - fixed_data["header"][1])
    cai_shen_low_43 = (650, 850 - fixed_data["header"][1])
    cai_shen_low_51 = (150 , 1000- fixed_data["header"][1])
    cai_shen_low_52 = (400, 1020- fixed_data["header"][1])
    cai_shen_low_53 = (650, 1000- fixed_data["header"][1])
    miao_list_up = [    
        xuan_wu,
        qi_lin,
        qing_long,
        cai_shen_ye_1,
        cai_shen_ye_2,
        cai_shen_ye_3,
        cai_shen_ye_4,
        cai_shen_ye_5,
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
        time.sleep(0.5)  # Adjust the sleep duration as needed
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    x,y = fixed_data["painless-point"]
    
    def click_one_miao(x,y,x0,y0):
        mouse_click(x+x0,y+y0, to_origin=False)
        time.sleep(SHT_TIME)
        mouse_click(x0+cai_shen_bu_pos[0],y0+cai_shen_bu_pos[1], to_origin=False)
        time.sleep(SHT_TIME)
        mouse_click(x0+dian_zan_pos[0],y0+dian_zan_pos[1], to_origin=False)
        time.sleep(SHT_TIME)
        # exit
        for _ in range(2): # 需要点赞 与 没有点赞的情况各需要 1-2次
            do_painless_click(x0=x0, y0=y0)
            time.sleep(SHT_TIME)
        mouse_click(x0+fixed_data["general_exit"][0], y0+fixed_data["general_exit"][1], to_origin=False)
        time.sleep(MID_TIME)

    for point in miao_list_up:
        click_one_miao(point[0], point[1], x0, y0)

    time.sleep(SHT_TIME)
    # move mouse to a lower position on the page (for later dragging event)
    mouse_move(x0+cai_shen_ye_4[0], y0+cai_shen_ye_4[1])
    time.sleep(SHT_TIME)
    
    print("drag begin")
    logging.info("drag starts")
    drag_and_move_up()
    logging.info("drag finished")
    print("drag end")
    
    for point in miao_list_down:
        click_one_miao(point[0], point[1], x0, y0)
    # do_click_all_templates(x0=x0, y0=y0,template_pic_path=red_imag_path, acc_threshold=0.8, round = 10, delay_time = MID_TIME)

def go_home_to_cai_shen_miao(x0 =0 , y0 =0 ):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    pos = fixed_data["home-cheng_jiao"]
    x,y = pos
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)
    x,y = fixed_data["cai_shen_miao"]
    mouse_click(x+x0, y+y0)
    time.sleep(SHT_TIME)

def do_from_home_to_do_all_in_cai_shen_miao(x0=0, y0=0, red_imag_path="img_templates/red_point.png"):
    if x0 == 0 and y0 == 0:
        x0,y0 = get_da_zhang_gui_pos()
        y0 += fixed_data["header"][1]
    go_home_to_cai_shen_miao(x0, y0)
    do_in_cai_shen_miao_click_points(x0,y0,red_imag_path)

TESTs = ["qian_zhuang", "xiao_yu", "home_enter_kua_fu", "do_huodong_enter_yanhuizhengba", "do_yan_hui_page_enter_bai_fu_and_fu_yan","do_exit_to_the_end", "do_click_cai_shen", "do_in_cai_shen_miao_click_points", "go_home_to_cai_shen_miao", "do_from_home_to_do_all_in_cai_shen_miao"]
TEST = TESTs[-1]
if TEST != "":
    print("BEGIN")
    ImageTest().starttest()#启动软件
    time.sleep(SHT_TIME)
    x0, y0 = get_da_zhang_gui_pos()
    y0 += fixed_data["header"][1]
    if TEST == "qian_zhuang":
        do_enter_stores(x0=x0, y0=y0)
        time.sleep(SHT_TIME)
        do_click_qian_zhuang(x0=x0, y0=y0, times=100)
    elif TEST == "xiao_yu":
        do_xiao_yu(x0=x0, y0=y0)
    elif TEST == "home_enter_kua_fu":
        do_home_enter_kua_fu(x0=x0,y0=y0)
    elif TEST == "do_huodong_enter_yanhuizhengba":
        do_huodong_enter_yanhuizhengba(x0=x0, y0=y0)
    elif TEST == "do_yan_hui_page_enter_bai_fu_and_fu_yan":
        do_yan_hui_page_enter_bai_fu_and_fu_yan()
    elif TEST == "do_exit_to_the_end":
        do_exit_to_the_end()
    elif TEST == "do_in_cai_shen_miao_click_points":
        do_in_cai_shen_miao_click_points()
    elif TEST == "go_home_to_cai_shen_miao":
        go_home_to_cai_shen_miao()
    elif TEST == "do_from_home_to_do_all_in_cai_shen_miao":
        do_from_home_to_do_all_in_cai_shen_miao()
exit()
while True:
    pass
if __name__ =='__main__':
    ImageTest().starttest()#启动软件
    # Specify the path to the "img_template" subdirectory
    subdirectory = "img_templates"
    # Get the absolute path of the current directory
    current_directory = os.getcwd()
    # Construct the full path of the "img_template" subdirectory
    subdirectory_path = os.path.join(current_directory, subdirectory)
    # Initialize the list to store the file names
    pictures = []
    # Iterate over the files in the subdirectory
    for filename in os.listdir(subdirectory_path):
        # Check if the file is a regular file (not a directory)
        if os.path.isfile(os.path.join(subdirectory_path, filename)):
            file_sub_path = os.path.join(subdirectory, filename)
            # Add the file path to the list
            pictures.append(file_sub_path)
    print(pictures)
    targets = []

    for picture_path in pictures:
        template = cv2.imread(picture_path)
        targets.append(template)
        logging.info("Reading source image " + str(picture_path))
    
    speech_indx = 100
    while True:
        if speech_indx == 100:
            # 公屏粘贴发言()
            pass
        speech_indx = (speech_indx + 1)%100
        time.sleep(MID_TIME)
        x0,y0 = get_da_zhang_gui_pos()
        click_pictures(pictures=pictures, targets=targets, x0 = x0, y0 = y0)
#   click_picture('picture6.png')

if False:
    img_template_path = os.path.join(os.getcwd(), 'test.jpg') #定义一个模板图片路径
    im_screen = ImageGrab.grab() #调用ImageGrab库函数实现对当前主机画面截图并存储至im变量
    im_screen.save(r'SCREEN2.png') #将截图变量im_screen输出保存至工程路径下命名为SCREEN2.PNG
    source = cv2.imread(r'SCREEN2.png')  # 读取当前屏幕截图
    template = cv2.imread(img_template_path)  # 打开要点击的模板图片
    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    print(result)
    pos_start = cv2.minMaxLoc(result)[3]
    x = int(pos_start[0]) + int(template.shape[1] / 2)
    y = int(pos_start[1]) + int(template.shape[0] / 2)
    mouse_click(x, y) #鼠标点击返回坐标点
    time.sleep(2)
    mouse_click(x, y) #鼠标点击返回坐标点
    print(x, y) #打印返回坐标点

