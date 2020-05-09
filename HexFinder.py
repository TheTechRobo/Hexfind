from tkinter import colorchooser, Button, Label
import tkinter
window = tkinter.Tk()
window.title("Hexfind")
def hi():
    hello = colorchooser.askcolor()
    print(hello)
    Label(window, text="RESULT:").pack()
    Label(window, text=hello).pack()
Button(window, text="Ask for Colour", command=hi).pack()
window.mainloop()
