from tkinter import *

class GetPincode(object):
    def __init__(self,parent):
        self.window = parent
        self.frame = Frame(parent)
        self.frame.pack()
        Label(self.frame,text='Enter Space separated Pincodes').pack()
        self.text = Text(self.frame,height=3,width = 25)
        self.text.pack()
        Button(self.frame,text='Next',command=self.onNextClick).pack()

    def onNextClick(self):
        self.var = self.text.get("1.0", "end-1c")
        self.window.destroy()

    def returnValue(self):
        #return self.var.split(' ')
        return list(filter(None, self.var.split(' ')))
    
def getPincodes():
    window = Tk()
    window.geometry("300x200")
    window.title('Pincode')
    obj1 = GetPincode(window)
    window.mainloop()
    return obj1.returnValue()