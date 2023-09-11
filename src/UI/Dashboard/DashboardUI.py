import os.path
import threading
import time
from queue import Queue
from PIL import Image

import PIL
import customtkinter

from src.Constants import Constants
from src.QRTools.QRDaemon import QRDaemon
from src.UI.Dashboard.MembersFrame import MembersFrame


class DashboardUI:
    def __init__(self, parent: customtkinter.CTkTabview):
        self.ID = "Dashboard"
        self.parent = parent
        self.parent.tab(self.ID).grid_columnconfigure((0, 1, 2, 3), weight=1, pad=10)
        self.parent.tab(self.ID).grid_rowconfigure(0, weight=1)

        self.parent.member_section = MembersFrame(master=parent.tab(self.ID))
        self.parent.member_section.grid(row=0,
                                        column=0,
                                        sticky="nsew",
                                        rowspan=2,
                                        pady=(15, 0),
                                        padx=15,
                                        columnspan=3)

        self.sign_out_all = customtkinter.CTkButton(master=parent.tab(self.ID),
                                                    text="Sign Out All",
                                                    fg_color="#D63D3D",
                                                    bg_color="transparent",
                                                    hover_color="#BC3535",
                                                    command=self.parent.member_section.sign_out_all)
        self.sign_out_all.grid(row=3, column=1, sticky="sew", pady=(10, 10), padx=15)

        self.right_frame = RightFrame(self.parent.tab(self.ID), member_section=self.parent.member_section)
        self.right_frame.grid(row=0, column=3, padx=10, pady=10, sticky="nsew")


# self.bob = customtkinter.CTkEntry(master=parent.tab(self.ID))
# self.bob.grid(row=0,column=1,sticky="n")
#
# self.submit = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.add_bit)
# self.submit.grid(row=2,column=1)
# self.rem = customtkinter.CTkButton(master=parent.tab(self.ID), command=self.remove_bit)
# self.rem.grid(row=3, column=1)

# parent.label = customtkinter.CTkLabel(master=parent.tab(self.ID))
# parent.label.grid(row=0, colpipumn=0, padx=0, pady=0)


class RightFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, member_section: MembersFrame, **kwargs):
        super().__init__(master, **kwargs)

        self.member_section = member_section

        self.img_queue = Queue()

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.manual_sign_in = ManualSignIn(member_section=self.member_section,
                                           master=self)
        self.manual_sign_in.grid(row=0, column=0, pady=10, padx=10, sticky="new")

        self.image_frame = customtkinter.CTkFrame(master=self)
        self.image_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.image_frame.grid_columnconfigure(0, weight=1)
        self.image_frame.grid_rowconfigure(0, weight=1)

        self.image_w = customtkinter.CTkImage(
            light_image=Image.open(os.path.join(Constants.RESOURCES_PATH, 'blank_img.png')),
            size=(20, 20))
        self.img_label = customtkinter.CTkLabel(self.image_frame, image=self.image_w, text="")
        self.img_label.grid(row=0, column=0, padx=5, pady=10, sticky="")

        self.qrb = customtkinter.CTkButton(master=self,
                                           text="QR",
                                           fg_color="#D63D3D",
                                           bg_color="transparent",
                                           hover_color="#BC3535",
                                           command=self.launch_qr)

        self.qrb.grid(row=2, column=0, padx=10, pady=10)

    def read_cam_img(self):
        while True:
            if self.img_queue.full():
                continue
            self.image_w.configure(light_image=Image.fromarray(self.img_queue.get()))
            self.img_label.configure(image=self.image_w, text="")
            time.sleep(0.05)

    def launch_qr(self):
        self.image_w.configure(size=(400,400))
        qr_daemon = QRDaemon(member_list=self.member_section, img_q=self.img_queue)
        qr_daemon_thread = threading.Thread(target=qr_daemon.main)
        qr_daemon_thread.daemon = True
        qr_daemon_thread.start()

        img_update_thread = threading.Thread(target=self.read_cam_img)
        img_update_thread.daemon = True
        img_update_thread.start()


class ManualSignIn(customtkinter.CTkFrame):
    def __init__(self, member_section, master, **kwargs):
        super().__init__(master, **kwargs)
        self.grid_columnconfigure(0, weight=1)

        self.id_entry_label = customtkinter.CTkLabel(master=self, text="Enter ID: ")
        self.id_entry_label.grid(row=0, column=0, padx=25, pady=(5, 15))

        self.member_section = member_section

        self.id_entry = customtkinter.CTkEntry(master=self)
        self.id_entry.grid(row=1, column=0, padx=25)

        self.submit_button = customtkinter.CTkButton(master=self,
                                                     text="Sign In",
                                                     fg_color=Constants.GREEN_COLOR,
                                                     bg_color="transparent",
                                                     hover_color=Constants.GREEN_HOVER_COLOR,
                                                     command=self.submit_event)
        self.submit_button.grid(row=2, column=0, padx=25, pady=(10, 15))

    def submit_event(self):
        id = self.id_entry.get()
        self.id_entry.delete(0, "end")

        self.member_section.sign_in(id)
