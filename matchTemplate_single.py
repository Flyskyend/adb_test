import matplotlib.pyplot as plt
import numpy as np
import cv2

img = cv2.imread("Desktop_1.jpg",cv2.IMREAD_COLOR)
img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
tampalet = cv2.imread("Desktop_ggd.jpg",cv2.IMREAD_COLOR)
tampalet = cv2.cvtColor(tampalet,cv2.COLOR_RGB2GRAY)
print(tampalet.shape)
h,w = tampalet.shape
print((w,h))
cv2.imshow("lena",img)
cv2.imshow("img_tamp",tampalet)
tampalets = ['cv2.TM_SQDIFF','cv2.TM_CCORR','cv2.TM_CCOEFF','cv2.TM_SQDIFF_NORMED','cv2.TM_CCORR_NORMED','cv2.TM_CCOEFF_NORMED']
for meth in tampalets:
    img2 = img.copy()
    method = eval(meth)
    res = cv2.matchTemplate(img,tampalet,method)
    min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(res)
    if method in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else :
        top_left = max_loc
    bottom_right = (top_left[0]+w, top_left[1]+h)

    cv2.rectangle(img2,top_left,bottom_right,255,2)
    plt.subplot(121),plt.imshow(res,cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(img2,cmap='gray')
    plt.xticks([]),plt.yticks([])
    plt.suptitle(meth)
    plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
