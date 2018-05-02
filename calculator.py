from tkinter import *
from tkinter import ttk
import string

class Calculator():
    
    def __init__(self):
        self.root = Tk()
        
        #----- GUI -----#       
        # Configure the screen
        self.root.title("Calculator")
        self.root.geometry("624x224")
        self.root.resizable(width=False, height=False)

        # Customize buttons and entry style
        style = ttk.Style()
        
        style.configure("TButton",
                        font="Serif 15",
                        padding=8,
                        width=12,
                        )
        
        style.configure("TEntry",
                        font="Serif 18",
                        padding=8)
        #--- Entry ---#
        # Create text entry box
        self.entry_value = StringVar(self.root, value="")
        self.entry = ttk.Entry(self.root,
                               textvariable=self.entry_value,
                               width=75,
                               justify=RIGHT)
       
        self.entry.grid(row=0, column=0, columnspan=3, sticky=W)
        self.focus_entry()

        #--- Buttons ---#
        # Create clear entry button
        ttk.Button(self.root, text="Clear", command=lambda: self.clear_entry(), padding=4, takefocus=False).grid(row=0, column=3) 

        # Create button section
        ttk.Button(self.root, text="7", command=lambda: self.button_press("7"), takefocus=False).grid(row=1, column=0)
        ttk.Button(self.root, text="8", command=lambda: self.button_press("8"), takefocus=False).grid(row=1, column=1)
        ttk.Button(self.root, text="9", command=lambda: self.button_press("9"), takefocus=False).grid(row=1, column=2)
        ttk.Button(self.root, text="/", command=lambda: self.button_press("/"), takefocus=False).grid(row=1, column=3)

        ttk.Button(self.root, text="4", command=lambda: self.button_press("4"), takefocus=False).grid(row=2, column=0)
        ttk.Button(self.root, text="5", command=lambda: self.button_press("5"), takefocus=False).grid(row=2, column=1)
        ttk.Button(self.root, text="6", command=lambda: self.button_press("6"), takefocus=False).grid(row=2, column=2)
        ttk.Button(self.root, text="×", command=lambda: self.button_press("*"), takefocus=False).grid(row=2, column=3)

        ttk.Button(self.root, text="1", command=lambda: self.button_press("1"), takefocus=False).grid(row=3, column=0)
        ttk.Button(self.root, text="2", command=lambda: self.button_press("2"), takefocus=False).grid(row=3, column=1)
        ttk.Button(self.root, text="3", command=lambda: self.button_press("3"), takefocus=False).grid(row=3, column=2)
        ttk.Button(self.root, text="-", command=lambda: self.button_press("-"), takefocus=False).grid(row=3, column=3)

        ttk.Button(self.root, text=".", command=lambda: self.button_press("."), takefocus=False).grid(row=4, column=0)
        ttk.Button(self.root, text="0", command=lambda: self.button_press("0"), takefocus=False).grid(row=4, column=1)
        ttk.Button(self.root, text="=", command=lambda: self.calculate(), takefocus=False).grid(row=4, column=2)
        ttk.Button(self.root, text="+", command=lambda: self.button_press("+"), takefocus=False).grid(row=4, column=3)

        #----- Input Handeling -----#
        #Handle keyboard input
        self.root.bind("<Return>", self.calculate)
        self.root.bind("<Delete>", self.clear_entry)
        self.root.bind("<Key>", self.check_entry)
        self.root.bind("<Escape>", self.close_window)

        #start mainloop
        self.root.mainloop()

    #----- Functions -----#
    def focus_entry(self, *args):
        #Places the cursor at the end of the entry
        self.entry.focus()
        self.entry.icursor(END)


    def clear_entry(self, *args):
        #resluts in an empty entry and places the cursor here
        self.entry_value.set("")
        self.focus_entry()

    
    def check_entry(self, *args):
        #after adding something to the entry check if it was valid, if not remove it from the entry
        entry_value = self.entry_value.get()

        #--if entry shows "invalid input" remove it from the entry
        if entry_value[:13] == "Invalid input":
            print("invalid is there!")
            if len(entry_value) == 13:
                entry_value = ""
            else:
                entry_value = entry_value[13:]

        new_entry = entry_value

        #--check for invalid inputs
        if len(entry_value)> 0:
            added_input = entry_value[-1]
            if added_input in string.ascii_letters or added_input in "\'\"!@#$&_[]{}|\\:;?":
                new_entry = entry_value[:-1]
            elif added_input == ',':
                new_entry = entry_value[:-1] + "."

                
        self.entry_value.set(new_entry)
        self.focus_entry()


    def button_press(self, value):
        # Adds the given value to the entry
        result = self.entry_value.get()

        #--removes replace "Invalid input" or "0' in the entry
        if(result == "Invalid input" or result == "0"):
            result = ""
            
        result += value
        self.entry_value.set(result)
        self.focus_entry()


    def calculate(self, *args):
        # evaluate input, show error if impossible
        to_calc = self.entry_value.get()
        
        try:
            result = eval(to_calc)
        except SyntaxError:
            result = "Invalid input"
            print(result)
     
        # turn whole number floats into integers
        if result != "Invalid input":
            if float(result).is_integer():
                result = int(result)

        # turn result into string and display to entry    
        self.entry_value.set(str(result))
        self.focus_entry()


    def close_window(self, *args):
        self.root.destroy()

             
def main():
    Calculator()
 

if __name__ == '__main__':
    main()





