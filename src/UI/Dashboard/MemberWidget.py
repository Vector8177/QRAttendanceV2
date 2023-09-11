import customtkinter

from src.Constants import Constants


class MemberWidget(customtkinter.CTkFrame):
    def __init__(self, master, id, name, **kwargs):
        super().__init__(master, **kwargs)

        self.id = id
        self.name = name
        self.master = master

        self.grid_columnconfigure(0, weight=1)
        self.signout_button = customtkinter.CTkButton(master=self,
                                                      text=self.name,
                                                      command=self.sign_in_ph,
                                                      fg_color=Constants.RED_COLOR,
                                                      bg_color="transparent",
                                                      hover_color=Constants.RED_HOVER_COLOR,
                                                      border_spacing=10,
                                                      corner_radius=5)

        self.signout_button.grid(row=0, column=0, padx=8, pady=8, sticky="nsew")

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def set_button_state(self, is_signed_in: bool):
        if is_signed_in:
            self.signout_button.configure(fg_color=Constants.GREEN_COLOR,
                                          hover_color=Constants.GREEN_HOVER_COLOR,
                                          command=self.sign_out_ph,
                                          border_spacing=10,
                                          corner_radius=5)

        else:
            self.signout_button.configure(fg_color=Constants.RED_COLOR,
                                          hover_color=Constants.RED_HOVER_COLOR,
                                          command=self.sign_in_ph,
                                          border_spacing=10,
                                          corner_radius=5)

    def sign_in_ph(self):
        self.master.sign_in(self.id)

    def sign_out_ph(self):
        self.master.sign_out(self.id)
