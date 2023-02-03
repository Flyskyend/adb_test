from adb import ADB_Util
from screenrec import SR_Util
import time

SCREENSHOT_PATH = "./screenshot.jpg"
CIRCLE_PATH = "./icon/icon_circle.jpg"
CIRCLE_PATH2 = "./icon/icon_circle2.jpg"
SQUARE_PATH = "./icon/icon_square.jpg"
X_PATH = "./icon/icon_x.jpg"

ADB_Util.getScreenSize()

def CurrentStringRecAndTap(str_to_tap, offset = [0, 0], which = 0):
    str_coord = []
    for time in range(0, 5):
        ADB_Util.getScreenshot(SCREENSHOT_PATH)
        str_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, str_to_tap)
        if not str_coord:
            print("Can not find", str_to_tap, "in current screen. Restarting...[" + str(time)+"]")
            continue
        coord = SR_Util.getCenter(str_coord[which][0])
        ADB_Util.tap([coord[0] + offset[0], coord[1] + offset[1]])
        return str_coord
    else:
        return str_coord

def CurrentStringRecAndTapNearOne(str_to_tap, str_near, offset = [0, 0]):
    str_coord = []
    for time in range(0, 5):
        ADB_Util.getScreenshot(SCREENSHOT_PATH)
        str_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, str_to_tap)
        str_near_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, str_near)
        if not str_coord:
            print("Can not find", str_to_tap, "in current screen. Restarting...[" + str(time)+"]")
            continue
        if not str_near_coord:
            print("Can not find", str_near, "in current screen. Restarting...[" + str(time)+"]")
            continue
        near_coord = SR_Util.getCenter(str_near_coord[0][0])
        for c in str_coord:
            coord = SR_Util.getCenter(c[0])
            if coord[1] > near_coord[1] :
                break
        ADB_Util.tap([coord[0] + offset[0], coord[1] + offset[1]])
        return str_coord
    else:
        return str_coord

def CurrentFirstSubImageRecAndTap(sub_image_path):
    image_coord = []
    for time in range(0, 5):
        ADB_Util.getScreenshot(SCREENSHOT_PATH)
        image_coord = SR_Util.getSubImageCoord(SCREENSHOT_PATH, sub_image_path, 0.8)
        if not image_coord:
            print("Can not find circle icon in current screen. Restarting...[" + str(time)+"]")
            continue
        ADB_Util.tap(image_coord[0])
        return image_coord[0]
    else:
        return image_coord

def CurrentHasString(string):
    ADB_Util.getScreenshot(SCREENSHOT_PATH)
    if SR_Util.getStringCoord(SCREENSHOT_PATH, string) :
        return True
    return False

def CurrentTapAnswer():
    ADB_Util.getScreenshot(SCREENSHOT_PATH)
    # img_crood = SR_Util.getSubImageCoord(SCREENSHOT_PATH, "./trxf/icon_circle.jpg", 0.8)
    answer = SR_Util.getAnswer(SCREENSHOT_PATH)
    str_coord = SR_Util.getStringCoord(SCREENSHOT_PATH, answer)
    str_center = SR_Util.getCenter(str_coord[0][0])
    # answer_coord = img_crood[0]
    # for c in img_crood:
        # if abs(answer_coord[1] - str_center[1]) > abs(c[1] - str_center[1]):
            # answer_coord = c
    # ADB_Util.tap(answer_coord)
    ADB_Util.tap(str_center)

def SignInCCBLife():
    ADB_Util.openCCBLifeApp()
    # time.sleep(2)
    while not CurrentHasString("信用卡") :
        CurrentFirstSubImageRecAndTap(X_PATH)
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
    ADB_Util.inputKeyBack()
    time.sleep(1)

def SignInTRXF():
    ADB_Util.backToHome()
    ADB_Util.inputKeyBack()

    for i in range(0, 7):
        ADB_Util.swipeCenterLeft()
    for i in range(0, 3):
        ADB_Util.swipeCenterRight()
    CurrentStringRecAndTap("CNPC", [0, -30])
    CurrentStringRecAndTap("铁人先锋", [0, -10])
    CurrentStringRecAndTap("学习", [0, -10], -1)
    CurrentStringRecAndTap("在线答题", [0, -10])
    for j in range(0, 3):
        CurrentStringRecAndTapNearOne("立即考试", "月月学")
        CurrentStringRecAndTap("开始答题")
        time.sleep(1)
        for i in range(0, 3):
            CurrentFirstSubImageRecAndTap(CIRCLE_PATH2)
            CurrentStringRecAndTap("下一题")
            if CurrentHasString("没有下一题了") :
                break
        CurrentStringRecAndTap("我要提交")
        CurrentStringRecAndTap("确认提交")
        while not CurrentHasString("答题") :
            continue
        ADB_Util.inputKeyBack()
    ADB_Util.inputKeyBack()

    # CurrentStringRecAndTap("我的")
    # for i in range(0, 3):
    #     while True:
    #         res = CurrentStringRecAndTap("查看解析")
    #         if res :
    #             break
    #         time.sleep(1)
    #     CurrentTapAnswer()
    #     CurrentStringRecAndTap("确认答案")
    #     CurrentStringRecAndTap("下一题")
    


# print(dir(ADB_Util))

# SignInCCBLife()
SignInTRXF()

