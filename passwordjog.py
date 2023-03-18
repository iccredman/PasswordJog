# Password Jog main file that gets data from google sheet
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '17dnWxj6FLWD_dABT9cPBXsLXsDQwcBL4-wFjyL8NB6g'
SAMPLE_RANGE_NAME = 'Sheet1!A:E'


def get_jog(account):
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.json', 'w') as token:
                token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        if not values:
            print('No data found.')
            return

        # Convert to lowercase
        account = account.lower()

        # print(values)
        # Search for the first item in values and return the second item
        result = [item[1] for item in values if item[0] == account]
        # print(result)
        result_string = ''.join(result)
        print(result_string)
        return(result_string)
        
    except Exception as e:
        print(e)


if __name__ == '__main__':
    account = input("Enter Account: ")
    get_jog(account)




## THIS CODE WORKS
# from __future__ import print_function

# import os.path

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build
# from googleapiclient.errors import HttpError

# # If modifying these scopes, delete the file token.json.
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# # The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '17dnWxj6FLWD_dABT9cPBXsLXsDQwcBL4-wFjyL8NB6g'
# SAMPLE_RANGE_NAME = 'Sheet1!A:E'


# def get_jog(account):
#     """Shows basic usage of the Sheets API.
#     Prints values from a sample spreadsheet.
#     """
#     creds = None
#     # The file token.json stores the user's access and refresh tokens, and is
#     # created automatically when the authorization flow completes for the first
#     # time.
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
#     # If there are no (valid) credentials available, let the user log in.
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     'credentials.json', SCOPES)
#                 creds = flow.run_local_server(port=0)
#             # Save the credentials for the next run
#             with open('token.json', 'w') as token:
#                 token.write(creds.to_json())

#     try:
#         service = build('sheets', 'v4', credentials=creds)

#         # Call the Sheets API
#         sheet = service.spreadsheets()
#         result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                     range=SAMPLE_RANGE_NAME).execute()
#         values = result.get('values', [])

#         if not values:
#             print('No data found.')
#             return

#         # print(values)
#         # Search for the first item in values and return the second item
#         result = [item[1] for item in values if item[0] == account]
#         # print(result)
#         result_string = ''.join(result)
#         print(result_string)
#         return(result_string)
        
#     except Exception as e:
#         print(e)

# # ## Streamlit section
# # import streamlit as st

# # st.title("Simple Streamlit Page")

# # input_box = str(st.text_input("Please enter your text"))

# # if st.button("Submit"):
# #     # Run the function
# #     result = get_jog(input_box)
# #     # Display the output on the Streamlit page
# #     st.write("Result:", result)

# if __name__ == '__main__':
#     account = input("Enter Account: ")
#     get_jog(account)