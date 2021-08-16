import smtplib
import tkinter as tk
from tkinter import Label
from tkinter import Entry
from tkinter import Button


root= tk.Tk()
root.title('Send email')
root.geometry("400x400")

def Email ():  
    server = smtplib.SMTP_SSL("SMTP.gmail.com", 465)
    server.login("Ajax091903@gmail.com", "Ajax091903")
    server.sendmail("Ajax091903@gmail.com",
                    eMail.get(),
                    Message.get())
    server.quit()
    Sent = "Your email was succesfully sent to " + eMail.get()
    myLabel2 = Label(root, text=Sent)
    myLabel2.pack(pady=30)


Greet = "Hello Andrew, who are you sending an email to today?"
myLabel1 = Label(root, text=Greet)
myLabel1.pack(pady=10)


eMail = Entry(root, width=50, font=('Helvetica', 25))
eMail.pack(padx=10, pady=15)

Ask_message = "What would you like to say?"
myLabel2 = Label(root, text=Ask_message)
myLabel2.pack(pady=20)

Message = Entry(root, width=50, font=('Helvetica', 12))
Message.pack(padx= 10, pady= 22)

Button = Button(root, text ="Send Email", command=Email)
Button.pack(pady=10)


root.mainloop()