#----All refferred to a CSDN Blog: https://blog.csdn.net/luoyir1997/article/details/119117168
import dzg_data_and_function as my_dzg 

print("BEGIN")
my_dzg.ImageTest().starttest()#启动软件
my_dzg.time.sleep(my_dzg.MID_TIME)
# commands = [1, 10, 9, 1] 
# commands = [0] # 点击钱庄
# commands = [9] # 去财神庙点赞
# commands = [10] # 排行榜点赞
# commands = [10, 9] # 点赞排行榜，财神庙点赞
commands = [11] # 商战
# one  time task
for command_idx in commands:
    test_command = my_dzg.command_list[command_idx]
    my_dzg.do_based_on_TEST_Command(test_command)
    my_dzg.time.sleep(SHT_TIME)
# long looping
my_dzg.process_pre_defined_event_with_interrupt_event()

exit()
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
