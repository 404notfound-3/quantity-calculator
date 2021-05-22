import os
import tkinter as tk
from tkinter import NoDefaultRoot, ttk, messagebox, PhotoImage
import webbrowser

width, height = 500, 210
main_app = tk.Tk()
main_app.geometry(f"{width}x{height}")
main_app.title(" Quantity Calculator")
main_app.resizable(False, False)
main_app.wm_iconbitmap(r"icons/icon.ico")

if os.path.isfile("config.txt"):
    with open("config.txt", "r") as r:
        accoutSize, riskperTrade = r.readlines()[-1].split(",")
        accoutSize, riskperTrade = float(accoutSize), float(riskperTrade)
else:
    accoutSize, riskperTrade = 10000, 2

def exitFunc(event = None):
    mBox = messagebox.askyesno("Warning", "Are you sure you want to Exit", icon = "warning")
    if mBox: main_app.destroy()

def config(acsize, rpt):
    global accoutSize, riskperTrade
    if (acsize == accoutSize) and (riskperTrade == rpt):
        messagebox.showerror(" Error", "Nothing changed")
    else:
        with open("config.txt", "a", newline = "") as f: f.write(f"{acsize},{rpt}\n")
        messagebox.showinfo(title = "Saved", message = "Config file saved successfully saved")

image1 = PhotoImage(file = r"icons/button_config_90_22.png")
image2 = PhotoImage(file = r"icons/button_clear_90_22.png")
image3 = PhotoImage(file = r"icons/button_submit_90_22.png")
image4 = PhotoImage(file = r"icons/button_label_550_21.png")
image5 = PhotoImage(file = r"icons/button_stop_price_250_21.png")
image6 = PhotoImage(file = r"icons/button_config_250_21.png")

notebook = ttk.Notebook(main_app)
notebook.pack(expand = True, fill = "both")
frame1 = tk.Frame(notebook)
frame2 = tk.Frame(notebook)

frame1.pack(fill = 'both', expand = True)
frame2.pack(fill = 'both', expand = True)

notebook.add(frame1, text = "Stop Price", image = image5)
notebook.add(frame2, text = "Stop Loss", image = image6)

frame3 = tk.Frame(frame1)
frame6 = tk.Frame(frame2)
frame4 = tk.Frame(frame3)
frame7 = tk.Frame(frame6)
frame5 = tk.Frame(frame3)
frame8 = tk.Frame(frame6)
line1 = tk.Frame(frame3, height = 2, width = 550, bg = "gray80", relief = "groove")
line2 = tk.Frame(frame6, height = 2, width = 550, bg = "gray80", relief = "groove")
label1 = ttk.Label(frame4, text = " Entry Price     : ")
label3 = ttk.Label(frame7, text = " Account Size (INR)    : ")
label2 = ttk.Label(frame4, text = " Stop Price      : ")
label4 = ttk.Label(frame7, text = " Risk per Trade  (%)    : ")

e1, e2, e3, e4 = tk.StringVar(), tk.StringVar(), tk.StringVar(value = float(accoutSize)), tk.StringVar(value = float(riskperTrade))
entry1 = ttk.Entry(frame4, width = 40, textvariable = e1)
entry1.focus()
entry3 = ttk.Entry(frame7, width = 40, textvariable = e3)
entry2 = ttk.Entry(frame4, width = 40, textvariable = e2)
entry4 = ttk.Entry(frame7, width = 40, textvariable = e4)

def calc_sp(event = None):
    global e1, e2
    sl = (float(e1.get()) - float(e2.get()))
    risk = (riskperTrade * accoutSize)/100
    qty = risk/sl
    return messagebox.showinfo("Information", f"According to your risk profile you should trade {qty} of this security and your maximum risk would be {risk}.")

def clear(event = None): entry1.delete(0, "end"), entry2.delete(0, "end")
def switch_tab(event = None): notebook.select(1)
def browser(event = None): webbrowser.open("https://github.com/404notfound-3")
def left(event = None): notebook.select(0)

button1 = tk.Button(frame5, image = image1,  command = switch_tab, cursor = "hand2", borderwidth = 0)
button2 = tk.Button(frame5, image = image2, command = clear, cursor = "hand2", borderwidth = 0)
button3 = tk.Button(frame5, image = image3, command = calc_sp, cursor = "hand2", borderwidth = 0)
button4 = tk.Button(frame8, image = image3, command = lambda:config(acsize = float(e3.get()), rpt = float(e4.get())), cursor = "hand2", borderwidth = 0)
button5 = tk.Button(main_app, image = image4, command = browser, cursor = "hand2", borderwidth = 0)

## All frame2 elements
label1.grid(row = 0, column = 0, padx = 20, pady = 10)
label3.grid(row = 0, column = 0, padx = 20, pady = 10)
entry1.grid(row = 0, column = 1, padx = 0, pady = 10)
entry3.grid(row = 0, column = 1, padx = 0, pady = 10)
label2.grid(row = 1, column = 0, padx = 20, pady = 0)
label4.grid(row = 1, column = 0, padx = 20, pady = 0)
entry2.grid(row = 1, column = 1, padx = 20, pady = 0)
entry4.grid(row = 1, column = 1, padx = 20, pady = 0)

## All frame3 elements
button1.grid(row = 0, column = 0, padx = 0, pady = 0)
button2.grid(row = 0, column = 1, padx = 20, pady = 0)
button3.grid(row = 0, column = 2, padx = 0, pady = 0)
button4.grid(row = 0, column = 0, padx = 0, pady = 0)

frame4.grid(row = 0, column = 0, pady = 10)
frame5.grid(row = 2, column = 0, pady = 0)
frame7.grid(row = 0, column = 0, pady = 10)
frame8.grid(row = 2, column = 0, pady = 0)

line1.grid(row = 1, column = 0, pady = 12)
line2.grid(row = 1, column = 0, pady = 12)
frame3.pack(side = tk.TOP, pady = 0)
frame6.pack(side = tk.TOP, pady = 0)

button5.pack(side = tk.BOTTOM)

main_app.bind("<Control-q>", exitFunc)
main_app.bind("<Escape>", exitFunc)
main_app.bind("<Left>", left)
main_app.bind("<Right>", switch_tab)

main_app.mainloop()