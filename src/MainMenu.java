import javax.swing.JFrame;
import javax.swing.WindowConstants;

import java.awt.Dimension;

/** MainMenu class */
class MainMenu extends MapMenu {

    /** MainMenu constructor */
    MainMenu() {
        super(new Map(0, 0));
    }

    /** Make a new Panel for the MainMenu */
    MainPanel makePanel() {
        return new MainPanel(this);
    }

    /** Run the FORDS app */
    public static void main(String[] args) {
        JFrame frame = new JFrame();
        frame.setPreferredSize(new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT));
        frame.setLocationByPlatform(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setTitle("Main Menu");

        MainMenu mainPanel = new MainMenu();
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }

}
