
#  tempconverter

import tkinter as tk
import tkinter.font as font

def convert_fahrenheit():
    input1 = fahrtext.get()
    fahrtemp = float(input1)
    celsiusbox.delete(0, "end")
    celsiusbox.insert(0, '%.2f' % (tocelsius(fahrtemp))) #specify 2 digits of precision
    kelvinbox.delete(0, "end")
    kelvinbox.insert(0, '%.2f' % (tokelvin(tocelsius(fahrtemp))))
    return

def convert_celsius():
    input2 = celtext.get()
    celtemp = float(input2)
    fahrenheitbox.delete(0, "end")
    fahrenheitbox.insert(0, '%.2f' % (tofahrenheit(celtemp)))
    kelvinbox.delete(0, "end")
    kelvinbox.insert(0, '%.2f' % (tokelvin(celtemp)))

def convert_kelvin():
    input3 = keltext.get()
    keltemp = float(input3)
    fahrenheitbox.delete(0, "end")
    fahrenheitbox.insert(0, '%.2f' % (tofahrenheit(kelvintocelsius(keltemp))))
    celsiusbox.delete(0, "end")
    celsiusbox.insert(0, '%.2f' % (kelvintocelsius(keltemp)))

def tocelsius(fahr):
    return (fahr-32) * 5.0 / 9.0

def tofahrenheit(cel):
    return cel * 9.0 / 5.0 + 32

def kelvintocelsius(kel):
    return kel - 273.15

def tokelvin(cel):
    return cel + 273.15

root = tk.Tk()
root.title('Temperature converter')

fahrlabel = tk.Label(root, text = 'Fahrenheit')
fahrlabel.grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)

cellabel = tk.Label(root, text = 'Celsius')
cellabel.grid(column = 0, row = 1,  padx = 5, pady = 5, sticky=tk.W)

kellabel = tk.Label(root, text = 'Kelvin')
kellabel.grid(column = 0, row = 2, padx = 5, pady = 5, sticky = tk.W)

fahrtext = tk.StringVar()
fahrtext.set('')
fahrenheitbox = tk.Entry(root, textvariable=fahrtext)
fahrenheitbox.grid(column = 1, row = 0, padx = 5, pady = 5)

celtext = tk.StringVar()
celtext.set('')
celsiusbox = tk.Entry(root, textvariable=celtext)
celsiusbox.grid(column = 1, row = 1, padx = 5, pady = 5)

keltext = tk.StringVar()
keltext.set('')
kelvinbox = tk.Entry(root, textvariable=keltext)
kelvinbox.grid(column = 1, row = 2, padx = 5, pady = 5)

fahrbutton = tk.Button(root, text = 'Convert', command = convert_fahrenheit)
fahrbutton.grid(column = 2, row = 0, padx = 5, pady = 5, sticky = tk.SW)

celbutton = tk.Button(root, text = 'Convert', command = convert_celsius)
celbutton.grid( column = 2, row = 1, padx = 5, pady = 5, sticky = tk.SW)

kelbutton = tk.Button(root, text = 'Convert', command = convert_kelvin)
kelbutton.grid(column = 2, row = 2, padx = 5, pady = 5, sticky = tk.SW)


myFont = font.Font(size=10)
mainmenu = tk.Menu(root)

toolmenu = tk.Menu(mainmenu, tearoff = 0) # second submenu
toolmenu.add_command(label = "Fahrenheit", command =convert_fahrenheit)
toolmenu.add_command(label = "Celsius", command = convert_celsius)
toolmenu.add_command(label = "Kelvin", command = convert_kelvin) # sets our window to Protein mode
mainmenu.add_cascade(label="Temperature", menu=toolmenu)

filemenu = tk.Menu(mainmenu, tearoff = 0) # first submenu
filemenu.add_command(label = "Exit", command = root.destroy) # close the main window
mainmenu.add_cascade(label="File", menu=filemenu) # add the entries to our submenu


root.config(menu = mainmenu)

root.mainloop()
