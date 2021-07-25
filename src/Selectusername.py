from tkinter import *

#UserList = [{'bref_id': '36316500223550', 'name': 'Shamima Khanam', 'vaccine': 'COVAXIN', 'age': 58, 'status': 'Vaccinated'}, {'bref_id': '83694130405200', 'name': 'Shahida Khanam', 'vaccine': 'COVAXIN', 'age': 29, 'status': 'Partially Vaccinated'}, {'bref_id': '97934304297270', 'name': 'Ayesha Ayubi Khanam', 'vaccine': 'COVAXIN', 'age': 28, 'status': 'Vaccinated'}]
l = [] 
class SelectUsername(object):
    def __init__(self,parent,UserList):
        self.UserList = UserList
        self.window = parent
        self.window.title("List of benefeciaries")
        self.frame = Frame(parent)
        self.frame.pack()
        self.varList = []
        self.varList.append(IntVar())
        self.i = 0
        for u in UserList:
            self.user = u
            self.varList.append(IntVar())
            t = u['name'] + '\t' + u['vaccine'] + '\t' + str(u['age'])+' years' + '\t' + u['status']
            Checkbutton(self.frame,text=t,variable=self.varList[self.i],onvalue=True,offvalue=False,command=self.select).pack(anchor=W)
            self.i+=1
        self.next = Button(self.frame,text='Next',fg='blue',command=self.onNextclick)
        self.next.pack()
    def select(self):
        print(self.user)
        for j in range(0,len(self.UserList)):
            if(self.varList[j].get()) and j not in l:
                l.append(j)
                l.sort()
        print(l)

    def onNextclick(self):
        with open('beneficiary.txt','w') as file:
            for x in l:
                file.write(str(x)+',')
        print("Next Clicked")
        self.window.destroy()


#if __name__=="__main__":
def selectUser(UserList):
    window = Tk()
    window.geometry("600x300")
    SelectUsername(window,UserList=UserList)
    window.mainloop()