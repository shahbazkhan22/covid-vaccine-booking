from tkinter import *

class feeSelect(object):
    def __init__(self,parent):
        self.window = parent
        self.frame = Frame(parent)
        self.frame.pack()
        Label(text='Select the fee prefrence').pack()
        self.free = IntVar()
        self.paid = IntVar()
        self.any = IntVar()
        Checkbutton(text='Free',variable=self.free,onvalue=True,offvalue=False).pack()
        Checkbutton(text='Paid',variable=self.paid,onvalue=True,offvalue=False).pack()
        Checkbutton(text='No Prefrence',variable=self.any,onvalue=True,offvalue=False).pack()
        Button(text='Next',command=self.feeSelection).pack()
    
    def feeSelection(self):
        if self.free.get():
            self.prefrence = ['Free']
        if self.paid.get():
            self.prefrence = ['Paid']
        if self.any.get():
            self.prefrence = ['Free', 'Paid']
        self.window.destroy()

    def returnValue(self):
        return self.prefrence

    
def fee_prefrence():
    window = Tk()
    window.geometry("200x150")
    window.title('Fee selection')
    f_obj = feeSelect(window)
    window.mainloop()
    return f_obj.returnValue()
