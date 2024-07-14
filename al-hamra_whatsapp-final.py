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


language_en = "en"
language_ar = "ar"
language_hi = "hi"
language_ru = "ru"
language_ml = "ml"
language_ta = "ta"
preferredLanguage = language_en
# print(preferredLanguage)


@app.route("/whatsapp/", methods=['POST', 'GET'])
def whatsapp_upload():
    response = MessagingResponse()
    if request.method == 'POST':
        if request.form:
            userNewResponse = ["hi", "hello", "hi al-hamra", "hello al-hamra"]
            userFinalResponse = ["thanks", "thank you", "that's all", "good", "fine", "great", "okay", "ok"]
            # print("received data from whatsapp")
            # print(request.form)
            msg = request.form.get('Body')
            # print(type(msg))
            # print(msg)
            ProfileName = request.form.get("ProfileName")
            WaID = request.form.get("WaId")
            waid = int(WaID)
            # print(WaID)
            PersonNumber = request.form.get("From")
            senderNumber = request.form.get("To")
            # print(senderNumber)
            # print(type(msg))
            customerDataFrame = pd.read_csv("customer-data.csv")
            # customerNames = customerDataFrame["Customer-name"]
            customer1Due = customerDataFrame["1-Due-date"]
            customer2Due = customerDataFrame["2-Due-date"]
            customer3Due = customerDataFrame["3-Due-date"]
            # customerPhoneNumber = customerDataFrame["Phone-number"]
            customerPaymentAmount = customerDataFrame["Payment-amount"]
            # allCustomerNumbers = list(customerPhoneNumber)
            customerIndexValue = customerDataFrame[customerDataFrame["Phone-number"] == waid].index.values
            # print(int(customerIndexValue))
            translate = boto3.client(service_name='translate', region_name='us-west-2', use_ssl=True)

            # comprehend = boto3.client(service_name='comprehend', region_name='us-west-2')
            # detectedLanguage = comprehend.detect_dominant_language(Text=msg)
            # languageCode = detectedLanguage["Languages"][0]["LanguageCode"]

            def rule_process(querymessage):
                global preferredLanguage
                if querymessage.lower() in userNewResponse:
                    # print("Greeting matched")
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"which language would you like to prefer to chat.\nA. English\nB. Arabic\n" \
                           f"C. Hindi\nD. Russian\nE. Malayalam\nF. Tamil\n*Note:* If you would like to change " \
                           f"your language preference again means just type 9"
                    replyData = data
                elif querymessage.lower() == "a":
                    # print("second loop")
                    preferredLanguage = "en"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() == "b":
                    # print("1 loop")
                    # global preferredLanguage
                    preferredLanguage = "ar"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() == "c":
                    # print("2 loop")
                    # global preferredLanguage
                    preferredLanguage = "hi"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() == "d":
                    # print("3 loop")
                    # global preferredLanguage
                    preferredLanguage = "ru"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() == "e":
                    # print("4 loop")
                    # global preferredLanguage
                    preferredLanguage = "ml"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service system*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() == "f":
                    # print("5 loop")
                    # global preferredLanguage
                    preferredLanguage = "ta"
                    data = f"*Hi {ProfileName}*\n*Welcome to Al-Hamra payment query service System.*\nLet me know " \
                           f"what kind of informations you needed.\n1. Due amount\n2. Next payment due date\n" \
                           f"3. All upcoming payment due dates\n4. Pay now\n5. Request to pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "9":
                    # print("6 loop")
                    data = f"*Let me know what language would you prefer to chat.\nA. English\nB. Arabic\n" \
                           f"C. Hindi\nD. Russian\nE. Malayalam\nF. Tamil\n*Note:* If you would like to change " \
                           f"your language preference again means just type 9"
                    replyData = data
                elif querymessage == "1":
                    # print("7 loop")
                    customerAmount = customerPaymentAmount[int(customerIndexValue)]
                    # print(customerAmount)
                    data = "Your apartemnt current due amount is AED{amount}".format(amount=customerAmount)
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "2":
                    # print("8 loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    data = "Your next payment due date is {date1}".format(date1=date1)
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "3":
                    # print("9 loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    date2 = customer2Due[int(customerIndexValue)]
                    date3 = customer3Due[int(customerIndexValue)]
                    data = "Your first due date is {date1}\nSecond due date is {date2}\nThird due date is {date3}" \
                        .format(date1=date1, date2=date2, date3=date3)
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "4":
                    # print("10 loop")
                    data = "Here is your payment link please click it.\nhttps://alhamra.ae/"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "5":
                    # print("11 loop")
                    data = "*Please let me know when would you like to pay*\n1.1 Pay in two days\n1.2 Pay later"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "1.1":
                    # print("12 loop")
                    date1 = customer1Due[int(customerIndexValue)]
                    # print(date1)
                    # print(type(date1))
                    year = int(date1[:4])
                    month = int(date1[5:7])
                    date = int(date1[8:10])
                    day2 = datetime.datetime(year, month, date) + datetime.timedelta(days=2)
                    data = "Dear {name} as per your request please don't forget to pay your due amount before " \
                           "{date2} and Thank you for your response".format(name=ProfileName, date2=day2.date())
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage == "1.2":
                    # print("13 loop")
                    data = "Please provide an exact date that you planned to pay your due amount." \
                           "\n*Your date format should be like this(YYYY-MM-DD)"
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif re.match("[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}", querymessage.lower()):
                    # print("14 loop")
                    data = "We accepted your planned paying date. Please don't forget to pay. Thank you for your " \
                           "response and utilizing our Al-hamra bot service."
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                elif querymessage.lower() in userFinalResponse:
                    # print("15 loop")
                    data = "Thank you for utilizing our Al-hamra bot service. Please feel free to reach us at " \
                           "anytime. Have a great day {name}".format(name=ProfileName)
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                else:
                    # print("16 loop")
                    data = "Invalid keywords!. Please enter complete valid keywords."
                    data1 = translate.translate_text(Text=data, SourceLanguageCode="en",
                                                     TargetLanguageCode=preferredLanguage)
                    translatedText = data1.get('TranslatedText')
                    replyData = translatedText
                return replyData

            replyData1 = rule_process(msg)
            response.message(body=replyData1, to=PersonNumber, from_=senderNumber)
    return Response(str(response), mimetype="application/xml")


if __name__ == '__main__':
    app.run(debug=True, port=8088, host="0.0.0.0")
