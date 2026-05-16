"Calculator Application"
import tkinter as tk #importing the tkinter 
import math #importing the math module 

#defien function that will take the input when buttons pressed
def button_click(num):
    global equation_text, display_text
    
    available_functions = {
    'sin': "sin",
    'cos': "cos",
    'tan': "tan",
    "arcsin": "asin",
    "arccos": "acos",
    "arctan": "atan",
    "√":"sqrt"
     }
    #checking if the input is related to the existing functions in the dictionary
    if num in available_functions:
        equation_text+=str(f"math.{available_functions[num]}(")
        display_text+=str(num+"(")
       

    else:
        equation_text+=str(num)
        display_text+=str(num)
      
    equation_label.set(display_text)
#define function that will out the square of input     
def square():
    global equation_text,display_text
    
    equation_text=str(f"math.pow({equation_text}, 2)")
    
    display_text+=str("²")
    equation_label.set(display_text)
#defien function that will define output and output to the label 
def equals():
    global equation_text, display_text
    
    try:
        total=eval(equation_text)
        
        if isinstance(total, float): #checking for point-float issue 
            total = round(total, 10)
        
       
        equation_label.set(total)
        
        equation_text=total
        display_text=total
    except ZeroDivisionError: #checking for zere division error
        equation_label.set("Undefined")
        equation_text=""
        display_text=""
        
    except SyntaxError:  #checking for syntax errors
        equation_label.set("Undefined")
        display_text=""
        equation_text=""
        
    except ValueError: #cehcking for value errors
        equation_label.set("Undefined")
        
#define function that will clear the window label      
def button_clear():
   global equation_text, display_text
    
   equation_label.set("")
   equation_text=""
   
   display_text=""
   

window=tk.Tk() #assigning tkinter
window.title("Simple Calculator")


equation_text=""
display_text=""
equation_label = tk.StringVar()  
   
label=tk.Label(window,textvariable= equation_label, width=35,borderwidth=5, height=3)
label.pack() #packing label

root=tk.Frame(window) #creating frame 
root.pack()

#initializing the buttons with their command functions 
button_1=tk.Button(root,text='1',padx=25,pady=20,command=lambda: button_click(1))
button_2=tk.Button(root,text='2',padx=25,pady=20,command=lambda: button_click(2))
button_3=tk.Button(root,text='3',padx=25,pady=20,command=lambda: button_click(3))
button_4=tk.Button(root,text='4',padx=25,pady=20,command=lambda: button_click(4))
button_5=tk.Button(root,text='5',padx=25,pady=20,command=lambda: button_click(5))
button_6=tk.Button(root,text='6',padx=25,pady=20,command=lambda: button_click(6))
button_7=tk.Button(root,text='7',padx=25,pady=20,command=lambda: button_click(7))
button_8=tk.Button(root,text='8',padx=25,pady=20,command=lambda: button_click(8))
button_9=tk.Button(root,text='9',padx=25,pady=20,command=lambda: button_click(9))
button_0=tk.Button(root,text='0',padx=25,pady=20,command=lambda: button_click(0))
button_add=tk.Button(root,text='+',padx=25,pady=20,command= lambda: button_click("+"))
button_equal=tk.Button(root,text='=',padx=50,pady=20,command= equals)
button_delete=tk.Button(root,text='C',padx=25,pady=20,command= button_clear, bg="red")
button_dots=tk.Button(root, text=".", padx=25, pady=20, command=lambda: button_click("."))

button_subtract=tk.Button(root,text='-',padx=25,pady=20,command= lambda: button_click("-"))
button_multiply=tk.Button(root,text='*',padx=25,pady=20,command= lambda: button_click("*"))
button_divide=tk.Button(root,text='/',padx=25,pady=20,command= lambda: button_click("/"))


button_sin=tk.Button(root,text="sin", padx=25, pady=20, command= lambda: button_click("sin"))
button_cosine=tk.Button(root, text="cosin", padx=25, pady=20, command=lambda: button_click("cos"))
button_arcsin=tk.Button(root, text="arcsin", padx=25, pady=20, command= lambda: button_click("arcsin"))
button_arccos=tk.Button(root, text="arccos", padx=25, pady=20, command=lambda: button_click("arccos"))
button_arctan=tk.Button(root, text="arctan", padx=25, pady=20, command=lambda: button_click("arctan"))

button_tan=tk.Button(root, text="tan", padx=25, pady=20, command= lambda: button_click("tan"))
button_square=tk.Button(root, text="x²", padx=25, pady=20, command=lambda: square())
button_sq_root=tk.Button(root,text="√", padx=25, pady=20, command=lambda: button_click("√"))

button_parethesis=tk.Button(root, text="(", padx=25, pady=20, command=lambda: button_click("("))
button_parethesis_1=tk.Button(root, text=")", padx=25, pady=20, command=lambda: button_click(")"))

#arranging the buttons with grid() function 
button_parethesis.grid(row=1,column=2, sticky = "nsew" )
button_parethesis_1.grid(row=1,column=3, sticky="snew")
button_square.grid(row=1, column=1, sticky = "nsew")
button_sq_root.grid(row=1, column=0, sticky = "nsew")

button_sin.grid(row=2, column=0, sticky = "nsew")
button_cosine.grid(row=2, column=1, sticky = "nsew")
button_tan.grid(row=2, column=2, sticky = "nsew")
button_delete.grid(row=2,column=3, sticky = "nsew")

button_arcsin.grid(row=3,column=0, sticky = "nsew")
button_arccos.grid(row=3,column=1, sticky = "nsew")
button_arctan.grid(row=3, column=2, sticky = "nsew")
button_add.grid(row=3, column=3, sticky = "nsew")

button_7.grid(row=4, column=0, sticky = "nsew")
button_8.grid(row=4, column=1, sticky = "nsew")
button_9.grid(row=4, column=2, sticky = "nsew")
button_subtract.grid(row=4, column=3, sticky = "nsew")

button_4.grid(row=5, column=0, sticky = "nsew")
button_5.grid(row=5, column=1, sticky = "nsew")
button_6.grid(row=5, column=2, sticky = "nsew")
button_multiply.grid(row=5, column=3, sticky = "nsew")

button_1.grid(row=6, column=0, sticky = "nsew")
button_2.grid(row=6, column=1, sticky = "nsew")
button_3.grid(row=6, column=2, sticky = "nsew")
button_divide.grid(row=6, column=3, sticky = "nsew")

button_0.grid(row=7, column=0, sticky = "nsew")
button_dots.grid(row=7, column=1, sticky = "nsew")
button_equal.grid(row=7, column=2, columnspan = 2, sticky = "nsew")




root.mainloop() #the main loop for keeping the window open and running every element of the program
