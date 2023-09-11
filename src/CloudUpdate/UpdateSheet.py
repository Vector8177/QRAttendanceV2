import gspread
from gspread import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
import json

from src.Constants import Constants
from src.UI.MemberManagement import DataGenerationFrame

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = ServiceAccountCredentials.from_json_keyfile_name(Constants.AUTH_PATH,
                                                               scopes)
file = gspread.authorize(credentials)  # authenticate the JSON key with gspread
sheet = file.open_by_url("https://docs.google.com/spreadsheets/d/15Kke3Mu1RXPREtoQE5KIsKQF0PsiuCmZLCRfNY8SKcQ/edit"
                         "#gid=0")
sheet = sheet.get_worksheet(0)


def update_sheet():
    values = DataGenerationFrame.flatten_json()
    print(values)
    fin_col = convert_num_to_sheet_col('B', len(values[0]))
    fin_row = 7 + len(values) - 1

    sheet.update(values=values,range_name=f"B7:{fin_col}{fin_row}")


def convert_num_to_sheet_col(start: chr, inc: int):
    startn = ord(start)
    charlist = []

    for i in range(inc - 1):
        if startn == 90:
            if len(charlist) == 0:
                charlist.append(65)
            else:
                charlist.insert(0, charlist.get(0) + 1)

            startn = 65
            continue
        startn += 1

    charlist.append(startn)

    r_str = "".join([chr(i) for i in charlist])

    return r_str
