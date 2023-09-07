import json

import customtkinter

from src.UI.Dashboard import DashboardUI
from src.UI.Dashboard.MembersFrame import MembersFrame
from src.UI.MemberManagement.DataGenerationFrame import DataGenerationFrame
from src.UI.MemberManagement.MemberLookupFrame import MemberLookupFrame


class MemberManagementUI:
    def __init__(self, parent: customtkinter.CTkTabview):
        self.ID = "Manage Members"
        self.parent = parent
        self.parent.tab(self.ID).grid_columnconfigure(index=(0, 1), weight=1)
        self.parent.tab(self.ID).rowconfigure(index=0, weight=1)

        self.datagen_frame = DataGenerationFrame(self.parent.tab(self.ID))
        self.datagen_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.member_lookup_frame = MemberLookupFrame(self.parent.tab(self.ID))
        self.member_lookup_frame.grid(row=0,column=1,sticky="nsew", padx=10, pady=10)



