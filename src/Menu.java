import javax.swing.JPanel;

import java.awt.Dimension;
import java.awt.Toolkit;

/** Menu class */
abstract class Menu extends JPanel {

    /** Menu attributes */
    Map map;
    static final String SAVE_DIR    = "saved maps";
    static final int WINDOW_WIDTH, WINDOW_HEIGHT;
    static {
        final Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        WINDOW_WIDTH  = screen.width - 200;
        WINDOW_HEIGHT = screen.height - 200;
    }
    static final int MENU_WIDTH = 200;
    static final int PANE_WIDTH    = WINDOW_WIDTH - Panel.MENU_WIDTH - 15;
    static final int PANE_HEIGHT   = WINDOW_HEIGHT - 60;

}
