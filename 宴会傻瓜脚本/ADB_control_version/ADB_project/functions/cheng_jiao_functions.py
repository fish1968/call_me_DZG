import ADB_project.functions.set_funcs_dir as set_funcs_dir
from ADB_project.functions.set_funcs_dir import future_care
from ADB_project.functions.local_data import local_device, debugging
import ADB_project
from ADB_project.functions.basic_dzg_functions import enter_home, enter_cheng_jiao, click_exit, click_painless, drag_and_move 
from ADB_project.functions.adb_operations import click_once, clicks, move_to_bottom, move_to_left
import time

########## cheng-jiao ###############

def click_union_basic_constrcut(device = local_device, sleep_time = 1):
    if debugging:
        print("click_union_basic_constrcut begin")
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import union
    # at home click cheng-jiao
    enter_home(device=device, sleep_time=sleep_time*3)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*3)
    # go to union
    entry = union["entry"]
    construct_entry = union["construct_entry"]
    basic_construct = union["basic_construct"]
    construct_box = union["construct_box"]
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time)
    # click into construct page
    click_once(construct_entry[0], construct_entry[1], device=device, sleep_time=sleep_time)
    # basic construct
    click_once(basic_construct[0], basic_construct[1], device=device, sleep_time=sleep_time)
    # finish constrcut notice
    click_painless(device=device, sleep_time=sleep_time)
    x , y= construct_box
    loop_num = 20
    for _ in range(0, loop_num):
        click_once(x,y, device=device, sleep_time=sleep_time/10)
        x += int((1080-construct_box[0])/loop_num) # x[0] = 370
    # 商会副业 建设
    fu_ye = union["fu_ye"]
    one_click = union["one_click"]
    do = union["do_fu_ye"]
    click_exit(device=device, sleep_time = sleep_time, times = 1)
    time.sleep(sleep_time)
    print(f"click {fu_ye}")
    click_once(fu_ye[0], fu_ye[1], device=device, sleep_time=sleep_time)
    for _ in range(2):
        clicks(one_click[0], one_click[1], device=device, sleep_time=sleep_time, times = 1)
        clicks(do[0], do[1], device=device, sleep_time=sleep_time, times = 1)
        time.sleep(10)
    click_exit(device=device, sleep_time = sleep_time, times = 2)
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("click_union_basic_constrcut end")

