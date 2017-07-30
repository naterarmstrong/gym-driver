import javax.swing.JPanel;
import javax.swing.JScrollPane;

import java.awt.Dimension;
import java.awt.Toolkit;

/** Menu class */
abstract class Menu extends JPanel {

    /** Menu attributes */
    static final int WINDOW_WIDTH, WINDOW_HEIGHT;
    static {
        final Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        WINDOW_WIDTH  = screen.width - 200;
        WINDOW_HEIGHT = screen.height - 200;
    }
    static final int PANEL_WIDTH  = 200;
    static final int PANEL_HEIGHT = WINDOW_HEIGHT - 60;
    static final int PANE_WIDTH   = WINDOW_WIDTH - PANEL_WIDTH - 15;
    static final int PANE_HEIGHT  = PANEL_HEIGHT;
    Map map;
    JScrollPane scrollPane;

}
