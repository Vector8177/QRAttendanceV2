import datetime
import json
import os
import time

import customtkinter

from src.CloudUpdate import UpdateSheet
from src.Constants import Constants
from src.UI.Dashboard.MemberWidget import MemberWidget


class MembersFrame(customtkinter.CTkScrollableFrame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.member_list: [MemberWidget] = []
        self.attendance_map: (str, datetime.time) = {}

        with open(Constants.JSON_PATH) as f:
            temp = json.load(f)

            if len(temp.keys()) == 0:
                return

            for key in temp.keys():
                self.add_member_widget(key)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)

    def check_signed_in(self, id: str):
        a = self.attendance_map.get(id)
        return not self.attendance_map.get(id) is None

    def add_member_widget(self, id: int):
        name: str
        with open(Constants.JSON_PATH) as f:
            temp = json.load(f)
            name = temp[id]["name"]
        temp_memwidget = MemberWidget(master=self, id=id, name=name)
        temp_memwidget.grid(row=int(len(self.member_list) / 4), column=len(self.member_list) % 4, pady=5, padx=5,
                            sticky="ew")
        self.member_list.append(temp_memwidget)
        # self.attendance_map[id] = int(time.time())

    def sign_in(self, m_id: int):
        self.attendance_map[m_id] = int(time.time())
        for member in self.member_list:
            if member.get_id() == m_id:
                member.set_button_state(True)

    def sign_out(self, m_id: int):
        for m_widget in self.member_list:
            if m_widget.get_id() == m_id and self.check_signed_in(m_id):
                time_diff = int((time.time() - self.attendance_map[m_id]) / 60)
                self.attendance_map.pop(m_id)
                temp = {}

                m_widget.set_button_state(False)

                with open(Constants.JSON_PATH) as f:
                    temp = json.load(f)

                t_dates = []
                with open(Constants.MEETING_DATES_PATH) as f:
                    t_dates = f.readlines()

                if not str(datetime.date.today()) in t_dates:
                    t_dates.append(str(datetime.date.today()))
                    with open(Constants.MEETING_DATES_PATH, "w") as f:
                        f.writelines(t_dates)

                temp[m_id]["attendance"][str(datetime.date.today())] = str(time_diff)

                with open(Constants.JSON_PATH, "w") as f:
                    json.dump(temp, f, indent=4)

    def sign_out_all(self):
        for m_widget in self.member_list:
            self.sign_out(m_widget.get_id())

        UpdateSheet.update_sheet()
