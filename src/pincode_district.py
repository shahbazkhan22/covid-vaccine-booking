from tkinter import *

value = []

class SelectChoice(object):
    def __init__(self,parent):
        self.window = parent
        self.window.title('Pincode-Distrcit Choice')
        self.frame = Frame(parent)
        self.frame.pack()
        #self.value = 0
        self.choiceP = IntVar()
        self.choiceD = IntVar()
        self.choiceLabel = Label(self.frame,text='Select any one searching type')
        self.choiceLabel.pack()
        self.choiceEntryP = Checkbutton(self.frame,text='Search by Pincode',variable=self.choiceP,onvalue=True,offvalue=False)
        self.choiceEntryP.pack()
        self.choiceEntryD = Checkbutton(self.frame,text='Search by District',variable=self.choiceD,onvalue=True,offvalue=False)
        self.choiceEntryD.pack()
        self.nextBtn = Button(self.frame,text='Next',fg='blue',command=self.onNextClick)
        self.nextBtn.pack()

    def onNextClick(self):
        if (self.choiceD.get() and self.choiceP.get()):
            print('Invalid Entry')
        else:
            if(self.choiceD.get()):
                print('District')
                value.append('2')
            if(self.choiceP.get()):
                print('Pincode') 
                value .append('1')
            self.window.destroy()

    def returnValue(self):
        #print(value.pop())
        return value.pop()


#if __name__=="__main__":
def selectPinDis():
    window = Tk()
    window.geometry("300x200")
    obj = SelectChoice(window)
    window.mainloop()
    print(SelectChoice.returnValue(obj))
    #print(value)