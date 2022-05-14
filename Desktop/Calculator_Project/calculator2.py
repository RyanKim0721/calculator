import tkinter as tk

window = tk.Tk()

entry = tk.Entry()
entry.grid(row=0,column=0, columnspan=4, sticky="ns")

first = tk.StringVar("")
second = tk.StringVar("")
operator = tk.StringVar("")
result = tk.IntVar(0)


def deleteAll():
    entry.delete(0, tk.END)
    first.set("")
    second.set("")
    operator.set("")
    result.set(0)


def doOperator(oper):
    operator.set(oper)
    entry.insert(tk.END, oper)


def getResult():
    if (operator.get() == "+"):
        entry.delete(0,tk.END)
        num = int(first.get()) + int(second.get())
        entry.insert(0, num)
    elif (operator.get() == "-"):
        entry.delete(0,tk.END)
        num = int(first.get()) - int(second.get())
        entry.insert(0, num)
    elif (operator.get() == "*"):
        entry.delete(0,tk.END)
        num = int(first.get()) * int(second.get())
        entry.insert(0, num)
    elif (operator.get() == "/"):
        entry.delete(0, tk.END)
        num = int(first.get()) / int(second.get())
        entry.insert(0, num)
    else:
        num2 =second.get() +first.get()
        second.set(num2)
        entry.insert(tk.END, num2)
first.set("")
second.set("")



def putVal(val):
    print("1")
    if(operator.get() == ""):
        entry.delete(0,tk.END)
        num = first.get() + val
        first.set(num)
        entry.insert(tk.END, num)
    else:
        second.set(val)
        entry.insert(tk.END, val)




def deleteAll():
    entry.delete(0, tk.END)
    first.set("")
    second.set("")
    operator.set("")
    result.set(0)




button = tk.Button(text="+",
          width="7",
          height="5",
          command=lambda: doOperator("+"))
button.grid(row=1, column=0)

button1 = tk.Button(text="-",
          width="7",
          height="5",
          command=lambda: doOperator("-"))
button1.grid(row=1, column=1)

button2 = tk.Button(text="x",
          width="7",
          height="5",
          command=lambda: doOperator("*"))
button2.grid(row=1, column=2)

button3 = tk.Button(text="/",
          width="7",
          height="5",
          command=lambda: doOperator("/"))
button3.grid(row=1, column=3)

button4 = tk.Button(text="7",
          width="7",
          height="5",
          command=lambda: putVal("7"))
button4.grid(row=2, column=0)

button5 = tk.Button(text="8",
          width="7",
          height="5",
          command=lambda: putVal("8"))
button5.grid(row=2, column=1)

button6 = tk.Button(text="9",
          width="7",
          height="5",
          command=lambda: putVal("9"))
button6.grid(row=2, column=2)

button7 = tk.Button(text="=",
          width="7",
          height="5",
          command=lambda: getResult())
button7.grid(row=2, column=3, rowspan=4)

button8 = tk.Button(text="4",
          width="7",
          height="5",
          command=lambda: putVal("4"))
button8.grid(row=3, column=0)

button9 = tk.Button(text="5",
          width="7",
          height="5",
          command=lambda: putVal("5"))
button9.grid(row=3, column=1)

button10 = tk.Button(text="6",
          width="7",
          height="5",
          command=lambda: putVal("6"))
button10.grid(row=3, column=2)

button11 = tk.Button(text="1",
          width="7",
          height="5",
          command=lambda: putVal("1"))
button11.grid(row=4, column=0)

button12 = tk.Button(text="2",
          width="7",
          height="5",
          command=lambda: putVal("2"))
button12.grid(row=4, column=1)

button13 = tk.Button(text="3",
          width="7",
          height="5",
          command=lambda: putVal("3"))
button13.grid(row=4, column=2)

button14 = tk.Button(text="0",
          width="7",
          height="5",
          command=lambda: putVal("0"))
button14.grid(row=5, column=0)

button15 = tk.Button(text=" ",
          width="7",
          height="5")
button15.grid(row=5, column=1)

button16 = tk.Button(text="AC",
          width="7",
          height="5",
          command=deleteAll)
button16.grid(row=5, column=2)




window.mainloop()
