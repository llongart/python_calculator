from tkinter import Frame, Label, Button, StringVar, PhotoImage
from memory import *
from math import sqrt, modf
from os import path

class Calculator(Frame):

############################################## CONSTRUCTOR #################################################
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Eventos del teclado
        self.master.bind('<Key>', self.push_key)        
        
        self.initialize_globals()

        self.frame1 = self.create_frames('#252526')
        self.frame2 = self.create_frames('#252526')
        self.frame3 = self.create_frames('#252526')
        self.frame4 = self.create_frames('#252526')

        self.create_labels(self.frame1, self.frame2)
        self.create_buttons()   

############################################### VARIABLES ##################################################
    def initialize_globals(self):
        # Constants
        self.NO_HIDEABLE_BUTTONS = (1, 2, 3, 4, 5, 6)

        # Toogle button images
        self.ON_PATH = path.abspath('./Calculator-python-OO/images/on.png')
        self.OFF_PATH = path.abspath('./Calculator-python-OO/images/off.png')

        # Global variables
        self.historial = StringVar()
        self.output_screen = StringVar()
        self.reset_screen = False
        self.show_memory = False
        self.is_on = True
        self.on  = PhotoImage(file = self.ON_PATH)
        self.off = PhotoImage(file = self.OFF_PATH)
        self.count = 0
        self.color = ('#252526', '#3F3F41', '#7A7A7E', '#ACACB0', '#EEEEEE', '#FFF5EE')

        # Button list from frames
        self.button_list = list()

        # Memory Class
        self.memory = Memory()

################################################ FRAMES ####################################################
    def create_frames(self, bg_color = None):
        frame = Frame(self, bg = bg_color)
        frame.pack(expand = True, fill = 'both')
        return frame

################################################ LABELS ####################################################        
    def create_labels(self, master1, master2):
        # Label DarkMode
        self.label_darkmode = Label(master1)
        self.label_darkmode.config(
            text = 'Dark Mode', 
            font = ("Tahoma",  7, "italic"), 
            bg = '#252526', 
            fg = 'White', 
            width = 7
        )
        self.label_darkmode.grid(row = 0, column = 0)
        
        # Label Historial
        self.label_historial = Label(master1)
        self.label_historial.config(
            font = ("Tahoma",  11), 
            anchor = 'e',
            bg = '#252526', 
            fg = 'White',
            width = 28
        )
        self.label_historial.grid(row = 0, column = 30, padx = 10)

        # Label Screen
        self.label_screen = Label(master2)
        self.label_screen.config(
            text = "0",
            font = ("Tahoma",  43), 
            justify = 'right',
            bg = '#252526', 
            fg = 'White',
            width = 10,
            relief = 'flat',
            anchor = 'e'
        )
        self.label_screen.pack(padx = 1, pady = 1)        

