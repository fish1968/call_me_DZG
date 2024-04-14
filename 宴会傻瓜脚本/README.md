# script description
1. 识别图片
2. 点击识别图片的位置
3. 重复上述过程

# set up environment
貌似总会出问题
`conda env create -f environment.yml`
建议 opencv 使用 `pip install opencv-python`
~~~cmd
conda create -n call_me_dzg python=3.10
conda activate call_me_dzg
~~~
install packages in the env
~~~cmd
conda install imageio -y
conda install pywin32 -y
conda install pillow -y
pip install opencv-python -y
~~~
# notes
1. 需提供小程序的链接地址


# 期望逻辑 （未实现）
1. 状态：

    - 主页
        - home
        - 商铺
    - 跨服活动
        - 宴会争霸（百福）
            - 百福中
    - 跨服宴会邀请
        - 跨服宴中
    - 跨服盛会主页
        - 跨服宴中
    - 财神送礼
# 位置数据
|           | 尺寸 1 | 尺寸 2 |
|-----------|--------|--------|
| 小程序分辨率      | 762    | 1404   |
| 小程序头帘分辨率   | 765    | 44     |
| 全屏纯页面分辨率   | 786    | 1395   |
| 主页-跨服活动     | 205    | 213    |
| 主页-home    | 80     | 1323   |
| 宴会-box     | 680    | 200    |
| 宴会-next     | 80     | 1325   |
| 宴会-in       | 639    | 1233   |
| 宴会-exit     | 40     | 33     |
| 百福-entry    | 700    | 680    |
| text-entry    | 480    | 1230   |
| text-input    | 430    | 1210   |
| text-send     | 680    | 1210   |
| 无害乱点      | 350    | 80     |
| 主页商铺      | 200    | 1330   |
| 主页钱庄      | 200    | 500    |
| 小玉 MID         | 750 | 830 | 
| 小玉执行         | 450 | 980 | 
| 小玉执行over         | 400 | 1100 | 
