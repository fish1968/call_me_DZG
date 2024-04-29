import set_project_dir
from ADB_project.functions.img_robots import ImgRobot
from ADB_project.functions.functions import obtain_screenshot, click_once,remove_local_file

from time import time
begin_t = time()

screen_img = "my_screen.png"
target_img = "exit.png"
obtain_screenshot(img_name=screen_img, local_dir="./")
aRobot = ImgRobot(screen_img)
bRobot = ImgRobot(target_img)
print(aRobot.get_brightness())
result = aRobot.find_image_position_with_robot(bRobot, threshold = 0.8)
print(result)
if result != None:
    click_once(result[0], result[1])
remove_local_file(screen_img)

end_t = time()

print("total duration is " + str(end_t-begin_t))
