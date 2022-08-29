import tkinter as tk
import tkinter.font as font


#root1 = tk.Tk()
#myFont = font.Font(family="Lato", slant="normal", s)


w = tk.Label(root1,
		 text="Bioinformatics",
		 fg = "red",
		 font="Times")
w1 = tk.Label(root1,
		 text="Biology",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic")
w2 = tk.Label(root1,
		 text="Computer Science",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold")
w.pack()
w1.pack()
w2.pack()
root1.mainloop()
