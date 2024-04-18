import tkinter as tk

###############################################################################
# DONE: 1. (2 pts)
#
#   The todos in this module are in one comment because you will be modifying
#   the same bit of code each time. Here you will create a basic ATM
#   application that allows a user to withdraw funds and deposit funds
#
#   For this _todo_, you will create a window with the title "ATM" and call its
#   mainloop() method so it runs.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 2. (3 pts)
#
#   For this _todo_, you will create an area where the user's current balance
#   is displayed. There should be a label that says "Current Balance ($):" and
#   below it another label that has the dollar amount of their current balance
#   displayed. For the purposes of this problem, we will assume that all users
#   start out with 1000 dollars in their account. So, this label should start
#   out with "1000" as its text.
#
#   All of the elements on this window should be centered.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 3 (3 pts)
#
#   For this _todo_, create two more labels: one that says "Amount ($):" and
#   another that starts out empty beneath it. This is where the user's amount
#   that they will either withdraw or deposit will display.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 4. (7 pts)
#
#   For this _todo_, you will create all the buttons that the user needs:
#
#       - One for each digit 0-9
#       - A withdrawal button
#       - A deposit button
#
#   They should be in the standard configuration for a numberpad (see the
#   images in the README file on GitHub). Each button is 75px by 75px.
#
#   HINT: I used a frame to surround the buttons and grid for this.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (10 pts)
#
#   For this _todo_, using the command keyword on each button to have each
#   number button type that digit in the amount label above (just like you
#   would if you were typing in an amount). Pressing each button should add
#   that number to end of the text in the label.
#
#   HINT: I found that the easiest way to accomplish this was to use a
#   different handler for each button.
#
#   You also need a handler for the withdrawal and deposit buttons.
#
#   The withdrawal button should subtract the amount typed into the amount box
#   from the user's current balance. It should clear the amount label and
#   update the current balance label.
#
#   The deposit button should add the amount typed into the amount box to the
#   user's current balance. It should also clear the amount label and update
#   the current balance label.
#
#   Remember that, for these handlers, you will need to convert the strings in
#   the label's to floats before you do your calculations.
#
#   Once you have done this, then change the above _TODO_ to DONE.
#
#
# DONE: 5. (3 pts)
#
#   For this _todo_, bind the window to any keypress so that if the user types
#   a number, it also types that number into the amount label. Remember, you
#   can use isdigit() to check if the key pressed is a digit.
#
#   Once you have done this, then change the above _TODO_ to DONE.
###############################################################################

window = tk.Tk()
window.title("ATM")
balance_label = tk.Label(master=window, text="Current Balance ($):", justify="center")
balance_label.pack()
balance_lbl = tk.Label(master=window, text="1000", justify="center")
balance_lbl.pack()
amount_label = tk.Label(master=window, text="Amount ($):", justify="center")
amount_label.pack()
amount_lbl = tk.Label(master=window, text="", justify="center")
amount_lbl.pack()
window.columnconfigure([0, 1, 2], weight=1, minsize=75)
window.rowconfigure([0, 1, 2, 3], weight=1, minsize=75)
frame = tk.Frame(master=window)
frame.pack()
def handler1():
    amount_lbl["text"] += "1"
def handler2():
    amount_lbl["text"] += "2"
def handler3():
    amount_lbl["text"] += "3"
def handler4():
    amount_lbl["text"] += "4"
def handler5():
    amount_lbl["text"] += "5"
def handler6():
    amount_lbl["text"] += "6"
def handler7():
    amount_lbl["text"] += "7"
def handler8():
    amount_lbl["text"] += "8"
def handler9():
    amount_lbl["text"] += "9"
def handlerw():
    total_amount = float(amount_lbl["text"])
    total_balance = float(balance_lbl["text"])
    total_balance -= total_amount
    balance_lbl["text"] = str(total_balance)
    amount_lbl["text"] = ""
def handler0():
    amount_lbl["text"] += "0"
def handlerd():
    total_amount = float(amount_lbl["text"])
    total_balance = float(balance_lbl["text"])
    total_balance += total_amount
    balance_lbl["text"] = str(total_balance)
    amount_lbl["text"] = ""
def handle_keypress(event):
    if event.char.isdigit():
        amount_lbl["text"] += event.char
window.bind("<Key>", handle_keypress)
button1 = tk.Button(master=frame, text=1, relief="raised", width=7, height=3, padx=5, pady=5, command=handler1)
button1.grid(row=0, column=0, sticky="nsew")
button2 = tk.Button(master=frame, text=2, relief="raised", width=7, height=3, padx=5, pady=5, command=handler2)
button2.grid(row=0, column=1, sticky="nsew")
button3 = tk.Button(master=frame, text=3, relief="raised", width=7, height=3, padx=5, pady=5, command=handler3)
button3.grid(row=0, column=2, sticky="nsew")
button4 = tk.Button(master=frame, text=4, relief="raised", width=7, height=3, padx=5, pady=5, command=handler4)
button4.grid(row=1, column=0, sticky="nsew")
button5 = tk.Button(master=frame, text=5, relief="raised", width=7, height=3, padx=5, pady=5, command=handler5)
button5.grid(row=1, column=1, sticky="nsew")
button6 = tk.Button(master=frame, text=6, relief="raised", width=7, height=3, padx=5, pady=5, command=handler6)
button6.grid(row=1, column=2, sticky="nsew")
button7 = tk.Button(master=frame, text=7, relief="raised", width=7, height=3, padx=5, pady=5, command=handler7)
button7.grid(row=2, column=0, sticky="nsew")
button8 = tk.Button(master=frame, text=8, relief="raised", width=7, height=3, padx=5, pady=5, command=handler8)
button8.grid(row=2, column=1, sticky="nsew")
button9 = tk.Button(master=frame, text=9, relief="raised", width=7, height=3, padx=5, pady=5, command=handler9)
button9.grid(row=2, column=2, sticky="nsew")
buttonw = tk.Button(master=frame, text="Withdrawal", relief="raised", width=7, height=3, padx=5, pady=5, command=handlerw)
buttonw.grid(row=3, column=0, sticky="nsew")
button0 = tk.Button(master=frame, text=0, relief="raised", width=7, height=3, padx=5, pady=5, command=handler0)
button0.grid(row=3, column=1, sticky="nsew")
buttond = tk.Button(master=frame, text="Deposit", relief="raised", width=7, height=3, padx=5, pady=5, command=handlerd)
buttond.grid(row=3, column=2, sticky="nsew")
window.mainloop()