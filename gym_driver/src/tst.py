from tkinter import *

frame_height = 600
frame_width = 1000
LETTER_SIZE = 10.25


class MainMenu(PanedWindow):
    button_width = 20
    button_height = 3 * LETTER_SIZE

    def __init__(self, root):
        PanedWindow.__init__(self)
        self.root = root
        self.displayMapName()
        self.addButtons()
        self.addMapPane()

    def addButtons(self):
        self.setEditButton()
        self.setRunButton()
        self.setNextButton()
        self.setPrevButton()
        self.setNewButton()
        self.setSelectButton()

    def displayMapName(self):
        T = Text(root, height=2, width=30)
        T.insert(END, "Map Name")
        T.place(x = frame_width - self.button_width * LETTER_SIZE, y=0)

    def start_edit_menu(self):
        print("EDIT")

    def setEditButton(self):
        editButton = Button(self.root, text="Edit Map", command = self.start_edit_menu, width=self.button_width)
        editButton.place(x = frame_width - self.button_width * LETTER_SIZE, y= 2 * LETTER_SIZE)

    def setRunButton(self):
        runButton = Button(self.root, text="Run Map", command=None, width=self.button_width)
        runButton.place(x = frame_width - self.button_width * LETTER_SIZE, y = self.button_height + 2 * LETTER_SIZE)

    def setNextButton(self):
        nextButton = Button(self.root, text=">", command=None, width = self.button_width / 2)
        nextButton.place(x = frame_width - self.button_width * LETTER_SIZE / 2, y = 2 * self.button_height + 2 * LETTER_SIZE)

    def setPrevButton(self):
        prevButton = Button(self.root, text="<", command=None, width = self.button_width / 2)
        prevButton.place(x = frame_width - self.button_width * LETTER_SIZE, y = 2 * self.button_height + 2 * LETTER_SIZE)

    def setSelectButton(self):
        selectButton = Button(self.root, text="Select Map", command=None, width = self.button_width)
        selectButton.place(x=frame_width - self.button_width * LETTER_SIZE, y= 3 * self.button_height + 2 * LETTER_SIZE)

    def setNewButton(self):
        newButton = Button(self.root, text="NEW MAP", command=None, width = self.button_width)
        newButton.place(x = frame_width - self.button_width * LETTER_SIZE, y = frame_height - self.button_height)

    def addMapPane(self):
        master = PanedWindow(bg="blue")
        master.pack(side=LEFT)
        master.propagate(0)
        canvas = Canvas(master, scrollregion=(0, 0, frame_width, frame_height), bg="blue")
        canvas.config(width = frame_width, height = frame_height)
        hbar = Scrollbar(master, orient=HORIZONTAL)
        hbar.pack(side=BOTTOM, fill=X)
        hbar.config(command=canvas.xview)
        vbar = Scrollbar(master, orient=VERTICAL)
        vbar.pack(side=RIGHT, fill=Y)
        vbar.config(command=canvas.yview)
        canvas.config(xscrollcommand=hbar.set, yscrollcommand=vbar.set)
        canvas.pack(side=LEFT, expand=True, fill=BOTH)
        master.config(width=frame_width - self.button_width * LETTER_SIZE, height=frame_height)

        b = Button(canvas)
        b.pack()
        canvas.create_window(235, 160, window=b)

        canvas.create_rectangle(100, 100, 200, 200, fill="green")

        master.add(canvas)



root = Tk()
root.wm_title("Menu")
root.resizable(width=False, height=False)
root.config(width = frame_width, height = frame_height)
root.propagate(0)
frame = Frame(root)
main_menu = MainMenu(root)
root.mainloop()