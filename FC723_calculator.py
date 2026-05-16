"Calculator Application"
import tkinter as tk
import math 

window=tk.Tk()
window.title("Simple Calculator")


equation_text=""
display_text=""
equation_label = tk.StringVar() 
   
label=tk.Label(window,textvariable= equation_label, width=35,borderwidth=5, height=3)
label.pack()

root=tk.Frame(window)
root.pack()


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
# button_clear=tk.Button(root, text="Clear All",padx=50, pady=20, command=button_clear_all)
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


