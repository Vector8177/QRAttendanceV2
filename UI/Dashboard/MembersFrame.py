import customtkinter

from UI.Dashboard.MemberWidget import MemberWidget


class MembersFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.member_list: [MemberWidget] = []

        self.grid_columnconfigure(0, weight=1)

    def sign_in(self, id: int, name: str):
        temp_memwidget = MemberWidget(master=self, id=id, name=name)
        temp_memwidget.grid(row=len(self.member_list), column=0, sticky="ew")
        self.member_list.append(temp_memwidget)

    def sign_out(self, id: int):
        for m_widget in self.member_list:
            if m_widget.get_id() == id:
                m_widget.destroy()
                self.member_list.remove(m_widget)