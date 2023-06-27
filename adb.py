import os
import re
import time

class ADB_Util:
    # def __init__(self) -> None:
    #     print("adb devices")
    #     os.system("adb.exe devices")
    SCREEN_SIZE = [0,0]
    SCREEN_CENTER_X = 0
    SCREEN_CENTER_Y = 0
    SCREEN_CENTER_SWIPE_LENGTH = 200

    def sendCommand(cmd):
        print("### " + cmd)
        os.system(cmd)

    # 模拟点击(540, 1104)坐标
    def tap(coord):
        x, y = coord
        print("### adb shell input tap " + str(x) +" " + str(y))
        os.system("adb.exe shell input tap " + str(x) +" " + str(y))
    
    # 模拟滑动，从(250,250)滑动到(300,300)
    def swipe(x1, y1, x2, y2):
        print("### adb shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))
        os.system("adb.exe shell input swipe " + str(x1) + " " + str(y1) + " " + str(x2) + " " + str(y2))

    def swipeCenterUp():
        ADB_Util.swipe(ADB_Util.SCREEN_CENTER_X, ADB_Util.SCREEN_CENTER_Y + ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_X, ADB_Util.SCREEN_CENTER_Y-ADB_Util.SCREEN_CENTER_SWIPE_LENGTH)    

    def swipeCenterDown():
        ADB_Util.swipe(ADB_Util.SCREEN_CENTER_X, ADB_Util.SCREEN_CENTER_Y - ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_X, ADB_Util.SCREEN_CENTER_Y + ADB_Util.SCREEN_CENTER_SWIPE_LENGTH)

    def swipeCenterLeft():
        ADB_Util.swipe(ADB_Util.SCREEN_CENTER_X + ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_Y, ADB_Util.SCREEN_CENTER_X - ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_Y)
        
    def swipeCenterRight():
        ADB_Util.swipe(ADB_Util.SCREEN_CENTER_X - ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_Y, ADB_Util.SCREEN_CENTER_X + ADB_Util.SCREEN_CENTER_SWIPE_LENGTH, ADB_Util.SCREEN_CENTER_Y)

    # screenshot & download
    def getScreenshot(path="./screenshot.jpg"):
        time.sleep(2)
        print("### adb pull /sdcard/screenshot.jpg " + path)
        os.system("adb.exe shell /system/bin/screencap -p /sdcard/screenshot.jpg")
        os.system("adb.exe pull /sdcard/screenshot.jpg " + path)

    # 获取屏幕分辨率
    def getScreenSize():
        print("### adb shell wm size")
        ret = os.popen("adb.exe shell wm size").read()
        if not ret:
            return False
        ADB_Util.SCREEN_SIZE = [ int(x) for x in re.findall(r": (.*)x(.*)\n", ret)[0]]
        ADB_Util.SCREEN_CENTER_X = int(ADB_Util.SCREEN_SIZE[0]/2)
        ADB_Util.SCREEN_CENTER_Y = int(ADB_Util.SCREEN_SIZE[1]/2)
        print("Screen Size:", ADB_Util.SCREEN_SIZE[0], "x", ADB_Util.SCREEN_SIZE[1], ", Center: (", ADB_Util.SCREEN_CENTER_X, ",", ADB_Util.SCREEN_CENTER_Y, ")")
        return True


    # def openApp():
    #     print("### adb shell am start -W -n com.richfit.qixin.partybuild.product/com.richfit.partybuild.activity.PBMainActivity")
    #     os.system("adb shell am start -W -n com.richfit.qixin.partybuild.product/com.richfit.partybuild.activity.PBMainActivity")

    def openCCBLifeApp():
        print("### adb shell am start -W -n com.ccb.longjiLife/com.ccb.longjiLife.MainActivity")
        os.system("adb.exe shell am start -W -n com.ccb.longjiLife/com.ccb.longjiLife.MainActivity")
        
    def backToHome():
        print("### adb shell am start -W -n com.miui.home/com.miui.home.launcher.Launcher")
        os.system("adb.exe shell am start -W -n com.miui.home/com.miui.home.launcher.Launcher")

    def inputKeyBack():
        print("### adb shell input keyevent KEYCODE_BACK")
        os.system("adb.exe shell input keyevent KEYCODE_BACK")
    

# screenshot_path = "./screenshot.jpg"
# ADB_Util.tap([540, 1104])
# ADB_Util.getScreenshot(screenshot_path)
# util = ADB_Util()


# exit()

# adb shell "dumpsys window | grep mCurrentFocus"

# adb shell am start -W -n com.richfit.qixin.partybuild.product/com.richfit.partybuild.activity.PBMainActivity
# adb shell am force-stop com.richfit.qixin.partybuild.product/com.richfit.partybuild.activity.PBMainActivity

# adb tcpip 5555
# adb connect <device-ip-address>

# #模拟输入“001”
# adb shell input text "001"

# #模拟home按键
# adb shell input keyevent 3

# #模拟点击(540, 1104)坐标
# adb shell input tap 540 1104

# #模拟滑动，从(250,250)滑动到(300,300)
# adb shell input swipe 250 250 300 300

# KEYCODE_UNKNOWN=0;
# KEYCODE_SOFT_LEFT=1;
# KEYCODE_SOFT_RIGHT=2;
# KEYCODE_HOME=3;     //home键
# KEYCODE_BACK=4;     //back键
# KEYCODE_CALL=5;
# KEYCODE_ENDCALL=6;
# KEYCODE_0=7;
# KEYCODE_1=8;
# KEYCODE_2=9;
# KEYCODE_3=10;
# KEYCODE_4=11;
# KEYCODE_5=12;
# KEYCODE_6=13;
# KEYCODE_7=14;
# KEYCODE_8=15;
# KEYCODE_9=16;
# KEYCODE_STAR=17;
# KEYCODE_POUND=18;
# KEYCODE_DPAD_UP=19;
# KEYCODE_DPAD_DOWN=20;
# KEYCODE_DPAD_LEFT=21;
# KEYCODE_DPAD_RIGHT=22;
# KEYCODE_DPAD_CENTER=23;
# KEYCODE_VOLUME_UP=24;
# KEYCODE_VOLUME_DOWN=25;
# KEYCODE_POWER=26;
# KEYCODE_CAMERA=27;
# KEYCODE_CLEAR=28;
# KEYCODE_A=29;
# KEYCODE_B=30;
# KEYCODE_C=31;
# KEYCODE_D=32;
# KEYCODE_E=33;
# KEYCODE_F=34;
# KEYCODE_G=35;
# KEYCODE_H=36;
# KEYCODE_I=37;
# KEYCODE_J=38;
# KEYCODE_K=39;
# KEYCODE_L=40;
# KEYCODE_M=41;
# KEYCODE_N=42;
# KEYCODE_O=43;
# KEYCODE_P=44;
# KEYCODE_Q=45;
# KEYCODE_R=46;
# KEYCODE_S=47;
# KEYCODE_T=48;
# KEYCODE_U=49;
# KEYCODE_V=50;
# KEYCODE_W=51;
# KEYCODE_X=52;
# KEYCODE_Y=53;
# KEYCODE_Z=54;
# KEYCODE_COMMA=55;
# KEYCODE_PERIOD=56;
# KEYCODE_ALT_LEFT=57;
# KEYCODE_ALT_RIGHT=58;
# KEYCODE_SHIFT_LEFT=59;
# KEYCODE_SHIFT_RIGHT=60;
# KEYCODE_TAB=61;
# KEYCODE_SPACE=62;
# KEYCODE_SYM=63;
# KEYCODE_EXPLORER=64;
# KEYCODE_ENVELOPE=65;
# KEYCODE_ENTER=66;
# KEYCODE_DEL=67;
# KEYCODE_GRAVE=68;
# KEYCODE_MINUS=69;
# KEYCODE_EQUALS=70;
# KEYCODE_LEFT_BRACKET=71;
# KEYCODE_RIGHT_BRACKET=72;
# KEYCODE_BACKSLASH=73;
# KEYCODE_SEMICOLON=74;
# KEYCODE_APOSTROPHE=75;
# KEYCODE_SLASH=76;
# KEYCODE_AT=77;
# KEYCODE_NUM=78;
# KEYCODE_HEADSETHOOK=79;
# KEYCODE_FOCUS=80;//*Camera*focus
# KEYCODE_PLUS=81;
# KEYCODE_MENU=82;
# KEYCODE_NOTIFICATION=83;
# KEYCODE_SEARCH=84;
# KEYCODE_MEDIA_PLAY_PAUSE=85;
# KEYCODE_MEDIA_STOP=86;
# KEYCODE_MEDIA_NEXT=87;
# KEYCODE_MEDIA_PREVIOUS=88;
# KEYCODE_MEDIA_REWIND=89;
# KEYCODE_MEDIA_FAST_FORWARD=90;
# KEYCODE_MUTE=91;
