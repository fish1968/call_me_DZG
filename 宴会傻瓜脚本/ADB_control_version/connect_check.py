import subprocess
from local_data import local_device

def is_adb_connected():
    result = subprocess.run(['adb', 'devices'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.returncode == 0 and 'List of devices attached' in result.stdout

def is_device_connected(device = local_device):
    print("device is " + str(device))
    result = subprocess.run(['adb', 'connect', device], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0 and "already" in result.stdout:
        print(f"adb connected to {device}")
        return True
    else:
        print(f"adb failed connect to {device}")
        return False
    #print(f"return code: {result.returncode}")
    #print(f"return text: {result.stdout}")

if __name__ == "__main__":
    is_device_connected()
    print("- "*10)
    is_device_connected(device="localhost:5556")
    # Usage
    print("- "*10)
    if is_adb_connected():
        print("ADB is connected.")
    else:
        print("ADB is not connected.")


