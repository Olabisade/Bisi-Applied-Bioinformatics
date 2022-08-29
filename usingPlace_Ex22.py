import tkinter as tk

root = tk.Tk()
root.geometry("500x600")
label1= tk.Label(root, text="Traveling by air", bg="blue", fg="snow")
label1.place(relwidth=0.5, relheight=0.2, relx=0.05, rely=0.5)
label2= tk.Label(root, text="Luggage", bg="black", fg="snow")
label2.place(width=70, height=25, x=400, y=100)
label3= tk.Label(root, text="seatbelt", bg="green", fg="snow")
label3.place(width=75, height=25, x=100, y=200)
label4= tk.Label(root, text="Pilot", bg="purple", fg="snow")
label4.place(relwidth=0.5, relheight=0.2, relx=0.5, rely=0.5)
label5= tk.Label(root, text="Hostesses", bg="brown", fg="snow")
label5.place(width=75, height=25, x=250, y=50)
label6= tk.Label(root, text="Food", bg="red", fg="snow")
label6.place(width=50, height=25, x=50, y=500)

root.mainloop()
