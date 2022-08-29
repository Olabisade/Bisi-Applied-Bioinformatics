import tkinter as tk


def display_selected(choice):
    choice = var1.get()
    print(choice)
    label1.config(text=choice)

def change_bg(choice):
    label1.config(bg=var2.get())

def change_fg(choice):
    label1.config(fg=var3.get())

root = tk.Tk()

root.geometry("500x200")
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var1.set("NUAK1")
var2.set("light green")
var3.set("Blue")

menu1 = tk.OptionMenu(root, var1, "NUAK", "NUAK2", "FGFR1", "FGFR2", "FGFR3",
                        "POLQ", "KRAS", command=display_selected)
menu1.pack(side="left")
menu2 = tk.OptionMenu(root, var2, "light green", "black", "yellow", "orange", "pink",
                        "brown", "dark green", command=change_bg)
menu2.pack(side="left")
menu3 = tk.OptionMenu(root, var3, "blue", "light red", "red", "purple", "grey", "snow",
                        "white", "black", command=change_fg)
menu3.pack(side="left")

label1 = tk.Label(root, text=var1.get(), bg=var2.get(), fg=var3.get())
label1.pack(side="right")
root.mainloop()
