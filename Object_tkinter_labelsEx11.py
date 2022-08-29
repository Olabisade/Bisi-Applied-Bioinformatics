import tkinter as tk

root = tk.Tk()
w = tk.Label(root, text="Enzymes are proteins")
w1 = tk.Label(root, text="Small molecule drugs can be administered orally")    #case sensitive
w2 = tk.Label(root, text="Target engagement of compounds")
w.pack()
w1.pack()
w2.pack()
root.mainloop()

#example2
root1 = tk.Tk()

w = tk.Label(root1,
		 text="Red Text in Times Font",
		 fg = "red",
		 font="Times")
w1 = tk.Label(root1,
		 text="Green Text in Helvetica Font",
		 fg = "light green",
		 bg = "dark green",
		 font = "Helvetica 16 bold italic")
w2 = tk.Label(root1,
		 text="Blue Text in Verdana bold",
		 fg = "blue",
		 bg = "yellow",
		 font = "Verdana 10 bold")
w.pack()
w1.pack()
w2.pack()
root1.mainloop()
