from tkinter import *

district = ['Delhi','Mumbai','Kolkata','Chennai']

class checkbox(object):
    def __init__(self,parent):
        self.var1 = IntVar()
        self.var2 = IntVar()
        self.window = parent
        self.window.title("checkbox")
        self.frame = Frame(parent)
        self.frame.pack()
        self.varList = []
        self.varList.append(IntVar())
        #self.varList = [-1 for d in district]
        i = 0
        for d in district:
            self.varList.append(IntVar())
            Checkbutton(self.frame,text = d,variable=self.varList[i], onvalue=1, offvalue=0, command=self.testing).pack()
            i+=1
        
    def testing(self):
        print([self.varList[j].get() for j in range(0,len(district))])
        

if __name__=="__main__":
    window = Tk()
    window.geometry("300x300")
    checkbox(window)
    window.mainloop()
