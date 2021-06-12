import pdfreader
import PyPDF2
from pdfreader import PDFDocument, SimplePDFViewer
path = '/home/shabs/Desktop/cowin-booking/covidbooking_2/covid-vaccine-booking/src/file.pdf'
# fd = open(path,"rb")
# viewer = SimplePDFViewer(fd)
# print(viewer.prev())
# #print(viewer.metadata)
pdfFileObj = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
pageObj = pdfReader.getPage(0)
print(pageObj.extractText())