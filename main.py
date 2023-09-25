from tkinter import *

window = Tk()
window.title('Calculator')
window.geometry("420x720")
input = Frame()
equation = StringVar()
expression = ""


def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)


def equal():
    try:
        global expression
        total = str(eval(expression))
        expression = total
        equation.set(total)


    except:
        equation.set(" error ")
        expression = ""


def clear():
    global expression
    expression = ""
    equation.set("")


def backspace():
    global expression
    expression = expression[0:-1]
    equation.set(expression)


input_frame1 = Frame(window, width=450, height=70, bd=0, highlightthickness=0, background="#212931")
input_frame2 = Frame(window, width=450, height=200, bd=0, highlightthickness=0)
input_frame1.pack(side=TOP, expand=FALSE, fill=BOTH)
input_frame2.pack(side=TOP, expand=FALSE, fill=BOTH)

input_field = Entry(input_frame2, font=('tahoma', 30), textvariable=equation, bg="#212931", bd=0, justify=LEFT,
                    fg='#FBF9FF')
input_field.pack(expand=FALSE, fill=BOTH)

frame1 = Frame(window, width=360, height=90, bd=0, highlightthickness=0, bg='yellow')
frame1.pack(side=TOP, expand=FALSE, fill=BOTH)
b_rb = (Button(frame1, bg='#5899E2', activebackground='#74AAE7', fg='#101519', activeforeground='#101519', text='(',
               width=2, height=6, relief=GROOVE, bd=0, command=lambda: press('(')).pack(side=LEFT, expand=TRUE,
                                                                                        fill=BOTH))
b_lb = (Button(frame1, bg='#5899E2', activebackground='#74AAE7', fg='#101519', activeforeground='#101519', text=')',
               width=3, height=6, relief=GROOVE, bd=0, command=lambda: press(')')).pack(side=LEFT, expand=TRUE,
                                                                                        fill=BOTH))
b_p = (Button(frame1, bg='#5899E2', activebackground='#74AAE7', fg='#101519', activeforeground='#101519', text='%',
              width=2, height=6, relief=GROOVE, bd=0, command=lambda: press('%')).pack(side=LEFT, expand=TRUE,
                                                                                       fill=BOTH))
b_c = (Button(frame1, bg='#5899E2', activebackground='#74AAE7', fg='#101519', activeforeground='#101519', text='C',
              width=2, height=6, relief=GROOVE, bd=0, command=clear).pack(side=LEFT, expand=TRUE, fill=BOTH))
b_ce = (Button(frame1, bg='#5899E2', activebackground='#74AAE7', fg='#101519', activeforeground='#101519', text='CE',
               width=2, height=6, relief=GROOVE, bd=0, command=backspace).pack(side=LEFT, expand=TRUE, fill=BOTH))

frame2 = Frame(window, bd=0, highlightthickness=0, bg='yellow')
frame2.pack(side=RIGHT, expand=FALSE, fill=BOTH)
b_d = (Button(frame2, bg='#5899E2', activebackground='#74AAE7', fg='#101519', font=('tahoma', 10),
              activeforeground='#101519', text='/', width=11, height=6, relief=GROOVE, bd=0,
              command=lambda: press('/')).pack(side=TOP, expand=TRUE,
                                               fill=BOTH))
b_m = (Button(frame2, bg='#5899E2', activebackground='#74AAE7', fg='#101519', font=('tahoma', 10),
              activeforeground='#101519', text='x', width=11, height=6, relief=GROOVE, bd=0,
              command=lambda: press('*')).pack(side=TOP, expand=TRUE,
                                               fill=BOTH))
b_s = (Button(frame2, bg='#5899E2', activebackground='#74AAE7', fg='#101519', font=('tahoma', 10),
              activeforeground='#101519', text='_', width=11, height=6, relief=GROOVE, bd=0,
              command=lambda: press('-')).pack(side=TOP, expand=TRUE,
                                               fill=BOTH))
b_a = (Button(frame2, bg='#5899E2', activebackground='#74AAE7', fg='#101519', font=('tahoma', 10),
              activeforeground='#101519', text='+', width=11, height=6, relief=GROOVE, bd=0,
              command=lambda: press('+')).pack(side=TOP, expand=TRUE,
                                               fill=BOTH))

frame3 = Frame(window, bd=0, highlightthickness=0, bg='yellow')
frame3.pack(side=TOP, expand=TRUE, fill=BOTH)
b7 = (Button(frame3, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='7', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(7)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b8 = (Button(frame3, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='8', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(8)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b9 = (Button(frame3, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='9', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(9)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))

frame4 = Frame(window, bd=0, highlightthickness=0, bg='yellow')
frame4.pack(side=TOP, expand=TRUE, fill=BOTH)
b4 = (Button(frame4, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='4', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(4)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b5 = (Button(frame4, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='5', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(5)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b6 = (Button(frame4, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='6', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(6)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))

frame5 = Frame(window, bd=0, highlightthickness=0, bg='yellow')
frame5.pack(side=TOP, expand=TRUE, fill=BOTH)
b1 = (Button(frame5, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='1', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(1)).pack(side=LEFT, expand=TRUE, fill=BOTH))
b2 = (Button(frame5, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='2', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(2)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b3 = (Button(frame5, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='3', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(3)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))

frame6 = Frame(window, bd=0, highlightthickness=0, bg='yellow')
frame6.pack(side=TOP, expand=TRUE, fill=BOTH)
b_f = (Button(frame6, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
              activeforeground='#FBF9FF', text='.', width=15, height=6, relief=GROOVE, bd=0,
              command=lambda: press('.')).pack(side=LEFT,
                                               expand=TRUE,
                                               fill=BOTH))
b0 = (Button(frame6, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
             activeforeground='#FBF9FF', text='0', width=15, height=6, relief=GROOVE, bd=0,
             command=lambda: press(0)).pack(side=LEFT, expand=TRUE,
                                            fill=BOTH))
b_e = (Button(frame6, bg='#181F25', activebackground='#202931', fg='#FBF9FF', font=('tahoma', 10),
              activeforeground='#FBF9FF', text='=', width=15, height=6, relief=GROOVE, bd=0, command=equal).pack(
    side=LEFT,
    expand=TRUE,
    fill=BOTH))
window.mainloop()
