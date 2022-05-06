from tkinter import *
from PIL import Image
from PIL import ImageTk

# image as a clickable button
master = Tk()


def callback():
    print("button clicked")


width = 850
height = 450
img = Image.open("img/search.png")
img = img.resize((width, height))
photoImg = ImageTk.PhotoImage(img)
b = Button(master, image=photoImg, command=callback, width=850)
b.pack()
mainloop()
