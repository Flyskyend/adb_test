from adb import ADB_Util
from screenrec import SR_Util
import time

SCREENSHOT_PATH = "./screenshot.jpg"
CIRCLE_PATH = "./trxf/icon_circle.jpg"
CIRCLE_PATH2 = "./trxf/icon_circle2.jpg"
SQUARE_PATH = "./trxf/icon_square.jpg"

def CurrentStringRecAndTap(str):
    ADB_Util.getScreenshot(SCREENSHOT_PATH)
    str_coord = []
    str_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, str)
    if not str_coord:
        print("Can not find", str, "in current screen.")
        return str_coord
    coord = SR_Util.getCenter(str_coord[0])
    ADB_Util.tap(coord[0], coord[1])
    return str_coord

def CurrentFirstSubImageRecAndTap(str):
    ADB_Util.getScreenshot(SCREENSHOT_PATH)
    image_coord = []
    image_coord = SR_Util.getSubImageCoord(SCREENSHOT_PATH, str, 0.8)
    if not image_coord:
        print("Can not find circle icon in current screen.")
        return image_coord
    ADB_Util.tap(image_coord[0][0], image_coord[0][1])
    return image_coord[0]

def SignInCCBLife():
    ADB_Util.openCCBLifeApp()
    time.sleep(2)
    res = []
    ADB_Util.swipeCenterUp()
    res = CurrentStringRecAndTap("签到")
    time.sleep(1)
    while not res:
        ADB_Util.swipeCenterDown()
        time.sleep(1)
        ADB_Util.swipeCenterUp()
        time.sleep(1)
        res = CurrentStringRecAndTap("签到")
    time.sleep(2)
    CurrentStringRecAndTap("立即签到")
    CurrentStringRecAndTap("我知道了")
    ADB_Util.backToHome()

def CurrentTapAnswer():
    ADB_Util.getScreenshot(SCREENSHOT_PATH)
    # img_crood = SR_Util.getSubImageCoord(SCREENSHOT_PATH, "./trxf/icon_circle.jpg", 0.8)
    answer = SR_Util.getAnswer(SCREENSHOT_PATH)
    str_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, answer)
    str_center = SR_Util.getCenter(str_coord[0])
    # answer_coord = img_crood[0]
    # for c in img_crood:
        # if abs(answer_coord[1] - str_center[1]) > abs(c[1] - str_center[1]):
            # answer_coord = c
    # ADB_Util.tap(answer_coord[0], answer_coord[1])
    ADB_Util.tap(str_center[0], str_center[1])

def SignInTRXF():
    CurrentStringRecAndTap("我的")
    for i in range(0, 3):
        while True:
            res = CurrentStringRecAndTap("查看解析")
            if res :
                break
            time.sleep(1)
        CurrentTapAnswer()
        CurrentStringRecAndTap("确认答案")
        CurrentStringRecAndTap("下一题")
    
    CurrentStringRecAndTap("开始答题")
    for i in range(0, 2):
        CurrentFirstSubImageRecAndTap(CIRCLE_PATH2)
        CurrentStringRecAndTap("下一题")
    CurrentStringRecAndTap("我要提交")
    CurrentStringRecAndTap("确认提交")
    ADB_Util.inputKeyBack()


# print(dir(ADB_Util))

