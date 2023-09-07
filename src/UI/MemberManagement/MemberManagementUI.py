import json

import customtkinter


class MemberManagementUI:
	def __init__(self, parent: customtkinter.CTkTabview):
		self.ID = "Manage Members"
		self.parent = parent
		self.parent.tab(self.ID).grid_columnconfigure(index=(0, 1), weight=1)
		self.parent.tab(self.ID).grid_rowconfigure(index=(0, 1), weight=1)

		self.getFromFileText = customtkinter.CTkTextbox(master=parent.tab(self.ID))
		self.getFromFileText.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
		self.getFromFile = customtkinter.CTkButton(master=parent.tab(self.ID), text="Generate JSON",
												   command=self.generate_json)
		self.getFromFile.grid(row=1, column=0, padx=10, pady=10, sticky="n")

	def generate_json(self):
		f = self.getFromFileText.get("0.0", "end")
		self.getFromFileText.delete("0.0", "end")

		temp = [s.split("\t") for s in f.split("\n")]

		jsonf = {}
		with open("/Users/ishaan/Documents/Projects/QRAttendanceV2/src/Data/MemberList.json") as f:
			jsonf = json.load(f)

		for bit in temp:
			jsonf[bit[0]] = {
				"name": bit[1],
				"attendance": {}
			}

		with open("/Users/ishaan/Documents/Projects/QRAttendanceV2/src/Data/MemberList.json", "w") as f:
			json.dump(jsonf, f, indent=4)
