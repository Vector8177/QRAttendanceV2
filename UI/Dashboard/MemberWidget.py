import customtkinter


class MemberWidget(customtkinter.CTkFrame):
    def __init__(self, master, id, name, **kwargs):
        super().__init__(master, **kwargs)

        self.id = id
        self.name = name

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.name_label = customtkinter.CTkLabel(master=self, text=self.name,bg_color="transparent")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.signout_button = customtkinter.CTkButton(master=self,
                                                      text="Sign Out",
                                                      command=self.button_event,
                                                      fg_color="#D63D3D",
                                                      bg_color="transparent",
                                                      hover_color="#BC3535")
        self.signout_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def button_event(self):
        print("Signout Commencing")