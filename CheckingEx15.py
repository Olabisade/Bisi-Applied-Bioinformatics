import tkinter as tk

def Print_Check():
    checking1 = checkValue1.get()
    checking2 = checkValue2.get()
    checking3 = checkValue3.get()
    checking4 = checkValue4.get()
    checking5 = checkValue5.get()
    if checking1:
        print("Your Check Box is activated")
    elif checking2:
        print("Your Check Box is activated")
    elif checking3:
        print("Your Check Box is activated")
    elif checking4:
        print("Your Check Box is activated")
    elif checking5:
        print("Your Check Box is activated")
    else:
        print("Your Check Box is inactivated")
    label1.config(text= "")


root = tk.Tk()

root.geometry("500x200")
checkValue1 = tk.StringVar()
checkValue1.set("Option1")

checkValue2 = tk.BooleanVar()
checkValue2.set(True)

checkValue3 = tk.BooleanVar()
checkValue3.set(False)

checkValue4 = tk.StringVar()
checkValue4.set("Colour1")

checkValue5 = tk.BooleanVar()
checkValue5.set(True)

check1 =tk.Checkbutton(root, text="Check Box 1", var=checkValue1)
check1.pack(side="left")
check2 =tk.Checkbutton(root, text="Check Box 1", var=checkValue2)
check2.pack(side="left")
check3 =tk.Checkbutton(root, text="Check Box 3", var=checkValue3)
check3.pack(side="left")
check4 =tk.Checkbutton(root, text="Check Box 4", var=checkValue4)
check4.pack(side="left")
check5 =tk.Checkbutton(root, text="Check Box 5", var=checkValue5)
check5.pack(side="left")


button1 = tk.Button(
root, text="Check your input", width=80, fg="blue", bg="grey", command=Print_Check
)

button1.pack(side="right")

label1 = tk.Label(root, text = "")
#label2 = tk.Label(root, text = "")
#label1.pack()
label1.pack()

root.mainloop()
