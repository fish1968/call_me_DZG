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

def update_xing_shan(file_path = file_path, to_do = True):
    # update xing_shan to to_do
    with open(file_path, "r") as file:
        data = json.load(file)
        data["do_xing_shan"] = to_do
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)

def check_and_update_local_json_data(file_path = file_path):
    # update file time to today
    current_date = str(datetime.date.today())
    data = read_json_data(file_path=file_path)
    to_do = data["do_xing_shan"]
    if data["today"] == current_date:
        data["do_xing_shan"] = False
    else:
        data["today"] = current_date
    # update file
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)
    return to_do
