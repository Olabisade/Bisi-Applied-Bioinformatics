import tkinter as tk
def Choice():
    label_frame2.config(text="Centre")

root = tk.Tk()
root.geometry('600x500')
label_frame1 = tk.LabelFrame(root, text = "Head", labelanchor="s", relief=tk.RIDGE) #s=south
label_frame1.pack()
label_frame2 = tk.LabelFrame(root, text = "Centre", labelanchor="sw") #s=south
label_frame2.pack()
label_frame3 = tk.LabelFrame(root, text = "Tail", labelanchor="se", relief=tk.RIDGE) #s=south
label_frame3.pack()
var = tk.IntVar()
var1 = tk.IntVar()
radio1 = tk.Radiobutton(label_frame1, text = "Click 1",variable = var,
            value = 1, bg="blue", fg="snow",
            indicator=0,
            width=20)
radio1.pack()
radio2 = tk.Radiobutton(label_frame1, text = "Click 2",variable = var,
            value = 1, bg="blue", fg="snow", indicator=0,
            width=20)
radio2.pack()
radio3 = tk.Radiobutton(label_frame1, text = "Click 3",variable = var,
            value = 1, bg="blue", fg="snow", indicator=0,
            width=20)
radio3.pack()
button1 = tk.Button(label_frame2, text = "Button 1",
        command=Choice, bg="green", fg="snow")
button1.pack()
button2 = tk.Button(label_frame2, text = "Button 2",
        command=Choice, bg="green", fg="snow")
button2.pack()
button3 = tk.Button(label_frame2, text = "Button 3",
        command=Choice, bg="green", fg="snow")
button3.pack()
radio4 = tk.Radiobutton(label_frame3, text = "Option 1",variable = var1,
            value = 3, bg="purple", fg="snow")
radio4.pack()
radio5 = tk.Radiobutton(label_frame3, text = "Option 2",variable = var1,
            value = 3, bg="purple", fg="snow")
radio5.pack()
radio6 = tk.Radiobutton(label_frame3, text = "Option 3",variable = var1,
            value = 3, bg="purple", fg="snow")
radio6.pack()

root.mainloop()
