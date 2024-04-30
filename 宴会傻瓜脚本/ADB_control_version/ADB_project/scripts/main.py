import set_project_dir
import time
from ADB_project.functions.local_data import local_device, json_file_path, debugging
from ADB_project.functions.json_function import check_and_update_local_json_data
from ADB_project.functions.functions import daily_do_once, click_wait, init

if __name__ == "__main__":
    init_begin = time.time()
    device = init()
    init_end = time.time()
    if debugging:
        print(f"\nEmulator is on and connected by {device}, init time = {init_end - init_begin}\n")

    begin_t = time.time()
    # obtain whether do xing_shan based on current date
    do_xing_shan = check_and_update_local_json_data(file_path=json_file_path)
    daily_do_once(device=local_device, do_xing_shan=do_xing_shan)
    end_t = time.time()
    if debugging:
        print(f"Daily_do_once finished in {end_t - begin_t}")

    while True:
        click_wait(total_time = 100, sleep_time = 10, device = local_device)
