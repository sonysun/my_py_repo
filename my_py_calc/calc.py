__author__ = 'sonysun'

from tkinter import *
import calc_functions



# creating main window
root = Tk()
root.title('PyCalc by '+ __author__)
root.resizable(False, False)
screen = StringVar()
screen.set('0')
button_list = []


# placing and specifying widgets
calc_screen = Label(root, textvariable=screen, width=25, height=2,
    anchor=E, wraplength=175).grid(row = 1, column = 1, columnspan = 5)

button_01 = Button(root, text = 'MC', width=4, height=2)
button_01.grid(row = 2, column = 1)
button_list.append(button_01)
button_02 = Button(root, text = 'MR', width=4, height=2)
button_02.grid(row = 2, column = 2)
button_list.append(button_02)
button_03 = Button(root, text = 'MS', width=4, height=2)
button_03.grid(row = 2, column = 3)
button_list.append(button_03)
button_04 = Button(root, text = 'M+', width=4, height=2)
button_04.grid(row = 2, column = 4)
button_list.append(button_04)
button_05 = Button(root, text = 'M-', width=4, height=2)
button_05.grid(row = 2, column = 5)
button_list.append(button_05)

button_06 = Button(root, text = '\u2190', width=4, height=2)
button_06.grid(row = 3, column = 1)
button_list.append(button_06)
button_07 = Button(root, text = 'CE', width=4, height=2)
button_07.grid(row = 3, column = 2)
button_list.append(button_07)
button_08 = Button(root, text = 'C', width=4, height=2)
button_08.grid(row = 3, column = 3)
button_list.append(button_08)
button_09 = Button(root, text = '\u00B1', width=4, height=2)
button_09.grid(row = 3, column = 4)
button_list.append(button_09)
button_10 = Button(root, text = '\u221A', width=4, height=2)
button_10.grid(row = 3, column = 5)
button_list.append(button_10)

button_11 = Button(root, text = '7', width=4, height=2)
button_11.grid(row = 4, column = 1)
button_list.append(button_11)
button_12 = Button(root, text = '8', width=4, height=2)
button_12.grid(row = 4, column = 2)
button_list.append(button_12)
button_13 = Button(root, text = '9', width=4, height=2)
button_13.grid(row = 4, column = 3)
button_list.append(button_13)
button_14 = Button(root, text = '/', width=4, height=2)
button_14.grid(row = 4, column = 4)
button_list.append(button_14)
button_15 = Button(root, text = '%', width=4, height=2)
button_15.grid(row = 4, column = 5)
button_list.append(button_15)

button_16 = Button(root, text = '4', width=4, height=2)
button_16.grid(row = 5, column = 1)
button_list.append(button_16)
button_17 = Button(root, text = '5', width=4, height=2)
button_17.grid(row = 5, column = 2)
button_list.append(button_17)
button_18 = Button(root, text = '6', width=4, height=2)
button_18.grid(row = 5, column = 3)
button_list.append(button_18)
button_19 = Button(root, text = '*', width=4, height=2)
button_19.grid(row = 5, column = 4)
button_list.append(button_19)
button_20 = Button(root, text = '1/x', width=4, height=2)
button_20.grid(row = 5, column = 5)
button_list.append(button_20)

button_21 = Button(root, text = '1', width=4, height=2)
button_21.grid(row = 6, column = 1)
button_list.append(button_21)
button_22 = Button(root, text = '2', width=4, height=2)
button_22.grid(row = 6, column = 2)
button_list.append(button_22)
button_23 = Button(root, text = '3', width=4, height=2)
button_23.grid(row = 6, column = 3)
button_list.append(button_23)
button_24 = Button(root, text = '-', width=4, height=2)
button_24.grid(row = 6, column = 4)
button_list.append(button_24)
button_25 = Button(root, text = '=', width=4, height=5)
button_25.grid(row = 6, column = 5, rowspan = 2)
#button_list.append(button_25)

button_26 = Button(root, text = '0', width=10, height=2)
button_26.grid(row = 7, column = 1, columnspan = 2)
button_list.append(button_26)
button_27 = Button(root, text = '.', width=4, height=2)
button_27.grid(row = 7, column = 3)
button_list.append(button_27)
button_28 = Button(root, text = '+', width=4, height=2)
button_28.grid(row = 7, column = 4)
button_list.append(button_28)


# binding functions to buttons
button_01.bind("<Button-1>", lambda event: calc_functions.memory_reset())
button_02.bind("<Button-1>", lambda event: calc_functions.memory_recover())
button_03.bind("<Button-1>", lambda event: calc_functions.memory_set())
button_04.bind("<Button-1>", lambda event: calc_functions.memory_plus())
button_05.bind("<Button-1>", lambda event: calc_functions.memory_minus())

button_06.bind("<Button-1>", lambda event: calc_functions.backspace())
button_07.bind("<Button-1>", lambda event: calc_functions.ce())
button_08.bind("<Button-1>", lambda event: calc_functions.e())
button_09.bind("<Button-1>", lambda event: calc_functions.negative())
button_10.bind("<Button-1>", lambda event: calc_functions.square_root())

button_11.bind("<Button-1>", lambda event: calc_functions.digit_enter('7'))
button_12.bind("<Button-1>", lambda event: calc_functions.digit_enter('8'))
button_13.bind("<Button-1>", lambda event: calc_functions.digit_enter('9'))
button_14.bind("<Button-1>", lambda event: calc_functions.sign_enter('/'))
button_15.bind("<Button-1>", lambda event: calc_functions.percent())

button_16.bind("<Button-1>", lambda event: calc_functions.digit_enter('4'))
button_17.bind("<Button-1>", lambda event: calc_functions.digit_enter('5'))
button_18.bind("<Button-1>", lambda event: calc_functions.digit_enter('6'))
button_19.bind("<Button-1>", lambda event: calc_functions.sign_enter('*'))
button_20.bind("<Button-1>", lambda event: calc_functions.fraction_one())

button_21.bind("<Button-1>", lambda event: calc_functions.digit_enter('1'))
button_22.bind("<Button-1>", lambda event: calc_functions.digit_enter('2'))
button_23.bind("<Button-1>", lambda event: calc_functions.digit_enter('3'))
button_24.bind("<Button-1>", lambda event: calc_functions.sign_enter('-'))
button_25.bind("<Button-1>", lambda event: calc_functions.calculate())

button_26.bind("<Button-1>", lambda event: calc_functions.digit_enter('0'))
button_27.bind("<Button-1>", lambda event: calc_functions.digit_enter('.'))
button_28.bind("<Button-1>", lambda event: calc_functions.sign_enter('+'))



for button in button_list:
    button.bind("<ButtonRelease>", lambda event: screen.set(calc_functions.accum))


button_25.bind("<ButtonRelease>", lambda event: screen.set(calc_functions.result))


root.mainloop()
