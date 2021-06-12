import pytesseract
import cv2
from PIL import Image, ImageEnhance, ImageFilter
path = '/home/shabs/Desktop/cowin-booking/covidbooking_2/covid-vaccine-booking/src/captcha_1.png'

im = Image.open(path) # the second one 
im = im.filter(ImageFilter.MedianFilter())
im.show()
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.show()
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)

