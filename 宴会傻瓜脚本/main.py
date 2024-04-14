
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

LONG_TIME = 100
MID_TIME = 10
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
        time.sleep(1.05)
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

