from tkinter import *
from twilio.rest import Client

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text="Sign up at twilio.com").grid(row=0)
        self.account_sid_lb = Label(self, text='Your Twilio Account SID')
        self.account_sid_lb.grid(row=1, sticky=W)

        self.account_sid = Entry(self, width=30, bd=9)
        self.account_sid.grid(row=2, sticky=W)

        self.auth_token_lbl = Label(self, text="AuthToken")
        self.auth_token_lbl.grid(row=3, sticky=W)

        self.auth_token = Entry(self, width=30, bd=9)
        self.auth_token.grid(row=4, sticky=W)

        self.your_number_lb = Label(self, text='Your Twilio Number')
        self.your_number_lb.grid(row=5, sticky=W)

        self.your_number = Entry(self, width=30, bd=9)
        self.your_number.grid(row=6, sticky=W)

        self.no_to_send_lbl = Label(self, text="Recipient Number (must be verified at Twilio)")
        self.no_to_send_lbl.grid(row=7, sticky=W)

        self.no_to_send = Entry(self, width=30, bd=9)
        self.no_to_send.grid(row=8, sticky=W)

        self.message = Text(self)
        self.message.grid(row=9, sticky=W)

        self.send_btn = Button(self, text="Send Message", command=self.send_message)
        self.send_btn.grid(row=10, sticky=W)
    
    def send_message(self):
        sid = str(self.account_sid.get())
        auth_token = str(self.auth_token.get())
        number = str(self.your_number.get())
        recipient = str(self.no_to_send.get())
        message = self.message.get(0.0, END)

        conn = Client(sid, auth_token)

        # send message
        conn.messages.create(body=message, from_=number, to=recipient)

        Label(self, text="Message Sent").grid(row=11)


root = Tk()
app = Application(root)
root.mainloop()




    
    


        




