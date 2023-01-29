from adb import ADB_Util
from screenrec import SR_Util
import time

def CurrentStringRecAndTap(str):
    ADB_Util.getScreenshot("./screenshot.jpg")
    str_coord = []
    str_coord = SR_Util.getStringCoord("./screenshot.jpg", str)
    if not str_coord:
        print("Can not find", str, "in current screen.")
        return
    coord = SR_Util.getCenter(str_coord[0])
    ADB_Util.tap(coord[0], coord[1])

def SignInCCBLife():
    ADB_Util.openCCBLifeApp()
    ADB_Util.swipe(540, 1500, 540, 600)
    time.sleep(1)
    CurrentStringRecAndTap("签到")
    time.sleep(2)
    CurrentStringRecAndTap("立即签到")

def CurrentTapAnswer():
    ADB_Util.getScreenshot("./screenshot.jpg")
    img_crood = SR_Util.getSubImageCoord("./screenshot.jpg", "./trxf/icon_circle.jpg", 0.8)
    answer = SR_Util.getAnswer("./screenshot.jpg")
    str_coord = SR_Util.getStringCoord("./screenshot.jpg", answer)
    str_center = SR_Util.getCenter(str_coord[0])
    answer_coord = img_crood[0]
    for c in img_crood:
        if abs(answer_coord[1] - str_center[1]) > abs(c[1] - str_center[1]):
            answer_coord = c
    ADB_Util.tap(answer_coord[0], answer_coord[1])

# print(dir(ADB_Util))

# CurrentStringRecAndTap("我的")

for i in range(0, 3):
    CurrentStringRecAndTap("查看解析")
    CurrentTapAnswer()
    CurrentStringRecAndTap("确认答案")
    CurrentStringRecAndTap("下一题")
