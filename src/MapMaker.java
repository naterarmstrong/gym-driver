import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.SwingUtilities;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Label;
import java.awt.TextField;
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
        private final int ZOOM_STEP      = 25;
        private final int MIDDLE         = MENU_WIDTH / 2;
        private final int MARGIN         = 2;
        private final int LABEL_WIDTH    = 50;
        private final int INPUT_HEIGHT   = 25;
        private final int TERRAIN_WIDTH  = 100;
        private final int TERRAIN_HEIGHT = 50;
        private final int ZOOM_SIZE      = 20;
        private final int UPDATE_WIDTH   = 60;
        private final int RESIZE_Y       = 30;
        private final int TERRAIN_CHNG_Y = 200;
        private final int ZOOM_Y         = 350;
        private final int SAVE_LOAD_Y    = WINDOW_HEIGHT - INPUT_HEIGHT - 60;

        /** MenuPanel constructor */
        private MenuPanel(MapMaker m) {
            mapmaker = m;
            setLayout(null);
            setOpaque(false);
            setVisible(true);
            addResizeOptions();
            addTerrainOptions();
            addZoomOptions();
            addSaveBackOptions();
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
            button.setBounds(x + MARGIN, y + MARGIN, w - MARGIN, h - MARGIN);
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
            String w         = (new Integer(map.mapWidth())).toString();
            WIDTH_FIELD      = addTextField("Width:", w, yWidth, fieldWidth);
            String h         = (new Integer(map.mapHeight())).toString();
            HEIGHT_FIELD     = addTextField("Height:", h, yHeight, fieldWidth);
            int xUpdate      = MENU_WIDTH - UPDATE_WIDTH;
            int updateHeight = 2 * INPUT_HEIGHT;
            addButton("Update", xUpdate, yWidth, UPDATE_WIDTH, updateHeight,
                    (ActionEvent a) -> {
                        try {
                            String wField = WIDTH_FIELD.getText();
                            int newWidth  = Integer.valueOf(wField);
                            String hField = HEIGHT_FIELD.getText();
                            int newHeight = Integer.valueOf(hField);
                            changeMapSize(newWidth, newHeight);
                        } catch (NumberFormatException e) {
                            e.printStackTrace();
                        }
                    });
        }

        /** Populate the MenuPanel with toggle-terrain options */
        private void addTerrainOptions() {
            int xR  = MIDDLE;
            int xL  = xR - TERRAIN_WIDTH;
            int top = TERRAIN_CHNG_Y;
            int low = top + TERRAIN_HEIGHT;
            addTerrainButton("grass",  xL, top, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("road",   xR, top, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("gravel", xL, low, TERRAIN_WIDTH, TERRAIN_HEIGHT);
            addTerrainButton("ice",    xR, low, TERRAIN_WIDTH, TERRAIN_HEIGHT);
        }

        private void addTerrainButton(String t, int x, int y, int w, int h) {
            addButton(t, x, y, w, h, (ActionEvent e) -> setTerrain(t));
        }

        /** Populate the MenuPanel with zoom-in and zoom-out options */
        private void addZoomOptions() {
            int xR = MIDDLE;
            int xL = MIDDLE - ZOOM_SIZE;
            addButton("+", xL, ZOOM_Y, ZOOM_SIZE, ZOOM_SIZE,
                    (ActionEvent a) -> {
                        int PPT       = Tile.PIXELS_PER_TILE;
                        int stdZoom   = PPT + ZOOM_STEP;
                        if (stdZoom < PANE_WIDTH && stdZoom < PANE_HEIGHT) {
                            Tile.setPPT(stdZoom);
                        }
                        map.render();
                    });
            addButton("-", xR, ZOOM_Y, ZOOM_SIZE, ZOOM_SIZE,
                    (ActionEvent a) -> {
                        int PPT       = Tile.PIXELS_PER_TILE;
                        int minWidth  = PANE_WIDTH / map.mapWidth();
                        int minHeight = PANE_HEIGHT / map.mapHeight();
                        int stdZoom   = PPT - ZOOM_STEP;
                        if (minWidth < stdZoom || minHeight < stdZoom) {
                            Tile.setPPT(stdZoom);
                        } else {
                            Tile.setPPT(Math.min(minWidth, minHeight));
                        }
                        map.render();
                    });
        }

        /** Populate the MenuPanel with save & load options */
        private void addSaveBackOptions() {
            int ySave     = SAVE_LOAD_Y;
            int yLoad     = ySave - INPUT_HEIGHT;
            int yName     = yLoad - INPUT_HEIGHT;
            int nameWidth = MENU_WIDTH - LABEL_WIDTH;
            addButton("save map", 0, ySave, MENU_WIDTH, INPUT_HEIGHT,
                    (ActionEvent a) -> {
                        ObjectOutputStream out;
                        try {
                            String tag = NAME_FIELD.getText();
                            map.setTag(tag);
                            String dir = String.format("%s/%s.ser",
                                    SAVE_DIR, tag);
                            FileOutputStream f = new FileOutputStream(dir);
                            out = new ObjectOutputStream(f);
                            out.writeObject(map);
                            out.close();
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                    });
            addButton("main menu", 0, yLoad, MENU_WIDTH, INPUT_HEIGHT,
                    (ActionEvent a) -> {
                        JFrame frame = (JFrame)
                                SwingUtilities.getWindowAncestor(mapmaker);
                        frame.remove(mapmaker);
                        try {
                            frame.getContentPane().add(new MainMenu());
                        } catch (Exception e) {
                            e.printStackTrace();
                        }
                        frame.pack();
                    });
            NAME_FIELD = addTextField("Name:", map.getTag(), yName, nameWidth);
        }

        /** Update width & height TextFields with the current Map dimensions */
        private void updateFields(int w, int h) {
            WIDTH_FIELD.setText(String.valueOf(w));
            HEIGHT_FIELD.setText(String.valueOf(h));
        }

    }

    /** MapMaker attributes */
    private Map map;
    private JScrollPane scrollPane;
    private MenuPanel menuPanel;
    private static final int WINDOW_WIDTH  = MainMenu.WINDOW_WIDTH;
    private static final int WINDOW_HEIGHT = MainMenu.WINDOW_HEIGHT;
    private static final int MENU_WIDTH    = 200;
    private static final int PANE_WIDTH    = WINDOW_WIDTH - MENU_WIDTH - 15;
    private static final int PANE_HEIGHT   = WINDOW_HEIGHT - 60;

    /** MapMaker constructors */
    MapMaker() {
        this(new Map(PANE_WIDTH / Tile.PIXELS_PER_TILE + 1,
                     PANE_HEIGHT / Tile.PIXELS_PER_TILE + 1));
    }

    MapMaker(Map m) {
        setBackground(Color.WHITE);
        /* Initialize scrollable map pane */
        scrollPane = new JScrollPane();
        scrollPane.setPreferredSize(new Dimension(PANE_WIDTH, PANE_HEIGHT));
        map        = m;
        scrollPane.setViewportView(map);
        add(scrollPane);
        /* Initialize menu panel */
        menuPanel  = new MenuPanel(this);
        menuPanel.setPreferredSize(new Dimension(MENU_WIDTH, WINDOW_HEIGHT));
        add(menuPanel);
    }

    /** Set the MapMaker's Map to the one specified */
    private void setMap(Map m) {
        map = m;
        scrollPane.setViewportView(map);
        menuPanel.updateFields(map.mapWidth(), map.mapHeight());
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

}
// TODO: after zoom out is implemented, have a `load` panel like in Robert's branch, but it shows you the zoomed out version of your map
// TODO: remove zoom if it's too laggy
// TODO: frame.setTile("") accordingly. "Main Menu", "Map Maker", "Map Runner" etc

// TODO:
// You put the car down, specifying a cardinal direction on the menu. It appears, but the angle is plus or minus some error, generally going in that direction.
// You put the CPU cars down too, with no randomness added to their angle.
// Also make an AI for the CPU cars, so that they go straight if straight road, or turn if curved road.
// You click to put down a car, click again to delete it.
// Click "Play" to start.
// He gives us acceleration and steer angle. We have to give back (from the step function) this tuple:
    // An observation, which is a pixel array of what's on screen
    // A float returned from calling some function `getReward`, specified in the UserCar class
    // A boolean specifying whether it's time to finish.
