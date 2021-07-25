from tkinter import *
from tkcalendar import Calendar
from datetime import datetime

class datePicking(object):
    def __init__(self,parent):
        self.window = parent
        self.frame = Frame(parent)
        self.frame.pack()
        d = str(datetime.now()).split(' ')[0].split('-')
        self.cal = Calendar(self.frame,selectmode='day',year=int(d[0]),month=int(d[1]),day=int(d[2]))
        self.cal.pack()
        Button(self.frame,text='Next',command=self.dateSelect).pack()
    
    def dateSelect(self):
        s = self.cal.get_date().replace('/','-')
        self.s = s[:6]+'20'+s[6:]
        self.window.destroy()
    
    def returnValue(self):
        return self.s


#if __name__=="__main__":
def date():
    window = Tk()
    window.geometry("300x300")
    window.title("Date picking")
    d_obj = datePicking(window)
    window.mainloop()
    return(d_obj.returnValue())
