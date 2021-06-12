from PIL import Image
import pytesseract
import cv2
import os
import numpy as np
from reportlab.platypus.paragraph import imgNormV

SCREEN_WIDTH = 1366
SCREEN_HEIGHT = 768

path = '/home/shabs/Desktop/cowin-booking/covidbooking_2/covid-vaccine-booking/src/captcha.jpg'

#image = cv2.imread('/home/shabs/Desktop/cowin-booking/covid-vaccine-booking/src/captcha.png',cv2.IMREAD_UNCHANGED)[:,:,-1]
image = cv2.imread(path)
#img = cv2.imread(path,0)
#print(image)


# scale_factor = 6
# scaled_img = cv2.resize(img[10:50, 0:SCREEN_WIDTH], (0,0), fx=scale_factor, fy=scale_factor, interpolation=cv2.INTER_CUBIC)
# assert(scaled_img is not None)
# cv2.imshow("scaled_image",scaled_img)
# thres,thres_img = cv2.threshold(scaled_img, 0, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# assert(thres_img is not None)

# text = pytesseract.image_to_string(thres_img, config='--user-words words.txt config.txt')
# print('Result text: "{}"'.format(text))

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(gray, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
cv2.imshow("Image", img)
text = pytesseract.image_to_string(gray)
#os.remove(filename)
print(text)
# show the output images
# cv2.imshow("Output", thres_img)
cv2.waitKey(0)