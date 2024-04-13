
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

class POINT(Structure):
    _fields_ = [("x", c_ulong),("y", c_ulong)]
 
def get_mouse_point():
    po = POINT()
    windll.user31.GetCursorPos(byref(po))
    return int(po.x), int(po.y)
 
def mouse_click(x=None,y=None):
    if not x is None and not y is None:
        mouse_move(x,y)
        time.sleep(1.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
 
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
        time.sleep(1)
        print('*************start successfully!**************')
    
    #单击图片
    def on_click(self,target):
            x,y = self.match.find_img(target)
            self.mouse_click(x,y)
            print('在[%d,%d]位置单击1次'%(x,y,target))
    
    def starttest(self):
        self.START_APP(小程序启动路径)
 

def click_picture(picture):
    '''单击图片'''
    base_path = os.path.join(picture)
    im_screen = ImageGrab.grab()  # 保存
    im_screen.save(r'Test.png')
    source = cv2.imread(r'Test.png')
    template = cv2.imread(base_path)
    result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)
    pos_start = cv2.minMaxLoc(result)[3]
    x = int(pos_start[0]) + int(template.shape[1] / 2)
    y = int(pos_start[1]) + int(template.shape[0] / 2)
    s = cv2.minMaxLoc(result)[1]  # 测试两幅图像精确度
    if s >= 0.9:
        # print(picture)
        print("执行点击操作：点击",picture,"成功！，坐标：(",x,",",y,")  accuracy = ", s)
        mouse_click(x,y)
        if picture == "1.jpg":
            logging.info("当前时间是 {0}，现在识别到了图片1，准确率是 {1}".format(datetime.datetime.now(), s))
        time.sleep(0.1)
    else:
        print(f"未识别出目标 {picture}, accuracy = {s}", datetime.datetime.now())

def click_pictures(pictures=[], targets=[], accuracy_threshold = 0.7):
    if len(targets) == 0:
        for picture in pictures:
            base_path = os.path.join(picture)
            template = cv2.imread(base_path)
            targets.append(template)
            print("reading")
    index = 0
    for picture in pictures:
        '''单击图片'''
        # Define the coordinates of the region of interest
        left = 0  # X-coordinate of the left edge of the region
        top = 0  # Y-coordinate of the top edge of the region
        right = 2560/3  # X-coordinate of the right edge of the region
        bottom = 1440  # Y-coordinate of the bottom edge of the region

        # Crop the screenshot to the specified region
        im_screen = ImageGrab.grab()  # 保存
        im_screen = im_screen.crop((left, top, right, bottom))
        # im_screen.save(r'Test.png')
        source = np.array(im_screen.getdata(), dtype ='uint8').reshape((im_screen.size[1], im_screen.size[0], 3))
        # source = cv2.imread(r'Test.png')
        # base_path = os.path.join(picture)
        # template = cv2.imread(base_path)
        template = targets[index]
        index += 1
        find_matching_result = cv2.matchTemplate(source, template, cv2.TM_CCOEFF_NORMED)

        s = cv2.minMaxLoc(find_matching_result)[1]  # 测试两幅图像精确度
        if s >= accuracy_threshold:
            img_pos = cv2.minMaxLoc(find_matching_result)[3]
            x = int(img_pos[0]) + int(template.shape[1] / 2)
            y = int(img_pos[1]) + int(template.shape[0] / 2)
            # print(picture)
            print("执行点击操作：点击",picture,"成功！，坐标：(",x,",",y,")  accuracy = ", s)
            if "fu" in picture:
                for _ in range(3):
                    mouse_click(x,y)
                    mouse_click(x,y)
                    mouse_click(x,y)
                    time.sleep(0.5)
            else:
                mouse_click(x,y)
                time.sleep(0.5)
                mouse_click(x,y)

            if "fu_yan" in picture:
                logging.info("当前时间是 {0}，现在识别到了图片1，准确率是 {1}".format(datetime.datetime.now(), s))
            elif '2' in picture:
                time.sleep(1)
            # time.sleep(0.1)
        else:
            print(f"未识别出目标 {picture}, accuracy = {s}", datetime.datetime.now())



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
        
    while True:
        click_pictures(pictures=pictures, targets=targets)
        time.sleep(20)
#   click_picture('picture6.png')

while True:
    pass

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

