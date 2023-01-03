import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv.imread('Desktop_1.jpg')
img_gray = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
template = cv.imread('Desktop_folder.jpg',0)
w, h = template.shape[::-1]
res = cv.matchTemplate(img_gray,template,cv.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    print((pt[0] + w, pt[1] + h))
    cv.rectangle(img_rgb, pt, (pt[0] + w + 40, pt[1] + h + 40), (0,0,255), 2)

cv.rectangle(img_rgb, (1280, 720), (1300, 768), (0,0,255), 2)
cv.imwrite('res.png',img_rgb)

