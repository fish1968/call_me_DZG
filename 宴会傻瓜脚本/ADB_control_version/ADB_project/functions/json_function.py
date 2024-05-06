from ADB_project.functions import set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
import json
import datetime
import os
from ADB_project.functions.local_data import json_file_path as file_path

def read_json_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            data = json.load(file)
    else:
        data = {
            "do_xing_shan": True,
            "today": str(datetime.date.today())
        }
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
        print(f"Created new JSON file at {file_path}")
    return data

def read_json(file_path = file_path, entry = None):
    if entry == None:
        raise Exception("Unexpected Entry Value")
    with open(file_path, "r") as file:
        try:
            data = json.load(file)
            result = data[entry]
            return result
        except:
            return None
    
def update_json(file_path = file_path, entry: None|str = None, value = None):
    if entry == None:
        return
    with open(file_path, "r") as file:
        data = json.load(file)
        data[entry] = value
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

@future_care
def update_local_json_data_to_date(file_path = file_path):
    # update file time to today
    current_date = str(datetime.date.today())
    data = read_json_data(file_path=file_path)
    if data["today"] != current_date:
        data["today"] = current_date
        data["do_xing_shan"] = 0
        data["recruit_num"] = 0
        data["zhi_you_gift"] = 0
        data["zhen_shou_raise_up"] = 0
        data["zhi_you_skills"] = 0
        # update file
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
