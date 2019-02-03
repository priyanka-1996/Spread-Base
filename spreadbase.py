import gspread #to communicate with google speadsheets
from oauth2client.service_account import ServiceAccountCredentials
import  pandas as pd


#now we will use our credentials to create a client sp that we can communicate with google drive API

Scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive'] #first link is source of data, 2nd link is permission to access it
credentials= ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', Scope)# .json file is basically the file having credentials and client email

#creating a client
Client= gspread.authorize(credentials)

#after sharing the google sheet with client email, access it here
spreadsheet= Client.open("sample database 2").sheet1 #sheet 1 here  is the sheet no.

Extracted_record = spreadsheet.get_all_records() #data in the form of list of dictionary

df = pd.DataFrame(Extracted_record, columns=['first_name',	'last_name',	'company_name',	'address',	'city',	'country',	'postal',	'phone1',	'phone2',	'email',	'web'])
print(df) #data in the form of dataframe(table)
