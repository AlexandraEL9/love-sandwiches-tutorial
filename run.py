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
    #print(f"The data provided is: {data_str}")

    # validata data 1- create nw varible
    sales_data = data_str.split(",")
    validate_data(sales_data)

#validation function
def validate_data(values):
    """
    Inside the try, converts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there aren't exactly 6 values.
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly 6 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")


get_sales_data()
