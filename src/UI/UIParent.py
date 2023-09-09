from queue import Queue

import customtkinter

from src.UI.Dashboard.DashboardUI import DashboardUI
from src.UI.MemberManagement.MemberManagementUI import MemberManagementUI


class HomeTabView(customtkinter.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.add("Dashboard")
        self.add("Manage Members")

        self.DashboardTab = DashboardUI(self)
        self.MemberManagementTab = MemberManagementUI(self)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("QR Attendance")
        self.geometry("1600x900")
        self.minsize(800,450)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0), weight=1)
        self.tab_view = HomeTabView(master=self)
        self.tab_view.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")
        # self.grid_columnconfigure((0, 1), weight=1)
        #
        # self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        # self.button.grid(row=0, column=0, padx=20, pady=20, sticky="nsew", columnspan=2)
        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="nsew")
        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="nsew")
        #
        # self.segemented_button_var = customtkinter.StringVar(value="Member Dashboard")
        # self.segemented_button = customtkinter.CTkSegmentedButton(self,
        #                                                           values=[
        #                                                               "Member Dashboard",
        #                                                               "Manage Members"],
        #                                                           command=self.segmented_button_callback,
        #                                                           variable=self.segemented_button_var,
        #                                                           dynamic_resizing=True)
        # self.segemented_button.grid(row=2, column=0, padx=20, pady=(0, 20), columnspan=2, sticky="nsew")

    def segmented_button_callback(self, value):
        print("segmented button clicked:", value)

    def button_callback(self):
        print("button pressed")
