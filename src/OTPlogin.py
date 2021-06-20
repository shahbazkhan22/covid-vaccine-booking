from tkinter import *
from utils import generate_otp

base_request_header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'origin': 'https://selfregistration.cowin.gov.in/',
            'referer': 'https://selfregistration.cowin.gov.in/'
            }
mobile = ''
OTP = 0

class OtpWindow(object):
    def __init__(self,parent):
        self.number = StringVar()
        self.otp = StringVar()
        self.window = parent
        self.window.title("OTP Window")
        self.frame = Frame(parent)
        self.frame.pack()
        self.numberLabel = Label(self.frame, text = '\nEnter the registered mobile number')
        self.numberLabel.place(x = 40, y = 20)
        self.number_entry = Entry(self.frame,textvariable=self.number)
        self.number_entry.place(x = 50,y=50)
        self.number_btn = Button(self.frame, text = 'Get OTP', fg = 'blue', command = self.getOTP)
        self.number_btn.place(x = 20, y = 20)
        self.otpLabel = Label(self.frame, text = '\nEnter the received OTP')
        self.otpLabel.place(x = 40, y = 70)
        self.otp_entry = Entry(self.frame,textvariable=self.otp)
        self.otp_entry.place(x = 50,y=80)
        self.submit_otp_btn = Button(self.frame, text = 'Submit OTP', fg = 'blue', command = self.submitOTP)
        self.submit_otp_btn.place(x = 80, y = 80)
        self.numberLabel.pack()
        self.number_entry.pack()
        self.number_btn.pack()
        self.otpLabel.pack()
        self.otp_entry.pack()
        self.submit_otp_btn.pack() 

    def getOTP(self):
        #self.window.destroy()
        mobile = self.number.get()
        with open('mobile.txt','w') as file:
            file.write(mobile)
        generate_otp(mobile, base_request_header)
        #token = generate_otp(mobile, base_request_header)
    

    def submitOTP(self):
        OTP = self.otp.get()
        print("OTP = ",OTP)
        with open('otp.txt','w') as file:
            file.write(OTP)
        self.window.destroy()    
        print("hello")

def OtpLogin():
    window = Tk()
    window.geometry("300x300")
    OtpWindow(window)
    window.mainloop()
    print(mobile,OTP)

           