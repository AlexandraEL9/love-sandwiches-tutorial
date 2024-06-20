import gspread
from google.oauth2.service_account import Credentials

# Define the scope
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

# Provide the path to your service account key file
CREDS = Credentials.from_service_account_file('creds.json')

# Apply the defined scopes to the credentials
SCOPED_CREDS = CREDS.with_scopes(SCOPE)

# Authorize the client using the scoped credentials
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)

# Open the Google Sheets file by name
SHEET = GSPREAD_CLIENT.open('love-sandwiches')

# Access the 'sales' worksheet
sales = SHEET.worksheet('sales')

# Fetch all data from the worksheet
data = sales.get_all_values()

# Print the fetched data
print(data)
