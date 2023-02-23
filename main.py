from adb import ADB_Util
from screenrec import SR_Util
import config
import time

ADB_Util.getScreenSize()

def CurrentStringRecAndTap(str_to_tap, offset = [0, 0], which = 0):
    str_coord = []
    for time in range(0, 5):
        ADB_Util.getScreenshot(config.SCREENSHOT_PATH)
        str_coord = SR_Util.getStringCoord(config.SCREENSHOT_PATH, str_to_tap)
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
        ADB_Util.getScreenshot(config.SCREENSHOT_PATH)
        str_coord = SR_Util.getStringCoord(config.SCREENSHOT_PATH, str_to_tap)
        str_near_coord = SR_Util.getStringCoord(config.SCREENSHOT_PATH, str_near)
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
        ADB_Util.getScreenshot(config.SCREENSHOT_PATH)
        image_coord = SR_Util.getSubImageCoord(config.SCREENSHOT_PATH, sub_image_path, 0.8)
        if not image_coord:
            print("Can not find circle icon in current screen. Restarting...[" + str(time)+"]")
            continue
        ADB_Util.tap(image_coord[0])
        return image_coord[0]
    else:
        return image_coord

def CurrentHasString(string):
    ADB_Util.getScreenshot(config.SCREENSHOT_PATH)
    if SR_Util.getStringCoord(config.SCREENSHOT_PATH, string) :
        return True
    return False

def CurrentTapAnswer():
    result = SR_Util.getScreenshotandRead(config.SCREENSHOT_PATH)
    isSingleChoice = SR_Util.isSingleChoice(config.SCREENSHOT_PATH)
    answer = SR_Util.getAnswer(config.SCREENSHOT_PATH, result)

    if isSingleChoice:
        str_coord = SR_Util.getStringCoord(config.SCREENSHOT_PATH, answer)
        str_center = SR_Util.getCenter(str_coord[0][0])
        ADB_Util.tap(str_center)
    else:
        square_coord = SR_Util.getSubImageCoord(config.SCREENSHOT_PATH, config.SQUARE_PATH, 0.8)
        choices = [[0, 0], [0, 0], [0, 0], [0, 0]]
        num_choice = [x for x in result if SR_Util.hasChoice(x[1])]

        sc_ptr = 0
        for i in range(0, len(num_choice)):
            center = SR_Util.getCenter(num_choice[i][0])
            if center[1] + 10 > square_coord[sc_ptr][1]:
                sc_ptr += 1
                choices[int(num_choice[i][1][0]) - 1] = center
            if sc_ptr >= len(square_coord):
                break

        answer = [int(x) for x in answer]
        tmp = [x for x in answer]
        for i in range(0, len(tmp)):
            coord = choices[tmp[i] - 1]
            if(coord != [0, 0]):
                ADB_Util.tap(coord)
                answer.remove(tmp[i])
        while answer:
            ADB_Util.swipeCenterDown()
            result = SR_Util.getScreenshotandRead(config.SCREENSHOT_PATH)
            square_coord = SR_Util.getSubImageCoord(config.SCREENSHOT_PATH, config.SQUARE_PATH, 0.8)
            num_choice = [x for x in result if SR_Util.hasChoice(x[1])]
            
            sc_ptr = 0
            for i in range(0, len(num_choice)):
                center = SR_Util.getCenter(num_choice[i][0])
                if center[1] + 10 > square_coord[sc_ptr][1]:
                    sc_ptr += 1
                    choices[int(num_choice[i][1][0]) - 1] = center
                if sc_ptr >= len(square_coord):
                    break
            
            tmp = [x for x in answer]
            for i in range(0, len(tmp)):
                coord = choices[tmp[i] - 1]
                if(coord != [0, 0]):
                    ADB_Util.tap(coord)
                    answer.remove(tmp[i])

def SignInCCBLife():
    ADB_Util.openCCBLifeApp()
    # time.sleep(2)
    while not CurrentHasString("信用卡") :
        CurrentFirstSubImageRecAndTap(config.X_PATH)
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
    for i in range(0, 4):
        ADB_Util.swipeCenterRight()
    CurrentStringRecAndTap("CNPC", [0, -50])
    CurrentStringRecAndTap("铁人先锋", [0, -10])
    CurrentStringRecAndTap("学习", [0, -10], -1)
    time.sleep(1)
    CurrentStringRecAndTap("在线答题", [0, -10])
    for j in range(0, 3):
        CurrentStringRecAndTapNearOne("立即考试", "月月学")
        CurrentStringRecAndTap("开始答题")
        time.sleep(1)
        for i in range(0, 3):
            CurrentFirstSubImageRecAndTap(config.CIRCLE_PATH2)
            res = CurrentStringRecAndTap("下一题")
            if CurrentHasString("没有下一题了") or not res:
                break
        CurrentStringRecAndTap("我要提交")
        CurrentStringRecAndTap("确认提交")
        while not CurrentHasString("答题") :
            continue
        ADB_Util.inputKeyBack()
    ADB_Util.inputKeyBack()

    CurrentStringRecAndTap("我的")
    for i in range(0, 3):
        while True:
            res = CurrentStringRecAndTap("查看解析")
            if res :
                break
            time.sleep(1)
        CurrentTapAnswer()
        CurrentStringRecAndTap("确认答案")
        if i == 2:
            CurrentStringRecAndTap("完成")
        else:
            CurrentStringRecAndTap("下一题")
    CurrentStringRecAndTap("确定")

    CurrentStringRecAndTap("学习卡")
    CurrentStringRecAndTap("确认收藏")
    ADB_Util.inputKeyBack()
    ADB_Util.backToHome()


# print(dir(ADB_Util))

# SignInCCBLife()
# SignInTRXF()

