import tkinter as tk
import tkinter.font as Font

def display_choice():
    labelx.config(text = "Type in your sequence, please")

def count_G():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label1.config(text = input1.get().upper().count("G"))
    if checking == "PROTEIN":
        label1.config(text = "This is not possible with a protein sequence")

def count_A():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label2.config(text = input1.get().upper().count("A"))
    if checking == "PROTEIN":
        label2.config(text = "This is not possible with a protein sequence")

def count_C():
    checking = var.get()
    if checking == "DNA" or checking == "RNA":
        label3.config(text = input1.get().upper().count("C"))
    if checking == "PROTEIN":
        label3.config(text = "This is not possible with a protein sequence")

def count_T():
    checking = var.get()
    if checking == "DNA":
        label4.config(text = input1.get().upper().count("T"))
    if checking == "PROTEIN" or checking == "RNA":
        label4.config(text = "Oops!, there can't be a T in here")

def count_U():
    checking = var.get()
    if checking == "RNA":
        label5.config(text = input1.get().upper().count("U"))
    if checking == "PROTEIN" or checking == "DNA":
        label5.config(text = "Oops! there can't be a U in here")

def count_AGT():
    checking = var.get()
    if checking == "PROTEIN":
        label6.config(text = input1.get().upper().count(""))
    if checking == "RNA" or checking == "DNA":
        label6.config(text = "This is not a protein sequence!")

def count_all():
    checking = var.get()
    if checking == "All":
        label7.config(text = input1.get().upper().count("G", "U", "T", "C", "A"))


root = tk.Tk()

var = tk.StringVar()
var.set("DNA")
labelA = tk.Label(root, text="choose your option")
labelA.pack()
radio1 = tk.Radiobutton(
    root, text="DNA",
    variable=var,
    value="DNA",
    command=display_choice)
radio1.pack()
radio2 = tk.Radiobutton(root,
    text="RNA",
    variable=var,
    value="RNA",
    command=display_choice)
radio2.pack()
radio3 = tk.Radiobutton(root,
    text="PROTEIN",
    variable=var,
    value="PROTEIN",
    command=display_choice)
radio3.pack()

radio4 = tk.Radiobutton(root,
    text="",
    variable=var,
    value="",
    command=display_choice)
radio4.pack()

labelx =tk.Label(root, text ="Type in your sequence, please")
labelx.pack()

input1 = tk.StringVar()
edit1 = tk.Entry(root, textvariable = input1)
edit1.pack()

button1 = tk.Button(root, text = "Click here to count G", bg = "red", fg = "snow", command=count_G)
button1.pack()
label1 = tk.Label(root, text ="")
label1.pack()

button2 = tk.Button(root, text = "Click here to count A", bg = "green",
                    fg = "snow", command=count_A)
button2.pack()
label2 = tk.Label(root, text ="")
label2.pack()

button3 = tk.Button(root, text = "Click here to count C", bg = "purple",
                    fg = "snow", command=count_C)
button3.pack()
label3 = tk.Label(root, text ="")
label3.pack()

button4 = tk.Button(root, text = "Click here to count T", bg = "pink",
                    fg = "snow", command=count_T)
button4.pack()
label4 = tk.Label(root, text ="")
label4.pack()

button5 = tk.Button(root, text = "Click here to count U", bg = "brown",
                    fg = "snow", command=count_U)
button5.pack()
label5 = tk.Label(root, text ="")
label5.pack()

button6 = tk.Button(root, text = "Click here to count AGT", bg = "blue",
                    fg = "snow", command=count_AGT)
button6.pack()
label6 = tk.Label(root, text ="")
label6.pack()

button7 = tk.Button(root, text = "Click here to count all", bg = "white",
                    fg = "black", command=count_all)
button7.pack()
label7 = tk.Label(root, text ="")
label7.pack()

root.mainloop()
