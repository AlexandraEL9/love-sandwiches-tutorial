import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

"""
check linked up- Yes
sales = SHEET.worksheet('sales')

data = sales.get_all_values()

print(data)
"""

# functionnto collect sales data from user
def get_sales_data():
    """
     get sales figures input from the user
    """
    print("Please enter sales data from the market.")
    print("Data should be six numbers, separated by commas.")
    print("Example: 10,20,30,40,50,60\n")
    #use input method to get our sales data from the user in the terminal
    data_str = input("Enter your data here: ")
    print(f"The data provided is: {data_str}")
#call function outside of the function
get_sales_data()
#can enter data into the terminal and then terminal reiterates back
