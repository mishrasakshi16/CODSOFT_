import tkinter as tk
from tkinter import simpledialog


class CalculatorApplication(tk.Tk):
    """
    A simple calculator application using Tkinter.

    Attributes:
        val1 (float): The first operand value.
        val2 (float): The second operand value.
        result (float or str): The result of the operation, or "Undefined" for division by zero.

    Methods:
        __init__(self, master=None):
            Initialize the calculator application.

        createWidgets(self):
            Create the GUI components for the calculator application.

        operate(self, operator):
            Perform a mathematical operation based on the given operator.
    """

    def __init__(self, master=None):
        """
        Initialize the calculator application.

        Parameters:
            master (tk.Tk): The master Tkinter window.
        """
        tk.Tk.__init__(self, master)
        self.title("Calculator")
        self.resizable(False, False)
        self.createWidgets()

    def createWidgets(self):
        """
        Create the GUI components for the calculator application.
        """
        self.val1 = 0
        self.val2 = 0
        self.result = 0

        title_label = tk.Label(self, text="Calculator", font=("Helvetica", 24))
        title_label.pack(pady=10)

        self.result_label = tk.Label(
            self, text=str(self.result), font=("Helvetica", 24)
        )
        self.result_label.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(padx=20, pady=20)

        sum_button = tk.Button(
            button_frame, text=" + ", command=lambda: self.operate("+")
        )
        sub_button = tk.Button(
            button_frame, text=" - ", command=lambda: self.operate("-")
        )
        prod_button = tk.Button(
            button_frame, text=" * ", command=lambda: self.operate("*")
        )
        div_button = tk.Button(
            button_frame, text=" / ", command=lambda: self.operate("/")
        )

        sum_button.grid(row=0, column=0, padx=10, pady=10)
        sub_button.grid(row=0, column=1, padx=10, pady=10)
        prod_button.grid(row=1, column=0, padx=10, pady=10)
        div_button.grid(row=1, column=1, padx=10, pady=10)

    def operate(self, operator):
        """
        Get values from the user and perform an operation based on the given operator.

        Parameters:
            operator (str): The mathematical operator (+, -, *, /).
        """
        self.val1 = float(
            simpledialog.askstring("Input", "Enter the value of val1:", parent=self)
        )
        self.val2 = float(
            simpledialog.askstring("Input", "Enter the value of val2:", parent=self)
        )

        if operator == "+":
            self.result = self.val1 + self.val2
        elif operator == "-":
            self.result = self.val1 - self.val2
        elif operator == "*":
            self.result = self.val1 * self.val2
        elif operator == "/":
            if self.val2 == 0:
                self.result = "Undefined"
            else:
                self.result = self.val1 / self.val2

        self.result_label.config(text=str(self.result))


if __name__ == "__main__":
    app = CalculatorApplication()
    app.mainloop()