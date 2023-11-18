import tkinter as tk

window = tk.Tk()
window.minsize(width = 500, height = 500)
firstore = ''
secstore = ''
secstore = ''
'''secondstore = '' 
'''
order = 0
line = 1
secline = 1
intfirstore = 0
intsecstore = 0
char = 0
oprord = 0

def Button_check(button_press):

    global firstore, secstore, line, secstore, order, intfirstore, intsecstore, char, oprord
    button = int(button_press)
    i = 1

    Button_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    while i != 0:
    
        if button < 10 and button == Button_list[button]:
            order = str(button)
            print(button)
            if line == 1:
                firstore = firstore + order
                lb1.configure(text = firstore)
                char += 1
            else:
                secstore = secstore + order
                lb2.configure(text = secstore)
                char += 1
            '''
        elif button == 2:
            order = '2'
            print(button)
            if line == 1:
                firstore = firstore + order
                lb1.configure(text = firstore)
                char += 1
            else:
                secstore = secstore + order
                lb2.configure(text = secstore)
                char += 1
            '''
        elif button == 10: #Remove number
            if line == 1:
                inputstore = firstore
                newstore = remove_Character(inputstore, char - 1)
                print("new number: ", newstore)
                firstore = newstore
                char -= 1
                lb1.configure(text = firstore)
            else:
                inputstore = secstore
                newstore = remove_Character(inputstore, char - 1)
                print("new number: ", newstore)
                secstore = newstore
                char -= 1
                lb2.configure(text = secstore)
        elif button == 11: #Plus
            oprord = button
            line_Change()
            oprlb.config(text = ' + ')
            print("line has changed to: {}".format(line))
        elif button == 12: #Minus
            oprord = button
            line_Change()
            oprlb.config(text = ' - ')
            print("line has changed to: {}".format(line))
        elif button == 13: #Multi
            oprord = button
            line_Change()
            oprlb.config(text = ' x ')
            print("line has changed to: {}".format(line))
        elif button == 14: #Divid
            oprord = button
            line_Change()
            oprlb.config(text = ' ÷ ')
            print("line has changed to: {}".format(line))

        i = not i
        print('character: {}'.format(char))
    
    if button == 15: #Equal
        
        if oprord == 11: #plus
            a = int(firstore)
            b = int(secstore)
            ans = a + b
            print('{} + {} = {}'.format(a, b, ans))
            lb3.configure(text = ans)
        elif oprord == 12: #minus
            a = int(firstore)
            b = int(secstore)
            ans = a - b
            print('{} + {} = {}'.format(a, b, ans))
            lb3.configure(text = ans)
        elif oprord == 13: #multi
            a = int(firstore)
            b = int(secstore)
            ans = a * b
            print('{} + {} = {}'.format(a, b, ans))
            lb3.configure(text = ans)
        elif oprord == 14: #divid
            a = int(firstore)
            b = int(secstore)
            ans = a / b
            print('{} + {} = {}'.format(a, b, ans))
            lb3.configure(text = ans)
    
    elif button == 16: #AC
        clear()

def line_Change():
    global line, secline, char
    b = 0
    while b != 1:
        line = line + secline
        print("line: {}".format(line))
        b = not b
    char = 0

def clear(): 
    global firstore, secstore, line, char
    firstore = ''
    secstore = ''
    lb1.config(text = '')
    lb2.config(text = '')
    lb3.config(text = '')
    oprlb.config(text = '')
    line = 1
    char = 0
    print('RESET! \nline has changed to: {}'.format(line))

def remove_Character(str, i):
	
	if i == 0:
		return str[1:]
    
	return str[0] + remove_Character(str[1:], i - 1)
b0 = tk.Button(master = window, text = '  0  ', command = lambda m = "0" : Button_check(m))
b1 = tk.Button(master = window, text = '  1  ', command = lambda m = "1" : Button_check(m))
b2 = tk.Button(master = window, text = '  2  ', command = lambda m = "2" : Button_check(m))
b3 = tk.Button(master = window, text = '  3  ', command = lambda m = "3" : Button_check(m))
b4 = tk.Button(master = window, text = '  4  ', command = lambda m = "4" : Button_check(m))
b5 = tk.Button(master = window, text = '  5  ', command = lambda m = "5" : Button_check(m))
b6 = tk.Button(master = window, text = '  6  ', command = lambda m = "6" : Button_check(m))
b7 = tk.Button(master = window, text = '  7  ', command = lambda m = "7" : Button_check(m))
b8 = tk.Button(master = window, text = '  8  ', command = lambda m = "8" : Button_check(m))
b9 = tk.Button(master = window, text = '  9  ', command = lambda m = "9" : Button_check(m))
delb = tk.Button(master = window, text = ' C ', command = lambda m = "10" : Button_check(m))
plusb = tk.Button(master = window, text = ' + ', command = lambda m = "11" : Button_check(m))
minus = tk.Button(master = window, text = '  - ', command = lambda m = "12" : Button_check(m))
multi = tk.Button(master = window, text = '  x ', command = lambda m = "13" : Button_check(m))
divid = tk.Button(master = window, text = '  ÷ ', command = lambda m = "14" : Button_check(m))
testb = tk.Button(master = window, text = ' = ', command = lambda m = "15" : Button_check(m))
clearb = tk.Button(master = window, text = ' AC ', command = lambda m = "16" : Button_check(m))
blancb = tk.Button(master = window, text = ' ( ) ', command = lambda m = "17" : Button_check(m))
percentb = tk.Button(master = window, text = ' % ', command = lambda m = "18" : Button_check(m))
decimalb = tk.Button(master = window, text = ' . ', command = lambda m = "19" : Button_check(m))
lb1 = tk.Label(master = window, text = '')
lb2 = tk.Label(master = window, text = '')
lb3 = tk.Label(master = window, text = '')
oprlb = tk.Label(master = window, text = '')

lb1.grid(row = 0, column = 3)
oprlb.grid(row = 1, column = 3)
lb2.grid(row = 2, column = 3)
lb3.grid(row = 3, column = 3)
#Num buttons
b0.grid(row = 9, column = 1)
b1.grid(row = 8, column = 0)
b2.grid(row = 8, column = 1)
b3.grid(row = 8, column = 2)

b4.grid(row = 7, column = 0)
b5.grid(row = 7, column = 1)
b6.grid(row = 7, column = 2)

b7.grid(row = 6, column = 0)
b8.grid(row = 6, column = 1)
b9.grid(row = 6, column = 2)

delb.grid(row = 5, column = 2)
plusb.grid(row = 8, column = 3)
minus.grid(row = 7, column = 3)
multi.grid(row = 6, column = 3)
divid.grid(row = 5, column = 3)
testb.grid(row = 9, column = 3)
clearb.grid(row = 9, column = 2)
blancb.grid(row = 5, column = 0)
percentb.grid(row = 5, column = 1)
decimalb.grid(row = 9, column = 0)

window.mainloop()