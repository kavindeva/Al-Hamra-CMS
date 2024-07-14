# import json
import re
import boto3
import pandas as pd
import datetime
from flask import request
from flask import Flask, Response
from twilio.twiml.messaging_response import MessagingResponse

# Initialize our application
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'images/'


@app.route("/")
def index():
    return "Hello, World!"


@app.route("/whatsapp/", methods=['POST', 'GET'])
def whatsapp_upload():
    response = MessagingResponse()
    if request.method == 'POST':
        if request.form:
            userNewResponse = ["hi", "hello", "hi al-hamra", "hello al-hamra"]
            userFinalRespose = ["thanks", "thank you", "that's all", "good", "fine", "great", "okay", "ok"]
            print("received data from whatsapp")
            print(request.form)
            msg = request.form.get('Body')
            print(type(msg))
            print(msg)
            ProfileName = request.form.get("ProfileName")
            WaID = request.form.get("WaId")
            waid = int(WaID)
            print(WaID)
            PersonNumber = request.form.get("From")
            senderNumber = request.form.get("To")
            print(senderNumber)
            print(type(msg))
            customerDataFrame = pd.read_csv("customer-data.csv")
            # customerNames = customerDataFrame["Customer-name"]
            customer1Due = customerDataFrame["1-Due-date"]
            customer2Due = customerDataFrame["2-Due-date"]
            customer3Due = customerDataFrame["3-Due-date"]
            # customerPhoneNumber = customerDataFrame["Phone-number"]
            customerPaymentAmount = customerDataFrame["Payment-amount"]
            # allCustomerNumbers = list(customerPhoneNumber)
            customerIndexValue = customerDataFrame[customerDataFrame["Phone-number"] == waid].index.values
            print(int(customerIndexValue))
            translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)

            # comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
            # detectedLanguage = comprehend.detect_dominant_language(Text=msg)
            # languageCode = detectedLanguage["Languages"][0]["LanguageCode"]

            def rule_process(querymessage):
                if querymessage.lower() in userNewResponse:
                    print("Greeting matched")
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    replyData = data
                elif querymessage == "1":
                    print("second loop")
                    customerAmount = customerPaymentAmount[int(customerIndexValue)]
                    print(customerAmount)
                    data = "Your due amount is AED{amount}".format(amount=customerAmount)
                    replyData = data
                elif querymessage == "2":
                    print("third loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    data = "Your next payment due date is {date1}".format(date1=date1)
                    replyData = data
                elif querymessage == "3":
                    print("fourth loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    date2 = customer2Due[int(customerIndexValue)]
                    date3 = customer3Due[int(customerIndexValue)]
                    data = "Your first due date is {date1}\nSecond due date is {date2}\nThird due date is {date3}" \
                        .format(date1=date1, date2=date2, date3=date3)
                    replyData = data
                elif querymessage == "4":
                    print("fifth loop")
                    data = "Here is your payment link please click it.\nhttps://alhamra.ae/"
                    replyData = data
                elif querymessage == "5":
                    print("Sixth loop")
                    data = "*Please let me know when would you like to pay*\n1.1 Pay in two days\n1.2 Pay later"
                    replyData = data
                elif querymessage == "1.1":
                    print("Seventh loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    print(date1)
                    print(type(date1))
                    year = int(date1[:4])
                    month = int(date1[5:7])
                    date = int(date1[8:10])
                    day2 = datetime.datetime(year, month, date) + datetime.timedelta(days=2)
                    data = "Dear {name} as per your request you have to pay your due amount before {date2}. " \
                           "Thank you for your response".format(name=ProfileName, date2=day2.date())
                    replyData = data
                elif querymessage == "1.2":
                    print("Seventh loop")
                    data = "Please provide an exact date that you planned to pay your due amount." \
                           "\n*Your date format should be like this(YYYY-MM-DD)"
                    replyData = data
                elif re.match("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}", querymessage.lower()):
                    print("Eighth loop")
                    data = "We accepted your planned paying date. Please don't forget to pay. Thank you for your " \
                           "response and utilizing our Al-hamra bot service."
                    replyData = data
                elif querymessage.lower() in userFinalRespose:
                    print("sixth loop")
                    data = "Thank you for utilizing our Al-hamra bot service. Please feel free to reach us at " \
                           "anytime. Have a great day {name}".format(name=ProfileName)
                    replyData = data
                else:
                    replyData = "Invalid keywords!. Please enter complete valid keywords."
                return replyData

            # if languageCode == "en":
            #     replyData1 = rule_process(msg)
            # else:
            #     queryTranslate = translate.translate_text(Text=msg, SourceLanguageCode=languageCode,
            #                                               TargetLanguageCode="en")
            #     translatedQuery = queryTranslate.get('TranslatedText')
            replyData1 = rule_process(msg)
            result = translate.translate_text(Text=replyData1, SourceLanguageCode="en", TargetLanguageCode="en")
            translatedText = result.get('TranslatedText')
            response.message(body=translatedText, to=PersonNumber, from_=senderNumber)
    return Response(str(response), mimetype="application/xml")


if __name__ == '__main__':
    app.run(debug=True, port=8088)
