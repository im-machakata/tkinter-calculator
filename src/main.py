import tkinter as tk
from tkinter import messagebox
class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("ISH24 Calculator")
        self.master.resizable(False, False)

        # display box
        self.entry = tk.Entry(self.master, width=30, font=("Arial", 14))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # create numeric buttons
        button_grid = {
            "7": (1, 0), "8": (1, 1), "9": (1, 2), "/": (1, 3),
            "4": (2, 0), "5": (2, 1), "6": (2, 2), "*": (2, 3),
            "1": (3, 0), "2": (3, 1), "3": (3, 2), "-": (3, 3),
            "0": (4, 0), ".": (4, 1), "=": (4, 2), "+": (4, 3)
        }

        for button_text, button_position in button_grid.items():
            button = tk.Button(self.master, text=button_text, font=("Arial", 12), width=5, height=2, command=lambda text=button_text: self.handle_button_click(text), bg="white")
            button.grid(row=button_position[0], column=button_position[1], padx=5, pady=5)

        # clear calculator button
        self.clear_button = tk.Button(self.master, width="30", font=("Arial", 14), text="Clear Calculator", height=2, bg="white", command=self.clear_calculator_text)
        self.clear_button.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

    def handle_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except Exception as e:
                messagebox.showwarning("System error", f"{self.entry.get()} is not a calculatable value, please try calculating something else.")
                self.clear_calculator_text()
        else:
            self.entry.insert(tk.END, text)

    def clear_calculator_text(self):
        self.entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()