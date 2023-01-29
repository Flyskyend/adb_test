import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import glob
import easyocr
from PIL import Image,ImageDraw

class SR_Util:
    ocrreader = easyocr.Reader(['ch_sim','en'], gpu=True) # this needs to run only once to load the model into memory

    def getSubImageCoord(image_path, sub_path, threshold):
        print("image_path:", image_path, "sub_path:", sub_path)
        img_rgb = cv.imread(image_path)
        img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
        # template = cv.imread('trxf/icon_circle.jpg', 0)
        template = cv.imread(sub_path, 0)
        w, h = template.shape[::-1]
        res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
        # threshold = 0.4
        loc = np.where( res >= threshold)
        loc = list(zip(*loc[::-1]))
        coords = []
        for i in range(0, len(loc)):
            print((loc[i][0] + w, loc[i][1] + h), end=" ")
            if(i > 0 and loc[i][0] - loc[i-1][0] < w and loc[i][1] - loc[i-1][1] < h):
                print("Delete")
                continue
            else:
                print("")
            coords.append([int(loc[i][0] + w/2), int(loc[i][1] + h/2)])
        #     cv.rectangle(img_rgb, loc[i], (loc[i][0] + w, loc[i][1] + h), (0,0,255), 2)
        # cv.imwrite("res.jpg",img_rgb)
        return coords
    
    def getStringCoord(image_path, str):
        result = SR_Util.ocrreader.readtext(image_path)
        for r in result:
            if str in r[1]:
                print(r)
                return r
        # image=Image.open(image_path)
        # draw = ImageDraw.Draw(image)
        # for i in range(0, len(result)):
        #     draw.polygon([tuple(result[i][0][0]), tuple(result[i][0][1]), tuple(result[i][0][2]), tuple(result[i][0][3])], outline=(255,0,0))
        #     print(i, result[i])
        # # image.show()
        # image.save(image_path.split('/')[1].split('.')[0] + "_res.jpg")
        # print("===========================")
    
    def getCenter(coords):
        x = 0
        y = 0
        for c in coords:
            x += c[0]
            y += c[1]
        x /= len(coords)
        y /= len(coords)
        # print([int(x), int(y)])
        return [int(x), int(y)]
    
    def getAnswer(image_path):
        result = SR_Util.ocrreader.readtext(image_path)
        for i in range(0, len(result)):
            if "正确答案" in result[i][1]:
                answer = result[i][1].split(":")[1].split(" ")[-1]
                if answer[0].isdigit() and answer[1] == "," :
                    answer = answer.split(",")
                print("正确答案: ", answer)
                return answer
        

        
