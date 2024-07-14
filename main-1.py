import datetime
# import time
import ezgmail
import pandas as pd
from twilio.rest import Client
# from flask import request
# from flask import Flask, Response

while True:
    customerDataFrame = pd.read_csv("customer-data-1.csv")
    customerNames = customerDataFrame["Customer-name"]
    customerEmails = customerDataFrame["E-mail-ID"]
    customerPhoneNumber = customerDataFrame["Phone-number"]
    customerPaymentAmount = customerDataFrame["Payment-amount"]
    customerDueTime = customerDataFrame["Time"]
    customer1Due = customerDataFrame["1-Due-date"]
    # for i in range(0, 2):
    #     print(i)
    customerName = str(customerNames[0])
    # print(customerName)
    customerNumber = str(customerPhoneNumber[0])
    # print('+{number}'.format(number=customerNumber))
    customerAmount = str(customerPaymentAmount[0])
    customerEmail = str(customerEmails[0])
    dueTime = customerDueTime[0]
    customerDueDate = customer1Due[0]
    # print(dueTime)
    # print(dueTime[1:3])
    # print(dueTime[5:7])
    # print(dueTime[9:11])
    hour = int(dueTime[1:3])
    minute = int(dueTime[5:7])
    seconds = int(dueTime[9:11])

    account_sid = 'ACa07f4ba3c89c491822046b3f3f39f5f3'
    auth_token = '391f2d40f560f7d44f9afd31d9a2d6e3'
    client = Client(account_sid, auth_token)
    body = "Hi Mr.{name}. Your apartment current payment due date is {date} and " \
           "amount is AED{amount}".format(name=customerName, amount=customerAmount, date=customerDueDate)
    currentDateTime = datetime.datetime.now()
    onlyTime = (currentDateTime.hour, currentDateTime.minute, currentDateTime.second)
    onlyDate = (currentDateTime.year, currentDateTime.month, currentDateTime.second)
    if (currentDateTime.hour, currentDateTime.minute, currentDateTime.second) != (hour, minute, seconds):
        continue
    else:
        print("Reached")
        ezgmail.send(customerEmail, subject="Your Apartment payment due reminder!", body=body)
        smsMessage = client.messages.create(
            messaging_service_sid='MG8b91604744a1dbe677db010aa5e5629d',
            body=body,
            to='+{number}'.format(number=customerNumber)
        )
        print(smsMessage.sid)
        whatsAppMessage = client.messages.create(
            body=body,
            from_='whatsapp:+14155238886',
            to='whatsapp:+{number}'.format(number=customerNumber)
        )
        print(whatsAppMessage.sid)
        break
