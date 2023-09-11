import datetime
import json
import os.path

import customtkinter
import csv

from src.CloudUpdate import UpdateSheet
from src.Constants import Constants
from src.UI.Dashboard.MembersFrame import MembersFrame


class DataGenerationFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=(0, 1), weight=1)
        self.grid_rowconfigure(index=0, weight=1)

        self.getFromFileText = customtkinter.CTkTextbox(master=self)
        self.getFromFileText.grid(row=0, column=0, padx=10, pady=10, sticky="nsew", columnspan=2)
        self.getFromFile = customtkinter.CTkButton(master=self,
                                                   text="Generate JSON",
                                                   fg_color=Constants.BLUE_COLOR,
                                                   bg_color="transparent",
                                                   hover_color=Constants.BLUE_HOVER_COLOR,
                                                   command=self.generate_json)
        self.getFromFile.grid(row=1, column=0, padx=10, pady=10, sticky="se")
        self.clear_json = customtkinter.CTkButton(master=self,
                                                  text="Clear JSON",
                                                  fg_color=Constants.RED_COLOR,
                                                  bg_color="transparent",
                                                  hover_color=Constants.RED_HOVER_COLOR,
                                                  command=clear_json_pwd)
        self.clear_json.grid(row=1, column=0, padx=10, pady=10, sticky="sw")
        self.export_to_csv = customtkinter.CTkButton(master=self,
                                                     text="Export JSON",
                                                     fg_color=Constants.BLUE_COLOR,
                                                     bg_color="transparent",
                                                     hover_color=Constants.BLUE_HOVER_COLOR,
                                                     command=generate_csv)
        self.export_to_csv.grid(row=1, column=1, padx=10, pady=10, sticky="sw")

    def generate_json(self):
        f = self.getFromFileText.get("0.0", "end")
        self.getFromFileText.delete("0.0", "end")

        temp = [s.split("\t") for s in f.split("\n")]

        jsonf = {}
        with open(Constants.JSON_PATH) as f:
            jsonf = json.load(f)

        for bit in temp:
            if len(bit) < 2:
                continue

            jsonf[bit[0]] = {
                "name": bit[1],
                "attendance": {}
            }

        with open(Constants.JSON_PATH, "w") as f:
            json.dump(jsonf, f, indent=4)


def flatten_json():
    fields = []
    list_fin = []
    with open(Constants.MEETING_DATES_PATH) as file:
        fields = file.readlines()
    with open(Constants.JSON_PATH) as f:
        temp: {} = json.load(f)
        for key, value in temp.items():
            t_arr = [value["name"], key]

            for d in fields:
                if d in value["attendance"].keys():
                    t_arr.append(value["attendance"][d])
                else:
                    t_arr.append("0")

            list_fin.append(t_arr)
    fields.insert(0, "ID")
    fields.insert(0, "Name")

    list_fin.insert(0, fields)

    return list_fin


def generate_csv():
    list_fin = flatten_json()

    yr_str = ""

    if datetime.date.today().month <= 6:
        yr_str = f'{datetime.date.today().year - 1}-{datetime.date.today().year}'
    else:
        yr_str = f'{datetime.date.today().year}-{datetime.date.today().year + 1}'

    current_dir_path = os.path.join(
        Constants.DOWNLOADS_PATH,
        f'Attendance Records - {yr_str}')

    if not os.path.exists(current_dir_path):
        os.makedirs(current_dir_path)

    file_address_current = os.path.join(current_dir_path, f'{datetime.date.today()}.csv')

    with open(file_address_current, "w") as f:
        csvwriter = csv.writer(f)

        csvwriter.writerows(list_fin)

    UpdateSheet.update_sheet()


def clear_json_pwd():
    dialog = customtkinter.CTkInputDialog(text="Are you sure you want to do this? Enter password below:",
                                          title="Confirmation")

    entered_password = dialog.get_input()

    if entered_password == "Vector8177Authorization":
        clear_json()


def clear_json():
    with open(Constants.JSON_PATH, "w") as f:
        json.dump({}, f, indent=4)
