import pandas as pd

customerDataFrame = pd.read_csv("customer-data.csv")
customerNames = customerDataFrame["Customer-name"]
customerEmails = customerDataFrame["E-mail-ID"]
customerPhoneNumber = customerDataFrame["Phone-number"]
customerPaymentAmount = customerDataFrame["Payment-amount"]
allCustomerNumbers = list(customerPhoneNumber)
customerIndexValue = customerDataFrame[customerDataFrame["Phone-number"] == 971521285497].index.values
print(customerIndexValue)

# def getindexes(dfObj, value):
#     """ Get index positions of value in dataframe i.e. dfObj."""
#     listOfPos = list()
#     # Get bool dataframe with True at positions where the given value exists
#     result = dfObj.isin([value])
#     # Get list of columns that contains the value
#     seriesObj = result.any()
#     columnNames = list(seriesObj[seriesObj == True].index)
#     # Iterate over list of columns and fetch the rows indexes where value exists
#     for col in columnNames:
#         rows = list(result[col][result[col] == True].index)
#         for row in rows:
#             listOfPos.append((row, col))
#     # Return a list of tuples indicating the positions of value in the dataframe
#     return listOfPos
#
#
# listOfPositions = getindexes(customerDataFrame, +)
