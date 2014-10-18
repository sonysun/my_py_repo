__author__ = 'sonysun'

import math

accum = '0'   #accumulator of numbers
result = '0'  #where we get our result
memory = '0'  #memory of the calc


# allows to enter numbers in the way of concatenation
def digit_enter(char):
    global accum
    global screen
    if accum == '0' and char.isdigit() :
        accum = char
    elif accum == '0' and char == '.':
        accum = '0.'
    elif accum != '0' and '.' in list(accum) and char == '.':
        pass
    else:
        accum = accum + char




# allows to enter arithmetical signs and calculate intermediate result
def sign_enter(sign):
    global accum
    global result
    if result[-1].isdigit() or result[-1] == '.':
        result = accum + sign
    else:
        result = str(eval(result+accum)) + sign
    accum = '0'


# calculates the result
def calculate():
    global result
    global accum
    if result[-1].isdigit() or result[-1] == '.':
        result = result
    else:
        result = str(eval(result+accum))


# 1/x
def fraction_one():
    global accum
    accum = '1/' + accum

def square_root():
    global accum
    accum = str(math.sqrt(float(accum)))

# -x
def negative():
    global accum
    accum = '-' + accum

def percent():
    global accum
    global result
    accum = str(float(accum)/100.0)

def ce():
    global accum
    accum = '0'

def e():
    global result
    global accum
    result ='0'
    accum = '0'


def backspace():
    global accum
    if len(list(accum)) > 1:
        accum = accum[:-1]
    else:
        accum = 0

#-- memory functions --#
def memory_set():
    global accum
    global memory
    memory = accum

def memory_recover():
    global accum
    global memory
    accum = memory

def memory_reset():
    global memory
    memory = '0'

def memory_plus():
    global accum
    global memory
    memory = str(float(memory) + float(accum))

def memory_minus():
    global accum
    global memory
    memory = str(float(memory) + float(accum))






