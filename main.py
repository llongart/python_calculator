from tkinter import Tk
from calculator import *

# Create root panel
root = Tk()

# Icon
ICON_PATH = path.abspath('./Calculator-python-OO/images/calculator-icon.ico')

# Config root panel
root.title("Calculadora") 
root.geometry("315x460")
root.iconbitmap(ICON_PATH)
root.attributes('-topmost', True)
root.resizable(False, False)  

cal = Calculator(root)   
cal.mainloop()
    