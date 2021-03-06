from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
root = Tk()


h = ttk.Scrollbar(root, orient=HORIZONTAL)
v = ttk.Scrollbar(root, orient=VERTICAL)
canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
h['command'] = canvas.xview
v['command'] = canvas.yview
ttk.Sizegrip(root).grid(column=10, row=10, sticky=(S,E))

canvas.grid(column=0, row=0, sticky=(N,W,E,S))
h.grid(column=0, row=10, sticky=(W,E))
v.grid(column=10, row=0, sticky=(N,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

lastx, lasty = 0, 0

def xy(event):
    global lastx, lasty
    lastx, lasty = canvas.canvasx(event.x), canvas.canvasy(event.y)

def setColor(newcolor):
    global color
    color = newcolor
    canvas.dtag('all', 'paletteSelected')
    canvas.itemconfigure('palette', outline='white')
    canvas.addtag('paletteSelected', 'withtag', 'palette%s' % color)
    canvas.itemconfigure('paletteSelected', outline='#999999')

def addLine(event):
    global lastx, lasty
    x, y = canvas.canvasx(event.x), canvas.canvasy(event.y)
    canvas.create_line((lastx, lasty, x, y), fill=color, width=5, tags='currentline')
    lastx, lasty = x, y

def doneStroke(event):
    canvas.itemconfigure('currentline', width=1)  

def setTileColor(newcolor, w, z):
    index = 4*w + z
    if newcolor == "green":
        print "YAY"
    print tile_list[index]
    canvas.itemconfigure(tile_list[index], fill=newcolor)

def setTileImage(newimage, w, z):
    index = 4*w + z
    canvas.itemconfigure(tile_list[index], image=newimage)
def test(event):
    pass
        
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
canvas.bind("<B1-ButtonRelease>", doneStroke)
canvas.bind("<Shift-Button-1>", test)

moddable_curve_road = Image.open("../resources/quarter_turn_road_200.png")
upleft_curve_road = ImageTk.PhotoImage(moddable_curve_road)
upright_curve_road = ImageTk.PhotoImage(moddable_curve_road.rotate(90))
straight_road = ImageTk.PhotoImage(Image.open("../resources/straight_road_200.png"))
straight_ice = ImageTk.PhotoImage(Image.open("../resources/quarter_turn_road_200.png"))
tile_list = []
def populate(tile_list):
    def creator(x, y):
        id = canvas.create_image(100+200*x, 100 + 200*y, image=straight_road)
        canvas.tag_bind(id, "<Button-1>", lambda _: setTileImage(upleft_curve_road, x, y))
        canvas.tag_bind(id, "<Shift-Button-1>", lambda _: setTileImage(straight_road, x, y))
        tile_list.append(id)
    for x in range(4):
        for y in range(4):
            if x*y % 2 == 0:
                cur_color = "red"
            else:
                cur_color = "blue"
            creator(x, y)
populate(tile_list)

car_png = Image.open('../resources/blue_car.png')
car_gif = Image.open('../resources/blue_car.gif')
fcar_png = ImageTk.PhotoImage(car_png)
fcar_gif = ImageTk.PhotoImage(car_gif)

canvas.create_image(100, 100, image=fcar_png)
canvas.create_image(200, 200, image=fcar_gif)




#id = canvas.create_rectangle((10, 10, 30, 30), fill="red", tags=('palette', 'palettered'))
#canvas.tag_bind(id, "<Button-1>", lambda x: setColor("red"))
#id = canvas.create_rectangle((10, 35, 30, 55), fill="blue", tags=('palette', 'paletteblue'))
#canvas.tag_bind(id, "<Button-1>", lambda x: setColor("blue"))
#id = canvas.create_rectangle((10, 60, 30, 80), fill="black", tags=('palette', 'paletteblack', 'paletteSelected'))
#canvas.tag_bind(id, "<Button-1>", lambda x: setColor("black"))

setColor('black')
canvas.itemconfigure('palette', width=5)
root.mainloop()