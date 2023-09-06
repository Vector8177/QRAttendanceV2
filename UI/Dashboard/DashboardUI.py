import customtkinter

from UI.Dashboard.MembersFrame import MembersFrame


class DashboardUI:
    def __init__(self, parent: customtkinter.CTkTabview):
        self.ID = "Dashboard"
        self.parent = parent
        self.parent.tab(self.ID).grid_columnconfigure((0, 1, 2), weight=2)
        self.parent.tab(self.ID).grid_rowconfigure((0), weight=1)

        self.parent.member_section = MembersFrame(master=parent.tab(self.ID))
        self.parent.member_section.grid(row=0, column=0, sticky="nsew")

        self.bob = customtkinter.CTkEntry(master=parent.tab(self.ID))
        self.bob.grid(row=0,column=1,sticky="n")

        self.ab = customtkinter.CTkEntry(master=parent.tab(self.ID))
        self.ab.grid(row=1,column=1,sticky="n")

        self.submit = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.add_bit)
        self.submit.grid(row=2,column=1)
        self.rem = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.remove_bit)
        self.rem.grid(row=3, column=1)

    def add_bit(self):
        id = self.bob.get()
        self.bob.select_clear()
        name = self.ab.get()
        self.ab.select_clear()

        self.parent.member_section.sign_in(id, name)

    def remove_bit(self):
        id = self.bob.get()
        self.parent.member_section.sign_out(id)

        # parent.label = customtkinter.CTkLabel(master=parent.tab(self.ID))
        # parent.label.grid(row=0, column=0, padx=0, pady=0)
