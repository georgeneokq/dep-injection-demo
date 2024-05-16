from kink import di
import tkinter as tk
import threading
from time import sleep
from httpservice import HttpService
from auth import Auth
from uicontroller import UiController

# Constants
AUTH_URL = 'http://127.0.0.1:5000/authenticated'

class MainWindow():
    """
    A simple tkinter window manager class which contains a label.
    In this demo, other classes will make a reference to an instance of this class
    to update the tkinter UI.
    """
    def __init__(self):
        # Create the tkinter window
        root = tk.Tk()

        # Set tkinter window properties
        root.geometry("600x100")
        root.title("DI demo")

        # Attach label
        label = tk.Label(root, text="Authenticating...", font=("Arial", 18))
        label.pack()

        # Assign object properties
        self.root = root
        self.label = label

        # Center window
        self.center_window()

    def center_window(self):
        """
        Centers the tkinter window on the screen
        """
        self.root.update_idletasks()
        width = self.root.winfo_width()
        frm_width = self.root.winfo_rootx() - self.root.winfo_x()
        win_width = width + 2 * frm_width
        height = self.root.winfo_height()
        titlebar_height = self.root.winfo_rooty() - self.root.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = self.root.winfo_screenwidth() // 2 - win_width // 2
        y = self.root.winfo_screenheight() // 2 - win_height // 2
        self.root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        self.root.deiconify()
    
    def start_mainloop(self):
        self.root.mainloop()

    def update_text(self, text: str):
        self.label.config(text=text)


if __name__ == '__main__':
    # Create tkinter window reference (loop not started yet)
    window = MainWindow()

    # Populate dependency injection container
    di["http"] = HttpService()
    di["window"] = window

    # Simulate an UI update awhile after the tkinter window is created
    def authenticate():
        # Takes slightly longer than 1 second for some reason but that's not the focus...
        sleep(1)

        # DI Demo #1: Auth class' constructor requires HttpService, but not explicitly passed in as a parameter.
        #             An instance of MainWindow is automatically injected into the constructor
        #             of the Auth class by using kink library's @inject decorator (see auth.py)
        auth = Auth(AUTH_URL)
        authenticated = auth.authenticate()

        # DI Demo #2: UiController class' constructor requires MainWindow, but not explicitly passed in as a parameter.
        #             Works exactly the same way as the Auth class' usage of HttpService.
        ui_controller = UiController()
        ui_controller.update_ui_text("Authenticated" if authenticated else "Not Authenticated")
    
    # Start the thread which will update the UI after some time
    threading.Thread(target=authenticate).start()

    # Start the tkinter window
    window.start_mainloop()