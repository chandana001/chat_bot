from tkinter import *
# tkinter library is used  for gui in python
root=Tk()

# root is  the object of main window


def send():
    send="you->"+e.get()
    txt.insert(END,"YOu->"+send)
    

    user=e.get().lower()
    if user=="hello":
        txt.insert(END,"Bot->hiiii,How can I help you Enter the appropriate NUmber \n 1.Quick Transfer via Account Number\n 2.Quick Transfer via Mobile Number & MMID\n3.Transfer to Own account 4.Transfer to SBI Account of others \n 5.Transfer to Other Banks Accounts\n 6.Pay Utility Bill \n 7.Send/Receive using UPI/VPA/contacts\n 8.Scan QR and Make Payment \n 9.Payment to Phonebook Contacts \n 10.Contribute to Existing NPS Account")
    elif user=="1":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONOAPP' tab >>Click on 'Quick Transfer'>>Put your Profile password>>Select via Account>>Select other bank Account/SBI Account ")
    elif user=="2":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONOAPP' tab >>Click on 'Quick Transfer'>>Put your Profile password>>Select via Mobile >>Select other bank Account/SBI Account")
    elif user=="3":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click own SBI Account")
    elif user=="4":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click other SBI Account")
    elif user=="5":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click on pay a new Beneficiary>>Put your profile password>>Select via Account>>Select other bank Account/SBI Account")
    elif user=="6":
        txt.insert(END,"\n Bot->Login in app>>click on 'YONO PAY' tab >>Quick Payments>>Select Prepaid mobile/SBI credit card/DTH RECHARGE/BILL PAY>>Pay and register")
    elif user=="7":
        txt.insert(END,"\n Bot->This feature coming soon")
    e.delete(0, END)


root.title("Chatbot")
# setting the name for window
txt=Text(root)
# object if we need to place any text on screen
txt.grid(row=0,column=0)
#We are specifying the place for the text
e=Entry(root,width=100)
#the object for taking the input from the user
e.grid(row=1,column=0)
send=Button(root,text="Send",command=send).grid(row=1,column=1)
root.mainloop()

################################################## You have to start by saying hello#########################################################################################################################################