from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
path = '/home/shabs/Desktop/cowin-booking/covidbooking_2/covid-vaccine-booking/src/'
drawing = svg2rlg(path+'captcha.svg')
print(drawing)
renderPDF.drawToFile(drawing, path+'file.pdf')
#renderPM.drawToFile(drawing, path+"file.png", fmt="PNG")