import javax.swing.JScrollPane;

import java.awt.Color;
import java.awt.Dimension;

/** MapMenu class */
class MapMenu extends Menu {

    /** MapMenu attributes */
    private JScrollPane scrollPane;
    private MakerPanel menuPanel;

    /** MapMenu constructors */
    MapMenu() {
        this(new Map(PANE_WIDTH / Tile.PIXELS_PER_TILE + 1,
                     PANE_HEIGHT / Tile.PIXELS_PER_TILE + 1));
    }

    MapMenu(Map m) {
        setBackground(Color.WHITE);
        /* Initialize scrollable map pane */
        scrollPane = new JScrollPane();
        scrollPane.setPreferredSize(new Dimension(PANE_WIDTH, PANE_HEIGHT));
        map        = m;
        scrollPane.setViewportView(map);
        add(scrollPane);
        /* Initialize menu panel */
        menuPanel  = new MakerPanel(this);
        menuPanel.setPreferredSize(new Dimension(Panel.MENU_WIDTH, WINDOW_HEIGHT));
        add(menuPanel);
    }

    /** Set the MapMenu's Map to the one specified */
    private void setMap(Map m) {
        map = m;
        scrollPane.setViewportView(map);
        menuPanel.updateFields(map.mapWidth(), map.mapHeight());
    }

    /** Change the dimensions of the Map */
    void changeMapSize(int width, int height) {
        map.setWidth(width);
        map.setHeight(height);
        scrollPane.updateUI();
    }

}
// TODO: after zoom out is implemented, have a `load` panel like in Robert's branch, but it shows you the zoomed out version of your map
// TODO: remove zoom if it's too laggy
// TODO: frame.setTile("") accordingly. "Main Menu", "Map Maker", "Map Runner" etc
// TODO: fix laggy scrolling

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
