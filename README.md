# Call me DZG

1. [劫镖计算](劫镖计算)

   1. 🌝根据对方的全部挚友数据，以及战斗力推算对方的可能阵容
   2. 🌝根据推测的阵容，安排我方有$P_{pass}$以上通过率的最小战斗力和阵容
   3. 🌗根据对方的数据组，判断对方的组合是那些，大大降低可能的排列数。还需要完成对应的我方出战阵容生成。
   4. 🌑考虑出战的损耗值
   5. 🌑多几个输出，可以按照不同的角度获得不同的阵容（花元宝的数量、战斗力总和值，方差值）

2. [商铺统计](商铺统计)

   1. 🌗根据商铺街的数据分析最适合在哪里招募员工
   2. 🌑根据商铺街的数据分析哪个商店值得庄园增加员工工效
   3. 制作了一张计算商贸平均值的表
3. [宴会傻瓜脚本](宴会傻瓜脚本)
- Python + 小程序 + 图像识别
   1. 参考了 [CSDN文章](https://blog.csdn.net/luoyir1997/article/details/119117168)
   2. 由于没有使用 template matching，实际上如果图标大百分之十可能就识别不出来，对游戏画面分辨率敏感
   3. 是 Python 脚本，不能在 android 模拟器中运行，占用电脑的显示界面和鼠标键盘操作，并不方便
   4. 使用图像识别 + 亮度判断 决定部分情景，大部分为固定任务执行
- Python + ADB + 安卓模拟器
   1. 可以息屏操作
   2. 暂时没有图像处理的部分，按固定操作执行，有错误执行的风险
   3. 分为 daily once （一天只执行一次）和 常驻
   4. 没有使用多线程
   5. 缺少启动项代码，在缺少图像识别的情况下，貌似很难保证能点进来
   6. [1080*1920 素材数据](宴会傻瓜脚本/ADB_control_version/resources_1080_1920)
   7. [utils](宴会傻瓜脚本/ADB_control_version/utils) 有跟据模拟器截图 x,y 转换为 1080 * 1920 下的位置的小工具（x,y 由 snipaste 获取）
