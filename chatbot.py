
    






import nltk
from nltk.chat.util import Chat,reflections
set_pairs=[
    ["hello",['hiiii,How can I help you Enter the appropriate NUmber \n 1.Quick Transfer via Account Number\n 2.Quick Transfer via Mobile Number & MMID\n3.Transfer to Own account 4.Transfer to SBI Account of others \n 5.Transfer to Other Banks Accounts\n 6.Pay Utility Bill \n 7.Send/Receive using UPI/VPA/contacts\n 8.Scan QR and Make Payment \n 9.Payment to Phonebook Contacts \n 10.Contribute to Existing NPS Account']],
    ["1",["Login in app>>click on 'YONOAPP' tab >>Click on 'Quick Transfer'>>Put your Profile password>>Select via Account>>Select other bank Account/SBI Account"]],
    
    
    ["2",["Login in app>>click on 'YONOAPP' tab >>Click on 'Quick Transfer'>>Put your Profile password>>Select via Mobile >>Select other bank Account/SBI Account"]],
    ["3",["Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click own SBI Account"]],
    ['4',["Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click other SBI Account"]],
    ["5",["Login in app>>click on 'YONO PAY' tab >>click on 'Bank Account Tab>>Click on pay a new Beneficiary>>Put your profile password>>Select via Account>>Select other bank Account/SBI Account"]],
    ["6",["Login in app>>click on 'YONO PAY' tab >>Quick Payments>>Select Prepaid mobile/SBI credit card/DTH RECHARGE/BILL PAY>>Pay and register"]],
    ["7",["Coming Soon"]]
    
    ]

chat=Chat(set_pairs,reflections)
print(chat.converse())
# You have to start by saying hello