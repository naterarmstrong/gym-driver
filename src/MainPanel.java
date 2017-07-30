import javax.swing.*;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.io.File;
import java.io.FileInputStream;
import java.io.ObjectInputStream;

/** MainPanel class */
class MainPanel extends Panel {

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
            if (files == null) {
                files = new File[0];
            }
            saves = new Map[files.length];
            ObjectInputStream in = null;
            try {
                for (int i = 0; i < saves.length; i += 1) {
                    String name = SAVE_DIR + "/" + files[i].getName();
                    FileInputStream f = new FileInputStream(name);
                    in = new ObjectInputStream(f);
                    saves[i] = (Map) in.readObject();
                }
                if (in != null) {
                    in.close();
                }
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

    /** MainPanel attributes */
    private static final int RESIZE_Y  = 30;
    private static final int TERRAIN_Y = 200;
    private static final int ZOOM_Y    = 350;
    private static final int UPDATE_W  = 60;
    private static final int TERRAIN_W = 100;
    private static final int TERRAIN_H = 50;
    private static final int ZOOM_WH   = 20;
    private static final int ZOOM_STEP = 25;
    private JLabel NAME_FIELD;
    private MapList saves;

    /** MainPanel constructor */
    MainPanel(MainMenu m) {
        super(m);
        saves = new MapList();
        if (saves.getSize() != 0) {
        }
    }


    /**  */
    private void createScrollPane() {
        scrollPane = new JScrollPane();
        scrollPane.setBounds(0, 2 * WINDOW_HEIGHT / 3 - 150, WINDOW_WIDTH / 3, WINDOW_HEIGHT / 2);
        map = saves.peek();
        scrollPane.setViewportView(map);
        add(scrollPane);
    }

    /**  */
    private void createNameLabel() {
        NAME_FIELD = new JLabel("Name: " + map.getTag());
        NAME_FIELD.setBounds(WINDOW_WIDTH / 8, 2 * WINDOW_HEIGHT / 3 - 200, 200, 50);
        NAME_FIELD.setVisible(true);
        add(NAME_FIELD);
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
                scrollPane.setViewportView(map);
                NAME_FIELD.setText("Name: " + map.getTag());
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
                scrollPane.setViewportView(map);
                NAME_FIELD.setText("Name: " + map.getTag());
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
                    scrollPane.setViewportView(map);
                    NAME_FIELD.setText("Name: " + map.getTag());
                } catch (Exception e) {
                    e.printStackTrace();
                }
            }
        });
        add(listButton);
    }

}
