import tkinter as tk
import tkinter.font as font

root = tk.Tk()
Faith = "Faith is the substance of things hoped for, the evidence of things unseen yet"
Think = "As a man thinks in his heart, so is he"
Pray = "Pray without ceasing!"

msg1 = tk.Message(root, text=Faith)
msg2 = tk.Message(root, text=Think)
msg3 = tk.Message(root, text=Pray)

msg1.config(bg="dark blue", font=("Times", 16, "bold", "italic"), fg = "snow")
msg2.config(bg="dark green", font=("Helvetica", 12, "bold", "italic"), fg ="light green")
msg3.config(bg="yellow", font=("Verdana", 10, "bold"), fg ="blue")

msg1.pack()
msg2.pack()
msg3.pack()

root.mainloop()
