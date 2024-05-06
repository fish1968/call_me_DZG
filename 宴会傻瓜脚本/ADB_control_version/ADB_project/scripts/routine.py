import set_project_dir
import time
from ADB_project.functions.local_data import local_device, debugging, json_file_path
# from ADB_project.functions.local_data import local_device, debugging, json_file_path
from ADB_project.functions.json_function import check_and_update_local_json_data
from ADB_project.functions.daily_functions import daily_do_once, click_wait, init
from ADB_project.functions.events_functions import da_long, shou_lie, quick_fox

if __name__ == "__main__":
    init_begin = time.time()
    device = init()
    init_end = time.time()
    if debugging:
        print(f"\nEmulator is on and connected by {device}, init time = {init_end - init_begin}\n")

    begin_t = time.time()
    # obtain whether do xing_shan based on current date
    end_t = time.time()
    if debugging:
        print(f"Daily_do_once finished in {end_t - begin_t}")
    # Below should be in file
    has_da_long = False
    has_shou_lie = False
    while True:
        t_hour = time.localtime(time.time()).tm_hour
        print(f" t_hour = {t_hour}")
        if t_hour == 20 and (has_da_long == False):
            da_long(device = device, sleep_time=2)
            has_da_long = True
        if (t_hour == 12 or t_hour == 13 )and (has_shou_lie == False):
            shou_lie(device = device, sleep_time=2)
        click_wait(total_time = 100, sleep_time = 10, device = local_device)
