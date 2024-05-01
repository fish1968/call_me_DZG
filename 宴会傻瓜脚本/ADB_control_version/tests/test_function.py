# testing functions
import time
import inspect
import set_project_dir
from ADB_project.functions.functions import *
from ADB_project.functions.local_data import local_device

def test_function(function_head, device=local_device, sleep_time=1, times = 1, debugging = True):
    start = time.time()
    device = init(device=device)
    
    function_args = inspect.signature(function_head).parameters.keys()
    
    kwargs = {}
    if 'device' in function_args:
        kwargs['device'] = device
    if 'sleep_time' in function_args:
        kwargs['sleep_time'] = sleep_time
    if 'times' in function_args:
        kwargs['times'] = times
    try:
        function_head(**kwargs)
    except TypeError:
        function_head()
    end = time.time()
    if debugging:
        print(f"Function takes {end-start} seconds")

if __name__ == "__main__":
        
    # test_function(function_head=daily_cai_shen_miao_like, device=local_device, sleep_time=0.3)
    funs = [
        # daily_cai_shen_miao_like
        # click_union_basic_constrcut
        # obtain_screenshot
        # test_move_screenshot
        # start_apk_game
    ]
    exit()
    st = 0.5
    for fun in funs:
        test_function(fun, device = local_device, sleep_time=st)
    
    # def need_test():
    #     # 测试特殊弹窗
    #     start_game()
    #     tu_di_raise_up()
    #     zhi_you_tan_xin()

