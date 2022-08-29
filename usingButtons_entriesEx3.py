import tkinter as tk

def changeLabel1():
    label1.config(text="Bioinformatics")

def changeLabel2():
    label2.config(text="Biology")

def changeLabel3():
    label3.config(text="Science")

def userChange1():
    label1.config(text=input1.get())

def userChange2():
    label2.config(text=input2.get())

def userChange3():
    label3.config(text=input3.get())

root = tk.Tk()

input1 =tk.StringVar()
input2 =tk.StringVar()
input3 =tk.StringVar()
edit1 =tk.Entry(root, textvariable = input1)
edit2 =tk.Entry(root, textvariable = input2)
edit3 =tk.Entry(root, textvariable = input3)
edit1.pack()
edit2.pack()
edit3.pack()

label1 = tk.Label(root, text = "data")
label2 = tk.Label(root, text = "statistics")
label3 = tk.Label(root, text = "computer")
label1.pack()
label2.pack()
label3.pack()

button1 = tk.Button(root, text = "Click botton 1!", command=userChange1)
button1.pack()
button2 = tk.Button(root, text = "Click botton 2!", command=userChange2)
button2.pack()
button3 = tk.Button(root, text = "Click botton 3!", command=userChange3)
button3.pack()

root.mainloop()
