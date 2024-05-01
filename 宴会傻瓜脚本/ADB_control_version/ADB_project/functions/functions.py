import os
import subprocess
import time
import set_project_dir
from set_project_dir import future_care
from ADB_project.functions.local_data import local_device, debugging, adb_debugging, game_package_name, json_file_path
from ADB_project.functions.basic_dzg_functions import click_painless, click_wait, click_exit
import ADB_project.data.constant as constant
from adb_operations import adb_start_activity

