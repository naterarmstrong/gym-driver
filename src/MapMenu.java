import javax.swing.JScrollPane;

import java.awt.Color;
import java.awt.Dimension;

/** MapMenu class */
abstract class MapMenu extends Menu {

    /** MapMenu attributes */
    Panel panel;

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
        /* Initialize panel */
        addPanel();
    }

    /** Add a Panel to the MapMenu */
    abstract void addPanel();

}