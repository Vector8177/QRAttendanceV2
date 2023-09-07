import json

import customtkinter

from src.UI.Dashboard.MembersFrame import MembersFrame


class MemberLookupFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(index=0, weight=1)
        self.grid_rowconfigure(index=1, weight=1)

        self.member_id_lookup = MemberIDLookupEntry(master=self, parent=self)
        self.member_id_lookup.grid(row=0, column=0, padx=10, pady=10, sticky="n")

        self.member_info_box = customtkinter.CTkTextbox(master=self, wrap="word", state="disabled")
        self.member_info_box.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")


class MemberIDLookupEntry(customtkinter.CTkFrame):
    def __init__(self, master, parent: MemberLookupFrame, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)
        self.parent = parent
        self.id_entry_label = customtkinter.CTkLabel(master=self, text="Enter ID: ")
        self.id_entry_label.grid(row=0, column=0, padx=25, pady=(5, 15))

        self.id_entry = customtkinter.CTkEntry(master=self)
        self.id_entry.grid(row=1, column=0, padx=25)

        self.submit_button = customtkinter.CTkButton(master=self,
                                                     text="Lookup Member",
                                                     fg_color="#13BF5A",
                                                     bg_color="transparent",
                                                     hover_color="#0E8C42",
                                                     command=self.submit_event)
        self.submit_button.grid(row=2, column=0, padx=25, pady=(10, 15))

    def submit_event(self):
        id_mem = self.id_entry.get()
        self.id_entry.delete(0, "end")

        jsondat = {}
        name = ""
        with open(MembersFrame.JSON_PATH) as f:
            temp = json.load(f)
            name = temp[id_mem]["name"]
            jsondat = temp[id_mem]["attendance"]

        tstr = [f"{key}: {value}" for (key, value) in jsondat.items()]
        self.parent.member_info_box.configure(state="normal")
        self.parent.member_info_box.delete("0.0", "end")
        self.parent.member_info_box.insert("0.0", f"{name}\n" + "\n".join(tstr))
        self.parent.member_info_box.configure(state="disabled")
