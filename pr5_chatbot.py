# Chatbot
from tkinter import *

root = Tk()
root.title("Chatbot")

def send():
    send = "\nYou : " + e.get()
    txt.insert(END, send)
    user = e.get().lower()
    
    if user == "hello":
        txt.insert(END, "\nBot : Hi\n")
    elif user == "hi" or user == "hii" or user == "hiiii":
        txt.insert(END, "\nBot : Hello\n")
    elif e.get() == "how are you":
        txt.insert(END, "\nBot : fine! and you")
    elif user == "fine" or user == "i am good" or user == "i am doing good":
        txt.insert(END, "\nBot : Great! how can I help you.")
    else:
        txt.insert(END, "\nBot : Sorry! I didn't get you")
    
    e.delete(0, END)

# Create GUI elements
txt = Text(root)
txt.grid(row=0, column=0, columnspan=2)

e = Entry(root, width=100)
e.grid(row=1, column=0)

send = Button(root, text="Send", command=send)
send.grid(row=1, column=1)

root.mainloop()