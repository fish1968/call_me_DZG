import set_project_dir
from ADB_project.functions.img_robots import ImgRobot
from ADB_project.functions.adb_operations import obtain_screenshot, click_once,remove_local_file

from time import time
begin_t = time()

screen_img = "my_screen.png"
target_img = "frog_man.png"
obtain_screenshot(img_name=screen_img, local_dir="./")
aRobot = ImgRobot(screen_img)
bRobot = ImgRobot(target_img)
print(bRobot.get_image_shape())
print(aRobot.get_brightness())
result = aRobot.find_image_position_with_robot(bRobot, threshold = 0.6, at_center=True)
print(result)
if result != None:
    for i in range(10, 500, 40):
        click_once(result[0] + i, result[1], sleep_time = 0.01)
remove_local_file(screen_img)

end_t = time()

print("total duration is " + str(end_t-begin_t))



