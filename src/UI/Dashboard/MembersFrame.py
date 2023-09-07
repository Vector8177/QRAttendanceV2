import datetime
import json
import time

import customtkinter

from src.UI.Dashboard.MemberWidget import MemberWidget


class MembersFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.member_list: [MemberWidget] = []
        self.attendance_map: (str, datetime.time) = {}

        self.grid_columnconfigure(0, weight=1)

    def check_signed_in(self, id: str):
        a = self.attendance_map.get(id)
        return not self.attendance_map.get(id) is None

    def sign_in(self, id: int):
        name: str
        with open("/Users/ishaan/Documents/Projects/QRAttendanceV2/src/Data/MemberList.json") as f:
            temp = json.load(f)
            name = temp[id]["name"]
        temp_memwidget = MemberWidget(master=self, id=id, name=name)
        temp_memwidget.grid(row=len(self.member_list), column=0, sticky="ew")
        self.member_list.append(temp_memwidget)
        self.attendance_map[id] = int(time.time())

    def sign_out(self, id: int):
        for m_widget in self.member_list:
            if m_widget.get_id() == id:
                m_widget.destroy()
                self.member_list.remove(m_widget)
                time_diff = int((time.time() - self.attendance_map[id]) / 60)
                temp = {}

                with open("/Users/ishaan/Documents/Projects/QRAttendanceV2/src/Data/MemberList.json") as f:
                    temp = json.load(f)

                temp[id]["attendance"][str(datetime.date.today())] = str(time_diff)

                with open("/Users/ishaan/Documents/Projects/QRAttendanceV2/src/Data/MemberList.json", "w") as f:
                    json.dump(temp, f, indent=4)

    def sign_out_all(self):
        for m_widget in self.member_list:
            self.sign_out(m_widget.get_id())
