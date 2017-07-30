import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JScrollPane;
import javax.swing.SwingUtilities;
import javax.swing.WindowConstants;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.event.ActionEvent;

/** MainMenu class */
class MainMenu extends Menu {

    /** MapList subclass */
    private class MapList {

        /** MapList attributes */
        private final Map[] saves;
        private int index;

        /** MapList constructor */
        private MapList() {
            File[] files = new File(SAVE_DIR).listFiles(
                    (dir, name) -> name.endsWith(SAVE_EXT)
            );
            saves = new Map[files.length];
            ObjectInputStream in = null;
            try {
                for (int i = 0; i < saves.length; i += 1) {
                    String name = SAVE_DIR + "/" + files[i].getName();
                    FileInputStream f = new FileInputStream(name);
                    in = new ObjectInputStream(f);
                    saves[i] = (Map) in.readObject();
                }
                in.close();
            } catch (Exception e) {
                e.printStackTrace();
            }
            index = 0;
        }

        /** Get the size of the MapList */
        private int getSize() {
            return saves.length;
        }

        /** Get the current Map in the MapList */
        private Map peek() {
            return saves[index];
        }

        /** Get the next Map in the MapList */
        private Map next() {
            index = (index + 1) % getSize();
            return saves[index];
        }

        /** Get the previous Map in the MapList */
        private Map prev() {
            index = (index == 0) ? getSize() - 1 : index - 1;
            return saves[index];
        }

    }

    /** MainMenu attributes */
    private JScrollPane mapPane;
    private JLabel mapLabel;
    private MapList saves;

    /** MainMenu constructor */
    MainMenu() {
        setLayout(null);
        setBounds(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT);
        saves = new MapList();
        if (saves.getSize() != 0) {
            createScrollPane();
            createNameLabel();
            createPrevButton();
            createNextButton();
            createNewMapButton();
            createEditMapButton();
            createRunMapButton();
        }
        createNewMapButton();
        createSelectButton();
    }

    /**  */
    private void createScrollPane() {
        mapPane = new JScrollPane();
        mapPane.setBounds(0, 2 * WINDOW_HEIGHT / 3 - 150, WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2);
        map = saves.peek();
        mapPane.setViewportView(map);
        add(mapPane);
    }

    /**  */
    private void createNameLabel() {
        mapLabel = new JLabel("Name: " + map.getTag());
        mapLabel.setBounds(WINDOW_WIDTH / 8, 2 * WINDOW_HEIGHT / 3 - 200, 200, 50);
        mapLabel.setVisible(true);
        add(mapLabel);
    }

    /**  */
    private void createPrevButton() {
        JButton prevButton = new JButton("<");
        prevButton.setBounds(WINDOW_WIDTH / 3, 2 * WINDOW_HEIGHT / 3 - 100, 200, 50);
        prevButton.setVisible(true);
        prevButton.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        prevButton.addActionListener((ActionEvent e) -> {
            try {
                remove(map);
                map = saves.prev();
                mapPane.setViewportView(map);
                mapLabel.setText("Name: " + map.getTag());
            } catch (Exception e1) {
                e1.printStackTrace();
            }
        });
        add(prevButton);
    }

    /**  */
    private void createNextButton() {
        JButton nextButton = new JButton(">");
        nextButton.setBounds(WINDOW_WIDTH / 3, 2 * WINDOW_HEIGHT / 3 - 150, 200, 50);
        nextButton.setVisible(true);
        nextButton.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        nextButton.addActionListener((ActionEvent e) -> {
            try {
                remove(map);
                map = saves.next();
                mapPane.setViewportView(map);
                mapLabel.setText("Name: " + map.getTag());
            } catch (Exception e1) {
                e1.printStackTrace();
            }
        });
        add(nextButton);
    }

    /**  */
    private void createNewMapButton() {
        JButton newButton = new JButton("New Map");
        newButton.setBounds(WINDOW_WIDTH / 3, 2 * WINDOW_HEIGHT / 3, 200, 50);
        newButton.setVisible(true);
        newButton.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        newButton.addActionListener((ActionEvent e) -> {
            MakerMenu mapMaker = new MakerMenu();
            JFrame frame = (JFrame) SwingUtilities.getWindowAncestor(this);
            frame.remove(this);
            frame.getContentPane().add(mapMaker);
            frame.pack();
        });
        add(newButton);
    }

    /**  */
    private void createEditMapButton() {
        JButton loadButton = new JButton("Edit Map");
        loadButton.setBounds(WINDOW_WIDTH / 3, 2 * WINDOW_HEIGHT / 3 - 50, 200, 50);
        loadButton.setVisible(true);
        loadButton.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        loadButton.addActionListener((ActionEvent e) -> {
            map.addListeners();
            MakerMenu mapMaker = new MakerMenu(map);
            JFrame frame = (JFrame) SwingUtilities.getWindowAncestor(this);
            frame.remove(this);
            frame.getContentPane().add(mapMaker);
            frame.pack();
        });
        add(loadButton);
    }

    /**  */
    private void createRunMapButton() {
        // TODO (see createEditMapButton)
    }

    /**  */
    private void createSelectButton() {
        JButton listButton = new JButton("Select Map");
        listButton.setBounds(WINDOW_WIDTH / 3, 2 * WINDOW_HEIGHT / 3 + 50, 200, 50);
        listButton.setVisible(true);
        listButton.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        listButton.addActionListener((ActionEvent a) -> {
            JFileChooser fileChooser = new JFileChooser(SAVE_DIR);
            int returnValue = fileChooser.showOpenDialog(null);
            if (returnValue == JFileChooser.APPROVE_OPTION) {
                File selectedFile = fileChooser.getSelectedFile();
                try {
                    FileInputStream f = new FileInputStream(selectedFile);
                    ObjectInputStream in = new ObjectInputStream(f);
                    map = (Map) in.readObject();
                    mapPane.setViewportView(map);
                    mapLabel.setText("Name: " + map.getTag());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        add(listButton);
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
