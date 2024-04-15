# script description
1. 识别图片
2. 点击识别图片的位置 或 点击固定位置
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
1. 需提供小程序的 link file path
2. 根据 2k 分辨率 100% windows 屏幕比例，以及全屏小程序状态制作 （非全屏，但高度相同，貌似也可）

# current features
1. function implemented: 
    - 财神庙全部点赞
    - 公屏打字
    - 跳转到跨服活动
    - bai-fi 宴会点击
    - 财神送礼点击
    - 宴会邀请点击
    - 寻找宴会入口，点击箱子，点击下一场，退出到主页

# future features
1. 获取局部亮度，辅助检测当前页面状态
2. 优化脚本，分开定义和执行部分
3. 优化 logging 的信息
4. 根据绝对时间来设置检测规则
5. 存储当天状态，某些内容只执行有限次数
    - 商战-3次 2-小时
    - 打龙-1次 8-9点
    - 狩猎 1次 12-14点
    - 蛐蛐 1/3 次
    - 建设 4 次 30 分钟
    - 自动购买商品 1 次
    - 医馆 。。。
6. 优化识别方式，当前识别方式准确率较低，容易误识别
7. 游戏分辨率识别 以及 比例？
    - 感觉比较困难，更改量大

# 期望逻辑 （部分实现）
需要扩大这部分的状态 （脚本启动，进入游戏，打龙，狩猎，。。。）
1. 状态 machine：
    - 主页
    - 跨服宴会邀请
        - 跨服宴中
        -跨服盛会主页
    - 财神送礼
    - 游戏进入（点击 进入游戏）

# 位置数据 (Not up to date)
2560x1440 100% resolution
需要考虑是否包含了 header，这里没统一，请参考resources中的素材尺寸
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
| details | in | code |
| many | wrong | here |
