from tkinter import *
from tkinter import ttk

import math 


#cores
color1="#2E2E2E" #black
color2="#FAF9F6" #white
color3="#37474F" #black2
color4= "#424345" #gray
color5="#00FF7F" #green
background= "#e8e6e6"



#Janela principal
window = Tk ()
window.title("Calculadora")
window.geometry("235x287")
window.config(bg=color1)

#criando frames

frame_screen = Frame(window, width=300, height=56, bg=color3)
frame_screen.grid(row=0,column=0)

frame_scientific = Frame(window, width=300, height=86)
frame_scientific.grid(row=1, column=0)

frame_body = Frame(window, width=300, height=340)
frame_body.grid(row=2, column=0)

#functions
global all_values

all_values = ''
text = StringVar()

#functions enter values ​​on screen

def enter_values(event):
    global all_values
    
    all_values = all_values + str(event)
    text.set(all_values)
    
#calculate function

def calculate():
    global all_values
    modules = ['math.tan','math.sin','math.cos','math.sqrt','math.log','math.log10','math.e','math.pow','math.pi']
    
    for i in modules:
        if i =='math.tan':
            all_values = all_values.replace("tan",i)
            
        if i =='math.sin':
            all_values = all_values.replace("sin",i)
            
        if i =='math.cos':
            all_values = all_values.replace("cos",i)

        if i =='math.sqrt':
            all_values = all_values.replace("sqrt",i)
            
        if i =='math.log':
            all_values = all_values.replace("log",i)
            
        if i =='math.log10':
            all_values = all_values.replace("log10",i)
            
        if i =='math.e':
            all_values = all_values.replace("e",i)
            
        if i =='math.pow':
            all_values = all_values.replace("pow",i)
            
        if i =='math.pi':
            all_values = all_values.replace("pi",i)
            
    result = str(eval(all_values))
    text.set(result)
    
    all_values = ''

#function clear window   
def clear_window():
    global all_values
    all_values = ''
    text.set("")
    


#Frame tela
label_window = Label(frame_screen, textvariable=text, width=16, height=2, padx= 7, anchor='e', bd=0, justify=RIGHT, font=('Ivy 18'), bg=color3, fg=color2)
label_window.place(x=1, y=0)

#Frame scientific
b_0 = Button(frame_scientific,command=lambda:enter_values('tan'),text="tan", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=0)
b_1 = Button(frame_scientific,command=lambda:enter_values('sin'),text="sin", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=0)
b_2 = Button(frame_scientific,command=lambda:enter_values('cos'),text="cos", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=0)
b_3 = Button(frame_scientific,command=lambda:enter_values('sqrt'),text="sqrt", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_3.place(x=177, y=0)

b_0 = Button(frame_scientific,command=lambda:enter_values('log'),text="log", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=29)
b_1 = Button(frame_scientific,command=lambda:enter_values('log10'),text="log10", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=29)
b_2 = Button(frame_scientific,command=lambda:enter_values('e'),text="e", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=29)
b_3 = Button(frame_scientific,command=lambda:enter_values('pow'),text="pow", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_3.place(x=177, y=29)

b_0 = Button(frame_scientific,command=lambda:enter_values('pi'),text="pi", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=58)
b_1 = Button(frame_scientific,command=lambda:enter_values(','),text=",", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=58)
b_2 = Button(frame_scientific,command=lambda:enter_values('('),text="(", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=58)
b_3 = Button(frame_scientific,command=lambda:enter_values(')'),text=")", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_3.place(x=177, y=58)

#frame body

b_0 = Button(frame_body,command=clear_window,text="C", width=14, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_0.place(x=0, y=0)
b_1 = Button(frame_body,command=lambda:enter_values('%'),text="%", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_1.place(x=118, y=0)
b_2 = Button(frame_body,command=lambda:enter_values('/'),text="/", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_2.place(x=177, y=0)

b_0 = Button(frame_body,command=lambda:enter_values('7'),text="7", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=29)
b_1 = Button(frame_body,command=lambda:enter_values('8'),text="8", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=29)
b_2 = Button(frame_body,command=lambda:enter_values('9'),text="9", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=29)
b_3 = Button(frame_body,command=lambda:enter_values('*'),text="*", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_3.place(x=177, y=29)

b_0 = Button(frame_body,command=lambda:enter_values('4'),text="4", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=58)
b_1 = Button(frame_body,command=lambda:enter_values('5'),text="5", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=58)
b_2 = Button(frame_body,command=lambda:enter_values('6'),text="6", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=58)
b_3 = Button(frame_body,command=lambda:enter_values('-'),text="-", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_3.place(x=177, y=58)

b_0 = Button(frame_body,command=lambda:enter_values('1'),text="1", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=87)
b_1 = Button(frame_body,command=lambda:enter_values('2'),text="2", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=59, y=87)
b_2 = Button(frame_body,command=lambda:enter_values('3'),text="3", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_2.place(x=118, y=87)
b_3 = Button(frame_body,command=lambda:enter_values('+'),text="+", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_3.place(x=177, y=87)

b_0 = Button(frame_body,command=lambda:enter_values('0'),text="0", width=14, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_0.place(x=0, y=116)
b_1 = Button(frame_body,command=lambda:enter_values('.'),text=".", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color2)
b_1.place(x=118, y=116)
b_2 = Button(frame_body,command=calculate,text="=", width=6, height=1 , relief=RAISED, overrelief=RIDGE, font=('Ivy 10 bold'), bg=color1, fg=color5)
b_2.place(x=177, y=116)




window.mainloop()
