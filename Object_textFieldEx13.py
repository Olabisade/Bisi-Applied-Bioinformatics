import tkinter as tk


def Text_Output():
    text1.insert(1.0, "This is a good idea\n")
    Content = text1.get(1.0, "end")
    label1.config(text="")
    label2.config(text="")
    print(Content)
    print(repr(Content))

def Insert_text_Begining():
    label1.config(text="You pressed the second button1")
    text1.insert(1.0, "Super")

def Insert_text_end():
    label1.config(text="You pressed the second button2")
    text1.insert("end", "Great")

def Text_Clear():
    label1.config(text="You pressed the second button3")
    text1.delete(1.0, "end")

def Text_length():
    label1.config(
    text="Your text has " + str(len(text1.get(1.0, "end-1c"))) + " characters"
    )


root = tk.Tk()

text1 = tk.Text(root, background="blue")
text1.pack()

button1 = tk.Button(root, text = "Insert text at the beginning", command = Insert_text_Begining)
button1.pack()
button2 = tk.Button(root, text = "Insert text at the end", command = Insert_text_end)
button2.pack()
button3 = tk.Button(root, text = "Clear text", command = Text_Clear)
button3.pack()
button4 = tk.Button(root, text = "print text", command = Text_Output)
button4.pack()
button5 = tk.Button(root, text = "length of text", command = Text_length)
button5.pack()

label1 = tk.Label(root, text = "")
label2 = tk.Label(root, text = "")
label1.pack()
label2.pack()

root.mainloop()
