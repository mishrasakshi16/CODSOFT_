import tkinter as tk
from tkinter import simpledialog, ttk
import re
import random


class PasswordGeneratorApplication(tk.Tk):
    """
    A simple password generator application using Tkinter.

    Attributes:
        length (int): The length of password.
        result (str): The generated password.

    Methods:
        __init__(self, master=None):
            Initialize the password generator application.

        createWidgets(self):
            Create the GUI components for the password generator application.

        generate(self, difficulty):
            Generate a password based on desired complexity and length.
    """

    def __init__(self, master=None):
        """
        Initialize the password generator application.

        Parameters:
            master (tk.Tk): The master Tkinter window.
        """
        tk.Tk.__init__(self, master)
        self.title("Password Generator")
        self.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        """
        Create the GUI components for the password generator application.
        """

        self.length = 0
        self.result = "[To Be Generated]"
        self.selectedDifficulty = "Easy"

        title_label = tk.Label(self, text="Password Generator", font=("Helvetica", 24))
        title_label.pack(pady=10)

        self.result_label = tk.Label(
            self, text=str(self.result), font=("Helvetica", 20)
        )
        self.result_label.pack(pady=10)

        # Define the options for the dropdown menu
        options = ["Easy", "Medium", "Hard"]

        # Create a dropdown menu
        dropdown_menu = ttk.Combobox(
            self, textvariable=self.selectedDifficulty, values=options, state="readonly"
        )
        dropdown_menu.pack(pady=10)
        dropdown_menu.set("Select an option")  # Set the default value

        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=20)

        generate_button = tk.Button(
            button_frame, text="Generate Password", command=self.generate
        )
        generate_button.pack(padx=10, pady=10)

    def generate(self):
        self.length = int(
            simpledialog.askstring(
                "Input", "Enter the desired length of password", parent=self
            )
        )

        self.result_label.config(text=str(self.result))


if __name__ == "__main__":
    app = PasswordGeneratorApplication()
    app.mainloop()