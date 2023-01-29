import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import glob

# path = 'pubg/pubg_1.jpg'
path = 'trxf/trxf_12.jpg'
for filename in glob.glob(path):
    print('read ', filename)
    img_rgb = cv.imread(filename)
    img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
    template = cv.imread('trxf/icon_circle.jpg', 0)
    # template = cv.imread('pubg/pubg_point_yellow.jpg', 0)
    w, h = template.shape[::-1]
    res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        print((pt[0] + w, pt[1] + h))
        cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # template = cv.imread('trxf/icon_circle.jpg', 0)
    # w, h = template.shape[::-1]
    # res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
    # threshold = 0.8
    # loc = np.where( res >= threshold)
    # for pt in zip(*loc[::-1]):
    #     print((pt[0] + w, pt[1] + h))
    #     cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)

    # cv.rectangle(img_rgb, (1280, 720), (1300, 768), (0,0,255), 2)
    # cv.imwrite(filename.split('\\')[1].split('.')[0] + "_res.jpg",img_rgb)
    cv.imwrite("res.jpg",img_rgb)

