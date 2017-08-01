from MapMenu import MapMenu
from MainPanel import MainPanel
from Tkinter import *



frame_height = 600
frame_width = 1200


class MainMenu(MapMenu):
    def __init__(self, root):
        panel = MainPanel(root)
        return;

root = Tk()
frame = Frame(root, height = frame_height, width = frame_width)
frame.pack()
MainMenu(root)
root.mainloop()

# import javax.swing.JFrame;
# import javax.swing.WindowConstants;
#
# import java.awt.Dimension;
#
# /** MainMenu class */
# class MainMenu extends MapMenu {
#
#     /** MainMenu constructor */
#     MainMenu() {
#         super(new Map(0, 0));
#     }
#
#     /** Make a new Panel for the MainMenu */
#     MainPanel makePanel() {
#         return new MainPanel(this);
#     }
#
#     /** Get the MainMenu's title */
#     String getTitle() {
#         return "Main Menu";
#     }
#
#     /** Run the FORDS app */
#     public static void main(String[] args) {
#         // Initialize the window
#         JFrame frame = new JFrame();
#         frame.setPreferredSize(new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT));
#         frame.setLocationByPlatform(true);
#         frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
#         frame.setVisible(true);
#         frame.setResizable(false);
#         // Initialize the MainMenu
#         Panel.newScreen(frame, new MainMenu());
#     }
#
# }
