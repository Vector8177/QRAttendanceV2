import json

import customtkinter

from src.UI.Dashboard.MembersFrame import MembersFrame


class DataGenerationFrame(customtkinter.CTkFrame):
    def __init__(self, master: any, **kwargs):
        super().__init__(master, **kwargs)

        self.grid_columnconfigure(index=0,weight=1)
        self.grid_rowconfigure(index=0,weight=1)

        self.getFromFileText = customtkinter.CTkTextbox(master=self)
        self.getFromFileText.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.getFromFile = customtkinter.CTkButton(master=self,
                                                   text="Generate JSON",
                                                   fg_color="#13BF5A",
                                                   bg_color="transparent",
                                                   hover_color="#0E8C42",
                                                   command=self.generate_json)
        self.getFromFile.grid(row=1, column=0, padx=10, pady=10, sticky="s")

    def generate_json(self):
        f = self.getFromFileText.get("0.0", "end")
        self.getFromFileText.delete("0.0", "end")

        temp = [s.split("\t") for s in f.split("\n")]

        jsonf = {}
        with open(MembersFrame.JSON_PATH) as f:
            jsonf = json.load(f)

        for bit in temp:
            if len(bit) < 2:
                continue

            jsonf[bit[0]] = {
                "name": bit[1],
                "attendance": {}
            }

        with open(MembersFrame.JSON_PATH, "w") as f:
            json.dump(jsonf, f, indent=4)