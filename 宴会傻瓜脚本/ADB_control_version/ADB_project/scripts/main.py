import set_project_dir
import time
from ADB_project.functions.local_data import local_device, debugging, json_file_path
from ADB_project.functions.json_function import update_local_json_data_to_date,read_json
from ADB_project.functions.daily_functions import daily_do_once, click_wait, init

if __name__ == "__main__":
    init_begin = time.time()
    device = init()
    init_end = time.time()
    if debugging:
        print(f"\nEmulator is on and connected by {device}, init time = {init_end - init_begin}\n")

    begin_t = time.time()
    # obtain whether do xing_shan based on current date
    update_local_json_data_to_date(file_path=json_file_path)
    do_xing_shan = True if (read_json(entry="do_xing_shan") == None or read_json(entry = "do_xing_shan") == 0) else False 
    daily_do_once(device=local_device, do_xing_shan=do_xing_shan)
    end_t = time.time()
    if debugging:
        print(f"Daily_do_once finished in {end_t - begin_t}")
    from ADB_project.scripts import routine
    # while True:
    #     click_wait(total_time = 100, sleep_time = 10, device = local_device)