################################################ BUTTONS ###################################################
    def create_buttons(self):       
        # Boton cambio modo oscuro/claro 
        self.button_toggle = Button(self.frame1, command = lambda: self.switch_dark_mode(self.button_toggle))
        self.button_toggle.config(
            image = self.on, 
            bg = '#252526',
            relief = 'flat',
            bd = 0, 
            activebackground = '#252526', 
            activeforeground = '#252526'
        )
        self.button_toggle.grid(row = 0, column = 1, padx = 2)

        # Boton borrar toda la memoria
        self.button_mc = Button(self.frame3, command = lambda: self.push_memory_clear(self.button_mc, self.button_mr, self.button_m_down))
        self.button_mc.config(
            text = "MC",
            font = ("Tahoma", 10, "bold"),
            width = 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            state = 'disabled',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_mc.grid(row = 0, column = 0, padx = 1, pady = 1)

        # Boton recuperar memoria
        self.button_mr = Button(self.frame3, command = self.push_memory_recover)
        self.button_mr.config(
            text = "MR",
            font = ("Tahoma", 10, "bold"),
            width = 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            state = 'disabled',
            activebackground = '#252526',
            activeforeground = 'White'    
        )
        self.button_mr.grid(row = 0, column = 1, padx = 1, pady = 1)

        # Boton sumar a la memoria
        self.button_m_plus = Button(self.frame3, command = lambda: self.push_memory_plus(self.button_mc, self.button_mr, self.button_m_down))
        self.button_m_plus.config(
            text = "M+",
            font = ("Tahoma", 10, "bold"),
            width= 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'    
        )
        self.button_m_plus.grid(row = 0, column = 2, padx = 1, pady = 1)

        # Boton restar a la memoria
        self.button_m_minus = Button(self.frame3, command = lambda: self.push_memory_minus(self.button_mc, self.button_mr, self.button_m_down))
        self.button_m_minus.config(
            text = "M-",
            font = ("Tahoma", 10, "bold"),
            width= 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'    
        )
        self.button_m_minus.grid(row = 0, column = 3, padx = 1, pady = 1)

        # Boton almacenar memoria
        self.button_ms = Button(self.frame3, command = lambda: self.push_memory_store(self.button_mc, self.button_mr, self.button_m_down))
        self.button_ms.config(
            text = "MS",
            font = ("Tahoma", 10, "bold"),
            width= 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'    
        )
        self.button_ms.grid(row = 0, column = 4, padx = 1, pady = 1)

        # Boton mostrar memoria
        self.button_m_down = Button(self.frame3, command = self.push_show_memory)
        self.button_m_down.config(
            text = "Mˇ",
            font = ("Tahoma", 10, "bold"),
            width= 5,
            height= 1,
            bg = '#252526', #Gris claro
            fg = 'White',    
            relief = 'flat',
            state = 'disabled',
            activebackground = '#252526',
            activeforeground = 'White'    
        )
        self.button_m_down.grid(row = 0, column = 5, padx = 1, pady = 1)

        # Button %
        self.button_percentage = Button(self.frame4, command = self.push_button_percentage)
        self.button_percentage.config(
            text = "%",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'        
        )
        self.button_percentage.grid(row = 0, column = 0, padx = 2, pady = 2)

        # Button CE
        self.button_reset_last = Button(self.frame4, command = self.push_button_ce)
        self.button_reset_last.config(
            text = "CE",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,    
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White',    
        )
        self.button_reset_last.grid(row = 0, column = 1, padx = 2, pady = 2)

        # Button C
        self.button_reset_all = Button(self.frame4, command = self.push_button_c)
        self.button_reset_all.config(
            text = "C",
            font = ("Tahoma", 18),
            width= 5,
            height= 1, 
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_reset_all.grid(row = 0, column = 2, padx = 2, pady = 2)

        # Button DELETE
        self.button_delete = Button(self.frame4, command = self.push_button_delete)
        self.button_delete.config(
            text = "◄",
            font = ("Tahoma", 18),
            width= 5,
            height= 1, 
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_delete.grid(row = 0, column = 3, padx = 2, pady = 2)

        # Button ¹∕ₓ
        self.button_denom = Button(self.frame4, command = self.push_button_denom)
        self.button_denom.config(
            text = "¹∕ₓ",
            font = ("Tahoma", 18, "italic"),
            width= 5,
            height= 1,
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_denom.grid(row = 1, column = 0, padx = 2, pady = 2)

        # Button x²
        self.button_square = Button(self.frame4, command = self.push_button_square)
        self.button_square.config(
            text = "x²",
            font = ("Tahoma", 18, "italic"),
            width= 5,
            height= 1,    
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_square.grid(row = 1, column = 1, padx = 2, pady = 2)

        # Button √x
        self.button_sqrt = Button(self.frame4, command = self.push_button_sqrt)
        self.button_sqrt.config(
            text = "√x",
            font = ("Tahoma", 18, "italic"),
            width= 5,
            height= 1,    
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_sqrt.grid(row = 1, column = 2, padx = 2, pady = 2)

        # Button ÷
        self.button_division = Button(self.frame4, command = self.push_button_division)
        self.button_division.config(
            text = "÷",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,   
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_division.grid(row = 1, column = 3, padx = 2, pady = 2)

        # Button 7
        self.button_7 = Button(self.frame4, command = lambda: self.push_button_number(7))
        self.button_7.config(
            text = "7",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_7.grid(row = 2, column = 0, padx = 2, pady = 2)

        # Button 8
        self.button_8 = Button(self.frame4, command = lambda: self.push_button_number(8))
        self.button_8.config(
            text = "8",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,  
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_8.grid(row = 2, column = 1, padx = 2, pady = 2)

        # Button 9
        self.button_9 = Button(self.frame4, command = lambda: self.push_button_number(9))
        self.button_9.config(
            text = "9",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White' 
        )
        self.button_9.grid(row = 2, column = 2, padx = 2, pady = 2)

        # Button x
        self.button_multiply = Button(self.frame4, command = self.push_button_multiply)
        self.button_multiply.config(
            text = "x",
            font = ("Tahoma", 18),
            width= 5,
            height= 1, 
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_multiply.grid(row = 2, column = 3, padx = 2, pady = 2)

        # Button 4
        self.button_4 = Button(self.frame4, command = lambda: self.push_button_number(4))
        self.button_4.config(
            text = "4",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_4.grid(row = 3, column = 0, padx = 2, pady = 2)

        # Button 5
        self.button_5 = Button(self.frame4, command = lambda: self.push_button_number(5))
        self.button_5.config(
            text = "5",
            font = ("Tahoma", 18),
            width= 5,
            height= 1, 
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_5.grid(row = 3, column = 1, padx = 2, pady = 2)

        # Button 6
        self.button_6 = Button(self.frame4, command = lambda: self.push_button_number(6))
        self.button_6.config(
            text = "6",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_6.grid(row = 3, column = 2, padx = 2, pady = 2)

        # Button -
        self.button_subtract = Button(self.frame4, command = self.push_button_subtract)
        self.button_subtract.config(
            text = "-",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#131313', #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_subtract.grid(row = 3, column = 3, padx = 2, pady = 2)

        # Button 1
        self.button_1 = Button(self.frame4, command = lambda: self.push_button_number(1))
        self.button_1.config(
            text = "1",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_1.grid(row = 4, column = 0, padx = 2, pady = 2)

        # Button 2
        self.button_2 = Button(self.frame4, command = lambda: self.push_button_number(2))
        self.button_2.config(
            text = "2",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White' 
        )
        self.button_2.grid(row = 4, column = 1, padx = 2, pady = 2)

        # Button 3
        self.button_3 = Button(self.frame4, command = lambda: self.push_button_number(3))
        self.button_3.config(
            text = "3",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_3.grid(row = 4, column = 2, padx = 2, pady = 2)

        # Button +
        self.button_add = Button(self.frame4, command = self.push_button_add)
        self.button_add.config(
            text = "+",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#131313', #Negro claro #Negro claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White' 
        )
        self.button_add.grid(row = 4, column = 3, padx = 2, pady = 2)

        # Button +/-
        self.button_plus_minus = Button(self.frame4, command = self.push_button_plus_minus)
        self.button_plus_minus.config(
            text = "+/-",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_plus_minus.grid(row = 5, column = 0, padx = 2, pady = 2)

        # Button 0
        self.button_0 = Button(self.frame4, command = lambda: self.push_button_number(0))
        self.button_0.config(
            text = "0",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White' 
        )
        self.button_0.grid(row = 5, column = 1, padx = 2, pady = 2)

        # Button comma
        self.button_comma = Button(self.frame4, command = self.push_button_comma)
        self.button_comma.config(
            text = ",",
            font = ("Tahoma", 18),
            width= 5,
            height= 1, 
            bg = 'Black',
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_comma.grid(row = 5, column = 2, padx = 2, pady = 2)

        # Button =
        self.button_equal = Button(self.frame4, command = self.push_button_equal)
        self.button_equal.config(
            text = "=",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_equal.grid(row = 5, column = 3, padx = 2, pady = 2)

        # Boton Memoria 1
        self.button_memory1 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory1))
        self.button_memory1.config(
            text = "M1",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory1.grid(row = 0, column = 3, padx = 2, pady = 2)
        self.button_memory1.lower()

        # Boton Memoria 2
        self.button_memory2 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory2))
        self.button_memory2.config(
            text = "M2",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory2.grid(row = 1, column = 3, padx = 2, pady = 2)
        self.button_memory2.lower()

        # Boton Memoria 3
        self.button_memory3 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory3))
        self.button_memory3.config(
            text = "M3",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory3.grid(row = 2, column = 3, padx = 2, pady = 2)
        self.button_memory3.lower()

        # Boton Memoria 4
        self.button_memory4 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory4))
        self.button_memory4.config(
            text = "M4",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory4.grid(row = 3, column = 3, padx = 2, pady = 2)
        self.button_memory4.lower()

        # Boton Memoria 5
        self.button_memory5 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory5))
        self.button_memory5.config(
            text = "M5",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory5.grid(row = 4, column = 3, padx = 2, pady = 2)
        self.button_memory5.lower()

        # Boton Memoria 6
        self.button_memory6 = Button(self.frame4, command = lambda: self.push_button_memory(self.button_memory6))
        self.button_memory6.config(
            text = "M6",
            font = ("Tahoma", 18),
            width= 5,
            height= 1,
            bg = '#19425e', #Azul claro
            fg = 'White',    
            relief = 'flat',
            activebackground = '#252526',
            activeforeground = 'White'
        )
        self.button_memory6.grid(row = 5, column = 3, padx = 2, pady = 2)
        self.button_memory6.lower()

############################################### FUNCTIONS ##################################################
    
    # Funcionalidad boton reset_all
    def push_button_c(self):
        self.label_historial["text"] = ""
        self.label_screen["text"] = "0"

    # Funcionalidad boton delete
    def push_button_delete(self):
        self.historial.set(self.label_historial["text"])
        if (self.historial.get().find("=") > 0 or self.reset_screen == True):
            self.label_screen["text"] = "0"

        last_pos = len(self.label_screen["text"]) - 1
        self.label_screen["text"] = str(self.label_screen["text"])[0: last_pos]

        if ((str(self.label_screen["text"])).find('-') > -1 and last_pos == 1) or last_pos == 0:
            self.label_screen["text"] = "0"

    # Funcionalidad boton plus_minus  
    def push_button_plus_minus(self):
        if (self.label_screen["text"] != "0" and str(self.label_screen["text"]).find('-') == -1):
            self.label_screen["text"] = "-" + self.label_screen["text"]
        else:
            self.label_screen["text"] = str(self.label_screen["text"]).replace('-', '')

    # Funcionalidad boton_comma
    def push_button_comma(self):
        self.historial.set(self.label_historial["text"])
        if (self.historial.get().find("=") > 0):
            self.label_historial["text"] = ""
            self.label_screen["text"] = "0,"

        if (str((self.label_screen["text"])).find(',') == -1):
            self.label_screen["text"] += ","

    # Funcionalidad para resetear historial
    def reset_historial(self):
        
        self.historial.set(self.label_historial["text"])
        if (self.historial.get().find("=") > 0):
            self.label_historial["text"] = ""  

    # Funcionalidad para setear operador aritmético            
    def set_operator(self, operator):
        self.label_historial["text"] += self.label_screen["text"] + operator
        self.label_screen["text"] = "0"
        self.reset_screen = True

    # Funcionalidad para mostrar resultado en Entry
    def show_result(self):   
        self.label_screen["text"] = ""
        self.historial.set(self.label_historial["text"])
        
        # Reemplazo de caracteres en cadena Historial para poder 
        # usar la ecuación correctamente en la función eval()
        #
        # Reemplazar operador de multiplicación
        self.historial.set(self.historial.get().replace('x', '*'))
        # Reemplazar operador de división
        self.historial.set(self.historial.get().replace('÷', '/'))
        # Reemplazar caracter de comma
        self.historial.set(self.historial.get().replace(',', '.'))
        # Reemplazar opción elevado al cuadrado
        self.historial.set(self.historial.get().replace(')²', '**2)'))
        # Reemplazar opción de raiz cuadrada
        self.historial.set(self.historial.get().replace('√', 'sqrt'))
        # Reemplazar opción de porcentaje
        self.historial.set(self.historial.get().replace('%', '/100'))

        # Validar division entre cero
        if(self.historial.get().find('/  0') > 0 or self.historial.get().find('/(0)') > 0):
            self.label_historial["text"] = "No se puede dividir entre cero"
            self.label_screen["text"] = "0"
            return

        # Ejecutar operación aritmética y devolver resultado en dos decimales
        # si el valor decimal es mayor a 0, sino solo muestra la parte entera
        result = "{0:.2f}".format(eval(self.historial.get()))
        decimal, entero = modf(float(result))
        if (abs(decimal) > 0):
            self.label_screen["text"] = str(result).replace('.', ',')
        else:
            self.label_screen["text"] = str(entero).replace('.0', '')

        self.label_historial["text"] += " = "
        self.reset_screen = True

    # Funcionalidad para botones de numeros
    def push_button_number(self, number):
        if (len(self.label_screen["text"]) > 9): # No introducir mas de 10 digitos en pantalla
            return

        self.reset_historial()

        if(self.label_screen["text"] == "0" or self.reset_screen):
            self.label_screen["text"] = str(number)
            self.reset_screen = False
            return

        self.label_screen["text"] += str(number)

    # Funcionalidad boton reset_last
    def push_button_ce(self):
        self.reset_historial()
        self.label_screen["text"] = "0"

    # Funcionalidad boton igual
    def push_button_equal(self):
        self.historial.set(self.label_historial["text"])
        if (self.historial.get().find("=") > 0):
            return
                
        self.label_historial["text"] += self.label_screen["text"]
        self.show_result()

    # Funcionalidad boton denominador
    def push_button_denom(self):
        self.label_historial["text"] += " 1/(" + self.label_screen["text"] + ") "
        self.show_result()

    # Funcionalidad boton elevado al cuadrado
    def push_button_square(self):
        self.label_historial["text"] += " (" + self.label_screen["text"] + ")² "
        self.show_result()

    # Funcionalidad boton raiz cuadrada
    def push_button_sqrt(self):
        self.label_historial["text"] += " √(" + self.label_screen["text"] + ") "
        self.show_result()

    # Funcionalidad boton de porcentaje
    def push_button_percentage(self):
        self.label_historial["text"] += self.label_screen["text"] + "% "
        self.show_result()

    def push_key(self, event):       
        if(event.char == 'c' or event.char == 'C'):
            self.push_button_c()

        if(event.char == '%'):
            self.push_button_percentage()    

        if(event.char == '/'):
            self.push_button_division()

        if(event.char == '*'):
            self.push_button_multiply()

        if(event.char == '-'):
            self.push_button_subtract()

        if(event.char == '+'):
            self.push_button_add()

        if(event.char in ('.', ',')):
            self.push_button_comma()

        if(event.char == '\r'):   #"ENTER"
            self.push_button_equal()

        if(event.char == '\x08'): #"BACKSPACE"
            self.push_button_delete()

        if(event.keycode in range(48, 58)): # botones del 0 al 9:
            self.push_button_number(event.char)              


    # Funcionalidad boton operador division
    def push_button_division(self):  
        self.reset_historial()   
        self.set_operator(' ÷ ')

    # Funcionalidad boton operador multiplicación
    def push_button_multiply(self):
        self.reset_historial()    
        self.set_operator(' x ')        

    # Funcionalidad boton operador restar
    def push_button_subtract(self):
        self.reset_historial()      
        self.set_operator(' - ')         

    # Funcionalidad boton operador sumar
    def push_button_add(self):        
        self.reset_historial()    
        self.set_operator(' + ')

    # # Habilitar boton MC, MR, Mˇ
    def push_memory_plus(self, button_mc, button_mr, button_m_down):     
        number = str(self.label_screen["text"]).replace(',', '.')
        if len(self.memory.get_memory()) == 0:
            self.memory.insert_to_memory(float(number)) 
        else: 
            self.memory.add_to_last_memory(float(number))

        button_mc["state"] = button_mr["state"] = button_m_down["state"] = 'active'
        self.reset_screen = True

    # Habilitar boton MC, MR, Mˇ
    def push_memory_minus(self, button_mc, button_mr, button_m_down):
        number = str(self.label_screen["text"]).replace(',', '.')
        if len(self.memory.get_memory()) == 0:
            self.memory.insert_to_memory(float(number) * -1) 
        else: 
            self.memory.subtract_to_last_memory(float(number))

        button_mc["state"] = button_mr["state"] = button_m_down["state"] = 'active'
        self.reset_screen = True

    # Desabilitar boton MC, MR, Mˇ
    def push_memory_clear(self, button_mc, button_mr, button_m_down):
        self.memory.reset_memory()
        button_mc["state"] = button_mr["state"] = button_m_down["state"] = 'disabled' 

    # Recuperar memoria
    def push_memory_recover(self):
        result = "{0:.2f}".format(self.memory.recover_last_memory())
        decimal, entero = modf(float(result))

        if (abs(decimal) > 0):
            self.label_screen["text"] = str(result).replace('.', ',')
        else:
            self.label_screen["text"] = str(entero).replace('.0', '')    

        self.reset_screen = True

    # Almacenar en la mermoria
    def push_memory_store(self, button_mc, button_mr, button_m_down):
        number = str(self.label_screen["text"]).replace(',', '.')
        self.memory.insert_to_memory(float(number))
        button_mc["state"] = button_mr["state"] = button_m_down["state"] = 'active'
        self.reset_screen = True

    # Mostrar contenido de la memoria
    def push_show_memory(self): 
        self.button_list = self.frame4.grid_slaves()   

        i = 1
        j = 5
        # Asignar el valor de la memoria a los botones correspondientes
        # i itera sobre el indice de la memoria
        # j itera sobre los botones de memoria empezando desde el boton
        # superior DELETE hasta el boton =
        for number in self.memory.get_memory():
            if i > 6:
                return
            else:
                result = "{0:.2f}".format(number)
                decimal, entero = modf(float(result))
                if (abs(decimal) > 0):
                    self.button_list[j]["text"] = str(result).replace('.', ',')
                else:
                    self.button_list[j]["text"] = str(entero).replace('.0', '')

                self.button_list[j].lift()
                j -= 1

            i += 1

        # i itera sobre los botones que se esconden al mostrar la memoria
        # mientras se asignan los colores de letras y botones dependiendo del
        # modo oscuro/claro. Los demas botones son puestos en disabled
        i = 1
        for my_button in self.button_list:
            if i not in self.NO_HIDEABLE_BUTTONS:
                my_button['fg'] = 'black'
                my_button['state'] = 'disabled'
            else:
                if self.is_on:
                    my_button['fg'] = 'white'
                    my_button['bg'] = '#19425e' #AZUL CLARO
                else:
                    my_button['fg'] = 'black'
                    my_button['bg'] = '#FF6448' #NARANJA

            i += 1   
        
        self.show_memory = True

    # Asignación del valor seleccionado de la memoria a la pantalla
    def push_button_memory(self, button):
        self.label_screen["text"] = str(button["text"]).replace('.', ',')

        self.button_list = self.frame4.grid_slaves()

        # i itera sobre los botones que se esconden al mostrar la memoria
        # mientras se asignan los colores de letras dependiendo del
        # modo oscuro/claro. Los demas botones son puestos en normal y se 
        # muestran con lift()
        i = 1
        button_range = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+/-", ",", "=")
        for mybutton in self.button_list:
            if i not in self.NO_HIDEABLE_BUTTONS:
                if self.is_on:
                    mybutton['fg'] = 'White'
                else:
                    if mybutton["text"] not in button_range:
                        mybutton['fg'] = '#FF4500'
                    else:
                        mybutton['fg'] = '#252526'

                mybutton['state'] = 'normal'
                mybutton.lift()
            i += 1

        self.show_memory = False 

    # Alternar modo oscuro/claro
    def switch_dark_mode(self, button):        
        button_frame3 = self.frame3.grid_slaves()
        self.button_list = self.frame4.grid_slaves()

        button_range1 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", 
                        "+/-", ",", "=", "M1", "M2", "M3", "M4", "M5", "M6")
        button_range2 = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+/-", ",")

        if self.is_on: # DARK MODE OFF
            # Todos los frames, labels y botones pasan a modo claro
            # i itera sobre todos los botones en los frames 3 y 4
            button.config(
                image = self.off, 
                bg = '#FFF5EE', 
                activebackground = '#FFF5EE', 
                activeforeground = '#FFF5EE'
            )
            
            self.is_on = False

            self.fade_in(button_range1, button_range2, button_frame3)
                    
        else: # DARK MODE ON (DEFAULT)
            button.config(
                image = self.on, 
                bg = '#252526', 
                activebackground = '#252526', 
                activeforeground = '#252526'
            )

            self.is_on = True
            self.fade_out(button_range1, button_range2, button_frame3)

    def fade_out(self, button_range1, button_range2, button_frame3):
        if self.count <= 6 and self.count > 0:                    
            self.count -= 1
            self.frame1.config(bg = self.color[self.count])
            self.frame2.config(bg = self.color[self.count])
            self.frame3.config(bg = self.color[self.count])
            self.frame4.config(bg = self.color[self.count])
            self.label_darkmode.config(bg = self.color[self.count], fg = 'white', state = 'normal')
            self.label_historial.config(bg = self.color[self.count], fg = 'white', state = 'normal')
            self.label_screen.config(bg = self.color[self.count], fg = 'white', state = 'normal')   
            i = 1
            for my_button in self.button_list:
                if my_button["text"] not in button_range1:
                    my_button.config(
                        bg = '#131313', 
                        fg = 'white', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    )      

                if my_button["text"] == "=":
                    my_button.config(
                        bg = '#19425e', 
                        fg = 'white', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    )  

                if my_button["text"] in button_range2:
                    my_button.config(
                        bg = 'Black', 
                        fg = 'white', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    )

                if i in self.NO_HIDEABLE_BUTTONS and self.show_memory:
                    if self.is_on:
                        my_button.config(bg = '#19425e', fg = 'white') 
                    else:
                        my_button.config(bg = '#FF6448', fg = 'black')

                i += 1
            for my_button in button_frame3:
                my_button.config(
                    bg = '#252526', 
                    fg = 'white', 
                    activebackground = '#252526', 
                    activeforeground = 'White'
            )            

            self.master.after(1, self.fade_out(button_range1, button_range2, button_frame3)) 

    def fade_in(self, button_range1, button_range2, button_frame3):
        if self.count < 6:
            self.frame1.config(bg = self.color[self.count])
            self.frame2.config(bg = self.color[self.count])
            self.frame3.config(bg = self.color[self.count])
            self.frame4.config(bg = self.color[self.count])
            self.label_darkmode.config(bg = self.color[self.count], fg = '#252526', state = 'disabled')
            self.label_historial.config(bg = self.color[self.count], fg = '#252526', state = 'disabled')
            self.label_screen.config(bg = self.color[self.count], fg = '#252526', state = 'disabled')      
            self.count += 1

            i = 1
            for my_button in self.button_list:
                if my_button["text"] not in button_range1:
                    my_button.config(
                        bg = '#FAF0E6', 
                        fg = '#FF4500', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    )
                
                if my_button["text"] == "=":
                    my_button.config(
                        bg = '#FF6448', 
                        fg = 'white', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    ) 

                if my_button["text"] in button_range2:
                    my_button.config(
                        bg = 'white', 
                        fg = '#252526', 
                        activebackground = '#252526', 
                        activeforeground = 'White'
                    )

                if i in self.NO_HIDEABLE_BUTTONS and self.show_memory:
                    if self.is_on:
                        my_button.config(bg = 'black', fg = 'black')
                    else:
                        my_button.config(bg = '#FF6448', fg = 'black')   
                i += 1
            for my_button in button_frame3:
                my_button.config(
                    bg = '#FFF5EE', 
                    fg = '#252526', 
                    activebackground = '#FFF5EE', 
                    activeforeground = '#252526'
            )

            self.master.after(1, self.fade_in(button_range1, button_range2, button_frame3))