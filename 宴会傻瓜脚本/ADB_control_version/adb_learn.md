# ADB info
Obtain front page running app, package name:
~~~shell
adb shell "dumpsys activity activities | grep mResumedActivity | cut -d "{" -f2 | cut -d ' ' -f3 | cut -d "/" -f1"
~~~

- method2
~~~shell
adb shell
dumpsys window w | grep mCurrent
~~~

# start app based on package name
example package:  com.sqwh5.ys.jwdzg.jwdzgh5_ptzy_ysf37/com.gamesdk.h5.GameActivity
~~~shell
# 启动 dzg
adb shell am start  com.sqwh5.ys.jwdzg.jwdzgh5_ptzy_ysf37/com.gamesdk.h5.GameActivity
~~~~
quick fox:  com.zx.a2_quickfox/com.zx.a2_quickfox.ui.main.activity.MainActivity
~~~shell
# 启动 quick fox
adb shell am start  com.zx.a2_quickfox/com.zx.a2_quickfox.ui.main.activity.MainActivity
~~~

# reference
https://blog.csdn.net/ezconn/article/details/99885715 

