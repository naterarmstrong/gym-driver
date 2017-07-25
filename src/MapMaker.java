import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.WindowConstants;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Label;
import java.awt.TextField;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

/** MapMaker class */
class MapMaker extends JPanel {

    /** MenuPanel subclass */
    private class MenuPanel extends JPanel {

        /** MenuPanel attributes */
        private final MapMaker mapmaker;
        private TextField NAME_FIELD, WIDTH_FIELD, HEIGHT_FIELD;
        private final String SAVE_DIR    = "saved maps";
        private final int MIDDLE         = MENU_WIDTH / 2;
        private final int LABEL_WIDTH    = 50,  INPUT_HEIGHT = 25;
        private final int TERRAIN_WIDTH  = 100, TERRAIN_HEIGHT = 50;
        private final int UPDATE_WIDTH   = 60;
        private final int RESIZE_Y       = 30;
        private final int TERRAIN_CHNG_Y = 200;
        private final int SAVE_LOAD_Y    = WINDOW_HEIGHT - INPUT_HEIGHT - 60;

        /** MenuPanel constructor */
        private MenuPanel(MapMaker m) {
            mapmaker = m;
            setLayout(null);
            setOpaque(false);
            setVisible(true);
            addResizeOptions();
            addTerrainOptions();
            addSaveLoadOptions();
        }

        /** Utility method for populating the MenuPanel with TextFields */
        private TextField addTextField(String lTx, String fTx, int y, int w) {
            Label label = new Label(lTx);
            label.setBackground(Color.WHITE);
            label.setBounds(0, y, LABEL_WIDTH, INPUT_HEIGHT);
            TextField field = new TextField(fTx);
            field.setBounds(LABEL_WIDTH, y, w, INPUT_HEIGHT);
            add(label);
            add(field);
            return field;
        }

        /** Utility method for populating the MenuPanel with JButtons */
        private JButton addButton(String t, int x, int y, int w, int h,
                                  ActionListener a) {
            JButton button = new JButton(t);
            button.setBounds(x, y, w, h);
            button.addActionListener(a);
            button.setBorder(BorderFactory.createLineBorder(Color.BLACK));
            add(button);
            return button;
        }

        /** Populate the MenuPanel with Map-resize options */
        private void addResizeOptions() {
            int yWidth       = RESIZE_Y;
            int yHeight      = yWidth + INPUT_HEIGHT;
            int fieldWidth   = MENU_WIDTH - LABEL_WIDTH - UPDATE_WIDTH;
            String w         = (new Integer(map.getTilesWidth())).toString();
            WIDTH_FIELD      = addTextField("Width:", w, yWidth, fieldWidth);
            String h         = (new Integer(map.getTilesHeight())).toString();
            HEIGHT_FIELD     = addTextField("Height:", h, yHeight, fieldWidth);
            int xUpdate      = MENU_WIDTH - UPDATE_WIDTH;
            int updateHeight = 2 * INPUT_HEIGHT;
            addButton("Update", xUpdate, yWidth, UPDATE_WIDTH, updateHeight,
                    (ActionEvent a) -> {
                        try {
                            int newWidth  = Integer.valueOf(WIDTH_FIELD.getText());
                            int newHeight = Integer.valueOf(HEIGHT_FIELD.getText());
                            changeMapSize(newWidth, newHeight);
                        } catch (NumberFormatException e) {
                            e.printStackTrace();
                        }
                    });
        }

        /** Populate the MenuPanel with toggle-terrain options */
        private void addTerrainOptions() {
            int xR = MIDDLE,             top = TERRAIN_CHNG_Y;
            int xL = xR - TERRAIN_WIDTH, low = top + TERRAIN_HEIGHT;
            addTerrainButton("grass",  xL, top, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("road",   xR, top, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("gravel", xL, low, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("ice",    xR, low, TERRAIN_WIDTH, TERRAIN_HEIGHT);
        }

        private void addTerrainButton(String t, int x, int y, int w, int h) {
            addButton(t, x, y, w, h, (ActionEvent e) -> setTerrain(t));
        }

        /** Populate the MenuPanel with save & load options */
        private void addSaveLoadOptions() {
            int ySave     = SAVE_LOAD_Y;
            int yLoad     = ySave - INPUT_HEIGHT;
            int yName     = yLoad - INPUT_HEIGHT;
            int nameWidth = MENU_WIDTH - LABEL_WIDTH;
            addButton("save map", 0, ySave, MENU_WIDTH, INPUT_HEIGHT,
                    (ActionEvent a) -> {
                        ObjectOutputStream out;
                        try {
                            String name = String.format("%s/%s.data",
                                    SAVE_DIR, NAME_FIELD.getText());
                            FileOutputStream f = new FileOutputStream(name);
                            out = new ObjectOutputStream(f);
                            out.writeObject(map);
                            out.close();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    });
            addButton("load map", 0, yLoad, MENU_WIDTH, INPUT_HEIGHT,
                    (ActionEvent a) -> {
                        ObjectInputStream in;
                        try {
                            String name = String.format("%s/%s.data",
                                    SAVE_DIR, NAME_FIELD.getText());
                            FileInputStream f = new FileInputStream(name);
                            in = new ObjectInputStream(f);
                            map = (Map) in.readObject();
                            mapmaker.setMap(map);
                            in.close();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    });
            NAME_FIELD = addTextField("Name:", "New Map", yName, nameWidth);
        }

    }

    /** MapMaker attributes */
    private Map map;
    private JScrollPane scrollPane;
    private static final int WINDOW_WIDTH, WINDOW_HEIGHT;
    static {
        final Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        WINDOW_WIDTH  = screen.width - 200;
        WINDOW_HEIGHT = screen.height - 200;
    }
    private static final int MENU_WIDTH = 200;

    /** MapMaker constructor */
    private MapMaker() {
        setBackground(Color.WHITE);
        /* Initialize scrollable map pane */
        map = new Map();
        scrollPane = new JScrollPane();
        int paneWidth = WINDOW_WIDTH - MENU_WIDTH - 15;
        int paneHeight = WINDOW_HEIGHT - 60;
        scrollPane.setPreferredSize(new Dimension(paneWidth, paneHeight));
        scrollPane.setViewportView(map);
        add(scrollPane);
        /* Initialize menu panel */
        JPanel menuPanel = new MenuPanel(this);
        menuPanel.setPreferredSize(new Dimension(MENU_WIDTH, WINDOW_HEIGHT));
        add(menuPanel);
    }

    /** Set the MapMaker's Map to the one specified */
    private void setMap(Map m) {
        map = m;
    }

    /** Change the dimensions of the Map */
    private void changeMapSize(int width, int height) {
        map.setWidth(width);
        map.setHeight(height);
        scrollPane.updateUI();
    }

    /** Set the terrain pen to the specified terrain type */
    private void setTerrain(String terrainSelection) {
        Tile.terrainSelection = terrainSelection;
    }

    public static void main(String args[]) {
        JFrame frame = new JFrame();
        frame.setPreferredSize(new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT));
        frame.setLocationByPlatform(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setTitle("Map Maker");

        JPanel mainPanel = new MapMaker();
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }

}
// TODO: get load working
// TODO: alter WIDTH and HEIGHT inputs to reflect size of loaded map
// TODO: implement toggling the path type and orientation of Tiles