def daily_click_rank(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_click_rank 排行榜点赞 begin")
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import rank
    enter_cheng_jiao(device=    device, sleep_time=sleep_time)
    
    x, y = rank["entry"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = rank["ben_fu"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = rank["enter_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    x, y = rank["yi_jian_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    click_painless(device=device, sleep_time=sleep_time, times=8)
    
    # 点赞
    for _ in range(3):
        drag_and_move(move_x= 0, move_y=-3000, start_x= 500, start_y=1200, device=device, duration_ms=200)
    x, y = rank["person_pos"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    click_once(x,y+100,device=device,sleep_time=sleep_time)
    click_once(x,y+200,device=device,sleep_time=sleep_time)
    x, y = rank["person_bai_fang"]
    click_once(x,y,device=device,sleep_time=sleep_time*3)
    x, y = rank["bai_fang_like"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    x, y = rank["bai_fang_back"]
    click_once(x,y,device=device,sleep_time=sleep_time)
    
    #进入跨服    
    click_exit(device = device, sleep_time = sleep_time)
    x, y = rank["kua_fu"]
    click_once(x,y, device=device, sleep_time=sleep_time)
    x, y = rank["enter_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    x, y = rank["yi_jian_dian_zan"]
    click_once(x,y, device=device, sleep_time=sleep_time*2)
    
    click_painless(device=device, sleep_time=sleep_time, times=8)
    
    for _ in range(3):
        click_once(ex,ey, device=device, sleep_time=sleep_time)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_click_rank 排行榜点赞 end")
 
def daily_qiao_qian(device = local_device, sleep_time = 1):
    
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import qiao_qian
    print("daily_qiao_qian begin")
    enter_home(device= device, sleep_time=sleep_time)
    enter_cheng_jiao(device= device, sleep_time=sleep_time)
    entry = qiao_qian["entry"]
    low_like = qiao_qian["low_like"]
    huang_like = qiao_qian["huang_like"]
    huang_entry = qiao_qian["huang_entry"]
    qin_entry = qiao_qian["qin_entry"]
    bei_shan_entry = qiao_qian["bei_shan_entry"]
    move_y = qiao_qian["bei_shan_move_y"]
    click_once(x=entry[0], y = entry[1], device=device,sleep_time=sleep_time*2)
    
    click_once(huang_entry[0], huang_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(huang_like[0], huang_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_exit(device = device, sleep_time = sleep_time)
    
    click_once(qin_entry[0], qin_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(low_like[0], low_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_once(ex[0], ex[1], device=device,sleep_time=sleep_time)

    drag_and_move(move_x = 0, move_y=move_y, device=device,duration_ms=int(sleep_time*500))
    time.sleep(sleep_time)
    click_once(bei_shan_entry[0], bei_shan_entry[1], device=device,sleep_time=sleep_time*2)
    click_once(low_like[0], low_like[1], device=device,sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 2)
    click_once(ex[0], ex[1], device=device,sleep_time=sleep_time)

    enter_home(device= device, sleep_time=sleep_time)
    print("daily_qiao_qian ends")

def shang_zhan(device= local_device,sleep_time = 1):
    if debugging:
        print("shang_zhan 商战")
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import shang_zhan as sz_data
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    x, y = sz_data["entry"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time*10)
    # 领取 money
    x, y = sz_data["money"]
    click_once(x = x, y = y, device= device, sleep_time=sleep_time)
    
    # 不检查是否点击了一键，做两次
    # 点击fight check
    for _ in range(2):
        x, y = sz_data["fight_check"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time)
        x, y = sz_data["fight"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time*3)
        x, y = sz_data["confirm_fight"]
        click_once(x = x, y = y, device= device, sleep_time=sleep_time)
        
        click_painless(device=device, sleep_time=sleep_time, times=4)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("shang_zhan 商战 end now at home")

@future_care
def daily_cheng_jiao_you_li(device = local_device, sleep_time = 1):
    # 游历时 点击空白位置，或者选择位置速度快点，太慢了
    if debugging:
        print("daily_cheng_jiao_you_li 城郊游历")
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*2)
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import you_li
    # 进入游历
    move_x, move_y = you_li["drag_move"]
    drag_and_move(move_x=move_x, move_y=move_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    x, y =you_li["entry"]
    click_once(x, y , device=device, sleep_time=sleep_time*3) # easily blocked
    # 赠礼
    gift_entry =you_li["shi_jiao_gift"] 
    donate =you_li["shi_jiao_give"] 
    obtain =you_li["shi_jiao_obtain"] 
    click_once(gift_entry[0], gift_entry[1], device=device, sleep_time=sleep_time*3)
    click_once(donate[0], donate[1], device=device, sleep_time=sleep_time)
    click_once(obtain[0], obtain[1], device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times =  2)
    
    cx, cy = you_li["ya_jiu"] # center position
    mx, my = you_li["men_ke_xuan_ze"] # men position
    dx, dy = you_li["drink"] # drink wine
    x, y =you_li["you_li_5"]
    for _ in range(2):
        click_once(x, y , device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times=3)
        click_once(mx, my, device=device, sleep_time=sleep_time)
        click_once(dx, dy, device=device, sleep_time=sleep_time)
        click_once(cx, cy, device=device, sleep_time=sleep_time)
    
    for _ in range(10):
        click_once(cx, cy, device=device, sleep_time=sleep_time)
        click_once(dx, dy, device=device, sleep_time=sleep_time)
        click_once(mx, my, device=device, sleep_time=sleep_time)
        click_painless(device, sleep_time=sleep_time, times=2)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_cheng_jiao_you_li 城郊游历 end")
@future_care
def daily_cai_shen_miao_like(device = local_device, sleep_time = 1):
    # usual sleep_time 0.6 +
    # 经常会点出去，点完大赞后点出去
    # 退出到城郊后会乱入到乔迁
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import cai_shen_miao
    print("daily_cai_shen_miao_like begin")
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time)
    # enter miao
    cai_shen = cai_shen_miao["pos"]
    click_once(cai_shen[0], cai_shen[1], device, sleep_time=sleep_time)
    cai_shen_pu = cai_shen_miao["cai_shen_pu"]
    cai_shen_like = cai_shen_miao["cai_shen_like"]
    big_like = cai_shen_miao["like"]
    # 点大赞
    time.sleep(sleep_time * 5) # waits
    click_once(big_like[0], big_like[1], device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times = 5)
    
    # 点赞上方的庙宇
    for pos in cai_shen_miao["ups"]:
        time.sleep(sleep_time)
        click_once(pos[0], pos[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_pu[0], cai_shen_pu[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_like[0], cai_shen_like[1], device=device, sleep_time=sleep_time*2)
        click_painless(device=device, sleep_time=sleep_time/2, times = 3)
        click_once(ex[0], ex[1], device=device, sleep_time=sleep_time*2)
    
    # 点赞下方的庙宇
    move_to_bottom(device = device)
    for pos in cai_shen_miao["lows"]:
        click_once(pos[0], pos[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_pu[0], cai_shen_pu[1], device=device, sleep_time=sleep_time*2)
        click_once(cai_shen_like[0], cai_shen_like[1], device=device, sleep_time=sleep_time*2)
        click_painless(device=device, sleep_time=sleep_time/2, times = 3)
        click_once(ex[0], ex[1], device=device, sleep_time=sleep_time*2)
    
    # 第二次点大赞，有时候第一次点不到
    time.sleep(sleep_time)
    clicks(big_like[0], big_like[1], device=device, sleep_time=sleep_time, times = 3)
    click_exit(device = device, sleep_time = sleep_time*2, times = 3)
    
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    print("daily_cai_shen_miao_like ends")

def daily_ling_qu_yu_gan(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_ling_qu_yu_gan 领取鱼竿")
    # 领取鱼竿
    # 经常领取不到，多做几次
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import zhuang_yuan
    
    enter_home(device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*3)
    entry = zhuang_yuan["entry"]
    click_once(entry[0], entry[1], device=device, sleep_time=sleep_time*4)
    move_to_left()
    move_x, move_y = zhuang_yuan["drag_to_yu_gan"]
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    drag_and_move(move_x=move_x/3, move_y=move_y, start_x=500, start_y=500, device=device, duration_ms=500)
    
    yu_x, yu_y = zhuang_yuan["yu_gan"]
    for _ in range(2):
        for i in range(-5, 5, 1):
            # often has x axis random bias
            clicks(yu_x + i * 20, yu_y, device=device, sleep_time=sleep_time*0.1, times=4)
        click_painless(device=device, sleep_time=sleep_time, times=2)
    x, y = zhuang_yuan["shou_huo"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    x, y = zhuang_yuan["shou_huo_confirm"]
    click_once(x, y, device=device, sleep_time=sleep_time)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    enter_home(device=device, sleep_time=sleep_time)
    if debugging:
        print("daily_ling_qu_yu_gan 领取鱼竿 end")

def daily_xing_shan(device = local_device, sleep_time = 1):
    if debugging:
        print("daily_xing_shan begin")
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import xing_shan
    enter_home  (device=device, sleep_time=sleep_time)
    enter_cheng_jiao(device=device, sleep_time=sleep_time*2)
    mv_x, mv_y = xing_shan["drag"]
    drag_and_move(mv_x, mv_y, start_x=1000, start_y=500, device=device, duration_ms=500)
    entry_x, entry_y = xing_shan["entry"]
    click_once(entry_x, entry_y, device=device, sleep_time=sleep_time*3)
    
    do = xing_shan["do"]
    one_click = xing_shan["one_click"]
    # 预期行善次数 max tiems + 15 + 10
    for _ in range(2):
        click_painless(device=device, sleep_time=sleep_time, times=3)
        click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time/3)
        for _ in range(25):
            click_once(do[0], do[1], device=device, sleep_time=sleep_time)
            click_painless(device=device, sleep_time=sleep_time/4, times=4)
    
    confirm = xing_shan["confirm"]
    for _ in range(2):
        click_once(do[0], do[1], device=device, sleep_time=sleep_time)
        click_once(confirm[0], confirm[1], device=device, sleep_time=sleep_time)
        click_painless(device=device, sleep_time=sleep_time, times=2)
        click_once(one_click[0], one_click[1], device=device, sleep_time=sleep_time/3)
    click_painless(device=device, sleep_time=sleep_time, times=2)
    
    enter_home(device=device, sleep_time=sleep_time)   
    if debugging:
        print("daily_xing_shan end")

def xiang_mu_zhao_shang(device = local_device, sleep_time = 1):
    if debugging:
        print("xiang_mu_zhao_shang begins")
    # 进入城郊 -> 进入 招商 -> 进入项目招商 -> 点击项目榜单 
    from ADB_project.resources_1080_1920.cheng_jiao.cheng_jiao_data import zhao_shang
    enter_home(device = device, sleep_time = sleep_time)
    enter_cheng_jiao(device = device, sleep_time = sleep_time)
    entry = zhao_shang["entry"]
    proj_entry = zhao_shang["proj_entry"]
    proj_bang = zhao_shang["proj_bang"]
    empty_toggle = zhao_shang["empty_toggle"]
    click_once(entry[0], entry[1], device = device, sleep_time = sleep_time)
    click_once(proj_entry[0], proj_entry[1], device = device, sleep_time = sleep_time)
    click_once(proj_bang[0], proj_bang[1], device = device, sleep_time = sleep_time)
    click_once(empty_toggle[0], empty_toggle[1], device = device, sleep_time = sleep_time)
    move_y = zhao_shang["move_y"]
    drag_and_move(0, move_y, device = device, duration_ms = 500)
    
    # 进入一个项目
    dy, y_range = zhao_shang["y_scan_step_range"]
    
    top_entry = zhao_shang["top_entry"]
    x, tmp_y = top_entry
    for i in range(int(y_range/dy)):
        click_once(x, tmp_y,device = device, sleep_time = sleep_time/2)
        tmp_y += dy
    
    xy00 = zhao_shang["xy00"]
    d_xy = zhao_shang["d_xy"]
    x, y = xy00
    for i in range(2):
        y = xy00[1] + i * d_xy[1]
        for j in range(2):
            x = xy00[0] + j * d_xy[0]
            print(f"x,y: {x,y}")
            clicks(x,y, device = device, sleep_time = sleep_time, times = 1)
            click_painless(device=device, sleep_time = sleep_time)
    exit_times = zhao_shang["exit_times"]
    click_exit(device = device, sleep_time = sleep_time, times = exit_times)
    
    # back home
    enter_home(device=device, sleep_time=sleep_time)
    
    if debugging:
        print("xiang_mu_zhao_shang ends")
