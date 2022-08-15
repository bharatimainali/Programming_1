##oppgave3.A# Hello tkinter.
#i importet tkinter as tk. and created the an applications window titled hello tkinter.
import tkinter as tk

window1 = tk.Tk()
window1.title("Hello rkinter!")
window1.mainloop()

##oppgave3.B# GUI elements.
#created a program window titled "GUI Elements".
window2 = tk.Tk()
window2.title("GUI Elements")
#created the level1,2,3 og adding the .pack()
label1 = tk.Label(text="Label 1").pack()
label2 = tk.Label(text="Label 2", background="red", foreground="white").pack()
label3 = tk.Label(text="Label 3", background="yellow", width = 10, height = 5).pack()
button = tk.Button(text="Button!", width = 7, height = 2).pack()
input = tk.Entry(width = 15).pack()
textbox = tk.Text().pack()


window2.mainloop()


