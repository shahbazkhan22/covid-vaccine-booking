from tkinter import *
#s_list = [{'district': 'Andaman and Nicobar Islands'}, {'district': 'Andhra Pradesh'}, {'district': 'Arunachal Pradesh'}, {'district': 'Assam'}, {'district': 'Bihar'}, {'district': 'Chandigarh'}, {'district': 'Chhattisgarh'}, {'district': 'Dadra and Nagar Haveli'}, {'district': 'Daman and Diu'}, {'district': 'Delhi'}, {'district': 'Goa'}, {'district': 'Gujarat'}, {'district': 'Haryana'}, {'district': 'Himachal Pradesh'}, {'district': 'Jammu and Kashmir'}, {'district': 'Jharkhand'}, {'district': 'Karnataka'}, {'district': 'Kerala'}, {'district': 'Ladakh'}, {'district': 'Lakshadweep'}, {'district': 'Madhya Pradesh'}, {'district': 'Maharashtra'}, {'district': 'Manipur'}, {'district': 'Meghalaya'}, {'district': 'Mizoram'}, {'district': 'Nagaland'}, {'district': 'Odisha'}, {'district': 'Puducherry'}, {'district': 'Punjab'}, {'district': 'Rajasthan'}, {'district': 'Sikkim'}, {'district': 'Tamil Nadu'}, {'district': 'Telangana'}, {'district': 'Tripura'}, {'district': 'Uttar Pradesh'}, {'district': 'Uttarakhand'}, {'district': 'West Bengal'}]
#s_list = []
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
selected_district = []
class district(object):
    def __init__(self,parent,d_list):
        self.window = parent
        self.d_list = d_list
        self.window.title('Select district')
        self.frame = Frame(parent)
        self.frame.pack()
        self.checkbox_pane = ScrollableFrame(self.frame)
        self.checkbox_pane.pack(expand="true",fill="both")
        self.x = 0
        self.var = []
        for s in self.d_list:
            self.var.append(IntVar())
            Checkbutton(self.checkbox_pane.interior,text=s['district'],variable=self.var[self.x],onvalue=True,offvalue=False).grid(row=self.x,column=0)
            self.x+=1
        Button(self.checkbox_pane.interior,text="Next",command=self.onNextClick).grid(row=self.x,column=0)

    def onNextClick(self):
        for i in range(0,len(self.d_list)):
            #print(self.var[i].get())
            if(self.var[i].get()):
                selected_district.append(i+1)
                print(self.d_list[i]['district'])
        self.window.destroy()



#if __name__ == '__main__':
def district_main(d_list):
    #print(s_list)
    window = Tk()
    window.geometry("600x300")
    district(window,d_list=d_list)
    window.mainloop()
    return selected_district
    print(selected_district)