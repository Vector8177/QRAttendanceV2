from ctypes import windll

from src.UI.UIParent import App



if __name__ == "__main__":
    windll.shcore.SetProcessDpiAwareness(2)
    app = App()
    app.mainloop()