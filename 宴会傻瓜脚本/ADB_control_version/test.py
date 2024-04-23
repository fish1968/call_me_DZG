import os
import subprocess
import time
from functions import *
from local_data import local_device


def need_test():
    obtain_screenshot()
    tu_di_raise_up(device=local_device) # 弹窗——导致卡死， 需要修改，现在有一键培养
    start_apk_game() # 容易点到特权

def passed_test():
    click_qian_zhuang_from_home(100)
    
    click_union_basic_constrcut()

    test_move_screenshot()

    remove_local_file()
    
    daily_click_home_shang_cheng_ling_qu(device=local_device, sleep_time=1)

    daily_click_xian_shi_chong_zhi(device=local_device, sleep_time=1)
    
    daily_click_qian_dao(device=local_device, sleep_time=1)
    
    daily_click_qian_zhuang_wei_ren(device=local_device, sleep_time=1)

    daily_click_rank(local_device, 1)
    
    ri_chang_ren_wu_qian_zhuang_20()
    daily_xing_yun_duo_bao_2()

def test_yu_gan():
    # 鱼竿测试，发现有偏移现象
    st = 1.3
    for _ in range(10):
        print(f"st = {st}")
        daily_ling_qu_yu_gan(sleep_time = st)
        st -= 0.1

def daily_once(device = local_device):
    # 启动
    # start_apk_game() # 容易卡住
    enter_chuang_dang(device=device, sleep_time=6)
    enter_cheng_jiao(device=device, sleep_time=6)
    enter_shang_pu(device=device, sleep_time=6)
    enter_home(device=device, sleep_time=6)
    # 行善
    daily_xing_shan(device=device)
    # 日常邮件
    daily_mail_process(device=device)
    # 商会建设
    click_union_basic_constrcut(device=device)
    # 商战
    shang_zhan(device=device)
    # 身份元宝领取
    daily_profile_yuan_bao(device=device,sleep_time=1)
    # 幸运夺宝
    daily_xing_yun_duo_bao_2(device=device) # 貌似点不到？
    # 免费商城领取
    daily_click_home_shang_cheng_ling_qu(device=device, sleep_time=1)
    # 钱庄点击 20
    ri_chang_ren_wu_qian_zhuang_20(device=device)
    # 日常钱庄委任更换
    daily_click_qian_zhuang_wei_ren(device=device, sleep_time=1)
    # 乔迁点赞
    daily_qiao_qian(device=device, sleep_time=0.8)
    # 排行榜点赞与上门点赞
    daily_click_rank(device=device, sleep_time=1)
    # 财神庙点赞
    daily_cai_shen_miao_like(device=device, sleep_time=0.8)
    # 日常闯荡一次
    ri_chang_chuang_dang(device=device, sleep_time=1)
    # 城郊游历
    daily_cheng_jiao_you_li(device=device)
    # 庄园与鱼竿领取
    daily_ling_qu_yu_gan(device = device, sleep_time = 1)
    # 商铺的三个 医馆 酒肆 药铺
    daily_do_yi_guan()
    daily_do_jiu_si()
    daily_do_yao_pu()
    # 等待
    for _ in range(3):
        for _ in range(10):
            time.sleep(60)
            click_painless(device=device, times = 10)
        click_union_basic_constrcut(device=device)
    time.sleep(3600 - 3  * 60 * 10)
    click_painless(device=device, times=10)
    shang_zhan(device=device)
    time.sleep(3600)
    click_painless(device=device, times=10)
    shang_zhan(device=device)


start = time.time()
daily_once(device=local_device)
# daily_mail_process()
# daily_cai_shen_miao_like(sleep_time=0.6)
# daily_cheng_jiao_you_li()
# click_qian_zhuang_from_home(30)
# daily_click_rank()
# tu_di_raise_up(device=local_device)
# daily_ling_qu_yu_gan(device = local_device, sleep_time = 1)
# shou_lie(device=local_device, sleep_time=1)
# ri_chang_chuang_dang()
# daily_xing_shan()
# shang_zhan()
# move_to_end(bottom=1)
# daily_cai_shen_miao_like()
# daily_qiao_qian()
# time.sleep(3)
# daily_profile_yuan_bao()
# start_apk_game()
# daily_do_yi_guan()
# daily_do_jiu_si()
# daily_do_yao_pu()
end = time.time()
print(end-start)

while True:
    click_painless(device=local_device, sleep_time=10,times=1000)
