from tkinter import *

frame_height = 600
frame_width = 1000
LETTER_SIZE = 10.25


class MakerMenu(PanedWindow):
    button_width = 5
    button_height = 3 * LETTER_SIZE

    def __init__(self, root):
        PanedWindow.__init__(self)
        self.root = root
        self.displayMapName()
        self.addButtons()
        self.addMapPane()

    def addButtons(self):
        self.setGrassButton()
        self.setRoadButton()
        self.setGravelButton()
        self.setIceButton()
        self.setNewButton()
        self.setSelectButton()

    def displayMapName(self):
        T = Text(root, height=2, width=30)
        T.insert(END, "Map Name")
        T.place(x = (frame_width - 3 * self.button_width * LETTER_SIZE), y=0)

    def start_edit_menu(self):
        print("EDIT")

    def setGrassButton(self):
        editButton = Button(self.root, text="grass", command = self.start_edit_menu, width=self.button_width)
        editButton.place(x = frame_width - self.button_width * LETTER_SIZE - 20, y= 5 * LETTER_SIZE)

    def setRoadButton(self):
        runButton = Button(self.root, text="road", command=None, width=self.button_width)
        runButton.place(x = frame_width - 3 * self.button_width * LETTER_SIZE, y = 5 * LETTER_SIZE)

    def setGravelButton(self):
        nextButton = Button(self.root, text="gravel", command=None, width = self.button_width)
        nextButton.place(x = frame_width - self.button_width * LETTER_SIZE - 20, y = 2 * self.button_height + 5 * LETTER_SIZE)

    def setIceButton(self):
        prevButton = Button(self.root, text="ice", command=None, width = self.button_width)
        prevButton.place(x = frame_width - 3 * self.button_width * LETTER_SIZE, y = 2 * self.button_height + 5 * LETTER_SIZE)

    def setSelectButton(self):
        selectButton = Button(self.root, text="Save Map", command=None, width = 3 * self.button_width)
        selectButton.place(x=frame_width - 3 * self.button_width * LETTER_SIZE, y= frame_height - 2 * self.button_height)

    def setNewButton(self):
        newButton = Button(self.root, text="Main Menu", command=None, width = 3 * self.button_width)
        newButton.place(x = frame_width - 3 * self.button_width * LETTER_SIZE, y = frame_height - self.button_height)

    def addMapPane(self):
        master = PanedWindow(bg="blue")
        master.pack(side=LEFT)
        master.propagate(0)
        canvas = Canvas(master, scrollregion=(0, 0, frame_width, frame_height), bg="green")
        hbar = Scrollbar(master, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        vbar = Scrollbar(master, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)
        master.config(width=frame_width - 200, height=frame_height)
        master.add(canvas)



root = Tk()
root.wm_title("Map Maker")
root.resizable(width=False, height=False)
root.config(width = frame_width, height = frame_height)
root.propagate(0)
frame = Frame(root)
main_menu = MakerMenu(root)
root.mainloop()