from tkinter import *

class vaccineSelect(object):
    def __init__(self,parent):
        self.window = parent
        self.frame = Frame(parent)
        self.frame.pack()
        Label(text='Select the Vaccine prefrence').pack()
        self.covaxin = IntVar()
        self.covishield = IntVar()
        self.sputnikV = IntVar()
        Checkbutton(text='Covaxin',variable=self.covaxin,onvalue=True,offvalue=False).pack()
        Checkbutton(text='Covishield',variable=self.covishield,onvalue=True,offvalue=False).pack()
        Checkbutton(text='Sputnik V',variable=self.sputnikV,onvalue=True,offvalue=False).pack()
        Button(text='Next',command=self.feeSelection).pack()
    
    def feeSelection(self):
        if self.covaxin.get():
            self.prefrence = 'COVAXIN'
        if self.covishield.get():
            self.prefrence = 'COVISHIELD'
        if self.sputnikV.get():
            self.prefrence = 'SPUTNIK V'
        self.window.destroy()

    def returnValue(self):
        return self.prefrence

def vaccine_prefrence():
    window = Tk()
    window.geometry("200x150")
    window.title('Fee selection')
    v_obj = vaccineSelect(window)
    window.mainloop()
    return v_obj.returnValue()