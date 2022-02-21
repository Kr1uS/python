from tkinter import *
from random import randint

root = Tk()

Label(text='Enter:').pack()
e = Entry(width=50)
e.pack()

colors = ['red', 'orange', 'yellow', 'green', 'blue']

c = Canvas(root, width=300, height=300, bg='white')
c.pack()

xy1 = 50
xy2 = 250

c.create_oval(xy1, xy1, xy2, xy2, width=2)


def draw(e):
    l = list(e.widget.get().split(' '))
    procents = []

    for i in l:
        procents.append(float(i))

    start = 0
    extent = 0
    i = 0

    for procent in procents:
        if i > len(colors) - 1:
            i = 0
        extent = 360 - (360 * ((100 - procent) / 100))
        print(extent)
        c.create_arc(xy1, xy1, xy2, xy2,
                     start=start, extent=extent,
                     fill=colors[i])
        start += extent
        extent = 0
        i += 1


e.bind('<Return>', draw)

root.mainloop()