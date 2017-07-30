import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;

import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
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

// TODO: frame.setTile("") accordingly. "Main Menu", "Map Maker", "Map Runner" etc
// TODO: fix laggy scrolling
// TODO: clean up the main method

// TODO: MapRunner
// You put the car down, specifying a cardinal direction on the menu. It appears, but the angle is plus or minus some error, generally going in that direction.
// You put the CPU cars down too, with no randomness added to their angle.
// Also make an AI for the CPU cars, so that they go straight if straight road, or turn if curved road.
// You click to put down a car, click again to delete it.
// Click "Play" to start.
// He gives us acceleration and steer angle. We have to give back (from the step function) this tuple:
// An observation, which is a pixel array of what's on screen
// A float returned from calling some function `getReward`, specified in the UserCar class
// A boolean specifying whether it's time to finish.
