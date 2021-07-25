from tkinter import *
#s_list = [{'state': 'Andaman and Nicobar Islands'}, {'state': 'Andhra Pradesh'}, {'state': 'Arunachal Pradesh'}, {'state': 'Assam'}, {'state': 'Bihar'}, {'state': 'Chandigarh'}, {'state': 'Chhattisgarh'}, {'state': 'Dadra and Nagar Haveli'}, {'state': 'Daman and Diu'}, {'state': 'Delhi'}, {'state': 'Goa'}, {'state': 'Gujarat'}, {'state': 'Haryana'}, {'state': 'Himachal Pradesh'}, {'state': 'Jammu and Kashmir'}, {'state': 'Jharkhand'}, {'state': 'Karnataka'}, {'state': 'Kerala'}, {'state': 'Ladakh'}, {'state': 'Lakshadweep'}, {'state': 'Madhya Pradesh'}, {'state': 'Maharashtra'}, {'state': 'Manipur'}, {'state': 'Meghalaya'}, {'state': 'Mizoram'}, {'state': 'Nagaland'}, {'state': 'Odisha'}, {'state': 'Puducherry'}, {'state': 'Punjab'}, {'state': 'Rajasthan'}, {'state': 'Sikkim'}, {'state': 'Tamil Nadu'}, {'state': 'Telangana'}, {'state': 'Tripura'}, {'state': 'Uttar Pradesh'}, {'state': 'Uttarakhand'}, {'state': 'West Bengal'}]
#s_list = []
#selected = 0
class ScrollableFrame(Frame):
    def __init__(self, master, **kwargs):
        Frame.__init__(self, master, **kwargs)

        # create a canvas object and a vertical scrollbar for scrolling it
        self.vscrollbar = Scrollbar(self, orient=VERTICAL)
        self.vscrollbar.pack(side='right', fill="y",  expand="false")
        self.canvas = Canvas(self, bd=0,
                                height=600,
                                highlightthickness=0,
                                yscrollcommand=self.vscrollbar.set)
        self.canvas.pack(side="left", fill="both", expand="true")
        self.vscrollbar.config(command=self.canvas.yview)

        # reset the view
        self.canvas.xview_moveto(0)
        self.canvas.yview_moveto(0)

        # create a frame inside the canvas which will be scrolled with it
        self.interior = Frame(self.canvas, **kwargs)
        self.canvas.create_window(0, 0, window=self.interior, anchor="nw")

        self.bind('<Configure>', self.set_scrollregion)


    def set_scrollregion(self, event=None):
        """ Set the scroll region on the canvas"""
        self.canvas.configure(scrollregion=self.canvas.bbox('all'))

class state(object):
    def __init__(self,parent,s_list):
        self.window = parent
        self.s_list = s_list
        self.window.title('Select State-Distrcit')
        self.frame = Frame(parent)
        self.frame.pack()
        self.checkbox_pane = ScrollableFrame(self.frame)
        self.checkbox_pane.pack(expand="true",fill="both")
        self.x = 0
        self.var = []
        for s in self.s_list:
            self.var.append(IntVar())
            Checkbutton(self.checkbox_pane.interior,text=s['state'],variable=self.var[self.x],onvalue=True,offvalue=False).grid(row=self.x,column=0)
            self.x+=1
        Button(self.checkbox_pane.interior,text="Next",command=self.onNextClick).grid(row=self.x,column=0)

    def onNextClick(self):
        for i in range(0,len(self.s_list)):
            #print(self.var[i].get())
            if(self.var[i].get()):
                self.selected = i+1
                print(i)
                print("state = ",self.s_list[i]['state'])
        self.window.destroy()
    
    def returnValue(self):
        return self.selected

#if __name__ == '__main__':
def state_main(s_list):
    #print(s_list)
    window = Tk()
    window.geometry("600x300")
    s_obj = state(window,s_list=s_list)
    window.mainloop()
    #print("selected = ",selected)
    print("Selected State = ",s_obj.returnValue())
    return s_obj.returnValue()