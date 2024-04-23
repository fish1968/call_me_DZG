# ADB info
Obtain front page running app, package name:
~~~shell
adb shell "dumpsys activity activities | grep mResumedActivity | cut -d "{" -f2 | cut -d ' ' -f3 | cut -d "/" -f1"
~~~

# 
