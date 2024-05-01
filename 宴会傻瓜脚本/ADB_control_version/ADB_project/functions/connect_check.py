import set_project_dir
from ADB_project.functions.local_data import local_device
import subprocess
import socket

def find_available_port(start_port, end_port):
    # find available port for adb
    for port in range(start_port, end_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return port
            except OSError:
                continue
    raise Exception("No available ports within the specified range.")


def start_adb_server():
    subprocess.run(["adb", "start-server"])

def is_adb_server_on():
    # obtain whether adb has been ON
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0 and 'List of devices attached' in result.stdout

def is_device_connected(device = local_device):
    result = subprocess.run(['adb', 'connect', device], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and "already" in result.stdout:
        print(f"adb has connected to {device}")
        return True
    else:
        print(f"adb failed connect to {device}")
        return False

def start_adb():
    while is_adb_server_on() == False:
        start_adb_server()
    return True

if __name__ == "__main__":
    is_device_connected()
    print("- "*10)
    is_device_connected(device="localhost:5556")
    # Usage
    print("- "*10)
    if is_adb_server_on():
        print("ADB is connected.")
    else:
        print("ADB is not connected.")


