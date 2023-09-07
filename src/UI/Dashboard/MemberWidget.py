import customtkinter

from src.Constants import Constants


class MemberWidget(customtkinter.CTkFrame):
    def __init__(self, master, id, name, **kwargs):
        super().__init__(master, **kwargs)

        self.id = id
        self.name = name
        self.master = master

        self.grid_columnconfigure((0, 1, 2), weight=1)
        self.name_label = customtkinter.CTkLabel(master=self, text=self.name,bg_color="transparent")
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.signout_button = customtkinter.CTkButton(master=self,
                                                      text="Sign In",
                                                      command=self.sign_in_ph,
                                                      fg_color=Constants.RED_COLOR,
                                                      bg_color="transparent",
                                                      hover_color=Constants.RED_HOVER_COLOR)
        self.signout_button.grid(row=0, column=2, padx=10, pady=10, sticky="e")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_button_state(self, is_signed_in: bool):
        if is_signed_in:
            self.signout_button.configure(text="Sign Out",
                                          fg_color=Constants.GREEN_COLOR,
                                          hover_color=Constants.GREEN_HOVER_COLOR,
                                          command=self.sign_out_ph)
        else:
            self.signout_button.configure(text="Sign In",
                                          fg_color=Constants.RED_COLOR,
                                          hover_color=Constants.RED_HOVER_COLOR,
                                          command=self.sign_in_ph)

    def sign_in_ph(self):
        self.master.sign_in(self.id)

    def sign_out_ph(self):
        self.master.sign_out(self.id)