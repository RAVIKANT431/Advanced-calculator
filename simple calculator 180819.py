import tkinter as tk
import math
win=tk.Tk()
win.title('Mini-Calculator')
win.resizable(False,False)
from tkinter import ttk
#globally delcare the expression
exp=""
equation=tk.StringVar()   #to show in text viewer entry box
ans_val=tk.StringVar()

def press(num):
    global exp
    exp=exp+str(num)
    equation.set(exp)

def pressT(num):
    global exp
    exp=exp+"math."+str(num)
    equation.set(exp)

def del_last():
    global exp
    dv=equation.get()
##    print(dv)
    if dv=='Error':
        equation.set("")
        exp=""
    else:
        del_dv=dv[:-1]
        exp=del_dv
        equation.set(del_dv)

def evaluate():
    global exp
    a=ans_val.get()
    b=equation.get()
##    print('a',a)
##    print('b',b)
    if a!=b:
        equation.set("")
        
        print("equal condition")
    
    try:
        global exp
        total=str(eval(exp))
        ans_val.set(total)
        equation.set(total)
        exp=""
    except:

        equation.set("Error")
        exp=""
def ans():
    global exp
    val=ans_val.get()
    exp=exp+val
##    print(exp)
    equation.set(exp)


def clear():
    global exp
    exp=""
    equation.set("")
entr=ttk.LabelFrame(win,text="Ravikant")
entr.grid()
text_output=ttk.Entry(entr,textvariable=equation,font="Arial 15",justify="right")
text_output.grid(column=0,row=0,ipadx=50,ipady=10)
#buttons
LF=ttk.LabelFrame(win)
LF.grid(column=0,row=2)
button_cal=ttk.Button(LF,text='(',command=lambda : press("(")).grid(column=0,row=1)
button_cal=ttk.Button(LF,text='7',command=lambda : press(7)).grid(column=0,row=2)
button_cal=ttk.Button(LF,text='4',command=lambda : press("4")).grid(column=0,row=3)
button_cal=ttk.Button(LF,text='1',command=lambda : press("1")).grid(column=0,row=4)
button_cal=ttk.Button(LF,text='0',command=lambda : press("0")).grid(column=0,row=5)
button_cal=ttk.Button(LF,text=')',command=lambda : press(")")).grid(column=1,row=1)
button_cal=ttk.Button(LF,text='8',command=lambda : press("8")).grid(column=1,row=2)
button_cal=ttk.Button(LF,text='5',command=lambda : press("5")).grid(column=1,row=3)
button_cal=ttk.Button(LF,text='2',command=lambda : press("2")).grid(column=1,row=4)
button_cal=ttk.Button(LF,text='.',command=lambda : press(".")).grid(column=1,row=5)
button_cal=ttk.Button(LF,text='^',command=lambda : press("**")).grid(column=2,row=1)
button_cal=ttk.Button(LF,text='9',command=lambda : press("9")).grid(column=2,row=2)
button_cal=ttk.Button(LF,text='6',command=lambda : press("6")).grid(column=2,row=3)
button_cal=ttk.Button(LF,text='3',command=lambda : press("3")).grid(column=2,row=4)
button_cal=ttk.Button(LF,text='clear',command=clear).grid(column=2,row=5)
button_cal=ttk.Button(LF,text='/',command=lambda : press("/")).grid(column=3,row=1)
button_cal=ttk.Button(LF,text='*',command=lambda : press("*")).grid(column=3,row=2)
button_cal=ttk.Button(LF,text='-',command=lambda : press("-")).grid(column=3,row=3)
button_cal=ttk.Button(LF,text='+',command=lambda : press("+")).grid(column=3,row=4)
button_cal=ttk.Button(LF,text='=',command=evaluate).grid(column=3,row=6)
button_cal=ttk.Button(LF,text='del',command=lambda: del_last()).grid(column=3,row=5)
button_cal=ttk.Button(LF,text='ans',command=lambda: ans()).grid(column=2,row=6)
#trigonometry button
tri_label=ttk.LabelFrame(win,text="Trigonometry")#.grid(column=1,row=0,rowspan=5)
tri_label.grid(column=1,row=0,rowspan=5)
button_cal=ttk.Button(tri_label,text='sin',command=lambda : pressT("sin(")).grid(column=0,row=1)
button_cal=ttk.Button(tri_label,text='cos',command=lambda : pressT("cos(")).grid(column=0,row=2)
button_cal=ttk.Button(tri_label,text='tan',command=lambda : pressT("tan(")).grid(column=0,row=3)
button_cal=ttk.Button(tri_label,text='sinh',command=lambda : pressT("sinh(")).grid(column=1,row=1)
button_cal=ttk.Button(tri_label,text='cosh',command=lambda : pressT("cosh(")).grid(column=1,row=2)                                            
button_cal=ttk.Button(tri_label,text='tanh',command=lambda : pressT("tanh(")).grid(column=1,row=3)

win.mainloop()

