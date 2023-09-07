import customtkinter

from src.QRTools.QRDaemon import QRDaemon
from src.UI.Dashboard.MembersFrame import MembersFrame

import threading


class DashboardUI:
    def __init__(self, parent: customtkinter.CTkTabview):
        self.ID = "Dashboard"
        self.parent = parent
        self.parent.tab(self.ID).grid_columnconfigure((0, 1, 2), weight=1, pad=10)
        self.parent.tab(self.ID).grid_rowconfigure(0, weight=1)

        self.parent.member_section = MembersFrame(master=parent.tab(self.ID))
        self.parent.member_section.grid(row=0,
                                        column=0,
                                        sticky="nsew",
                                        rowspan=2,
                                        pady=(15, 0),
                                        padx=15)

        self.sign_out_all = customtkinter.CTkButton(master=parent.tab(self.ID),
                                                    text="Sign Out All",
                                                    fg_color="#D63D3D",
                                                    bg_color="transparent",
                                                    hover_color="#BC3535",
                                                    command=self.parent.member_section.sign_out_all)
        self.sign_out_all.grid(row=3,column=0,sticky="sew", pady=(10,10), padx=15)

        self.manual_sign_in = ManualSignIn(member_section=self.parent.member_section,
                                           master=parent.tab(self.ID))
        self.manual_sign_in.grid(row=0,column=1,pady=10,padx=10, sticky="new")

        self.qrb = customtkinter.CTkButton(master=parent.tab(self.ID),
                                                    text="QR",
                                                    fg_color="#D63D3D",
                                                    bg_color="transparent",
                                                    hover_color="#BC3535",
                                                    command=self.launch_qr)
        self.qrb.grid(row=1,column=1,padx=10,pady=10)
        # self.bob = customtkinter.CTkEntry(master=parent.tab(self.ID))
        # self.bob.grid(row=0,column=1,sticky="n")
        #
        # self.submit = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.add_bit)
        # self.submit.grid(row=2,column=1)
        # self.rem = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.remove_bit)
        # self.rem.grid(row=3, column=1)

    def launch_qr(self):
        qr_daemon = QRDaemon(member_list=self.parent.member_section)
        qr_daemon_thread = threading.Thread(target=qr_daemon.main)
        qr_daemon_thread.start()

    def add_bit(self):
        id = self.bob.get()
        self.bob.select_clear()

        self.parent.member_section.sign_in(id)

    def remove_bit(self):
        id = self.bob.get()
        self.parent.member_section.sign_out(id)

        # parent.label = customtkinter.CTkLabel(master=parent.tab(self.ID))
        # parent.label.grid(row=0, column=0, padx=0, pady=0)

class ManualSignIn(customtkinter.CTkFrame):
    def __init__(self, member_section, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0,weight=1)

        self.id_entry_label = customtkinter.CTkLabel(master=self, text="Enter ID: ")
        self.id_entry_label.grid(row=0,column=0,padx=25,pady=(5,15))

        self.member_section = member_section

        self.id_entry = customtkinter.CTkEntry(master=self)
        self.id_entry.grid(row=1,column=0,padx=25)

        self.submit_button = customtkinter.CTkButton(master=self,
                                                    text="Sign In",
                                                    fg_color="#36C170",
                                                    bg_color="transparent",
                                                    hover_color="#30A15F",
                                                    command=self.submit_event)
        self.submit_button.grid(row=2,column=0,padx=25,pady=(10,15))
    def submit_event(self):
        id = self.id_entry.get()
        self.id_entry.delete(0,"end")

        self.member_section.sign_in(id)
