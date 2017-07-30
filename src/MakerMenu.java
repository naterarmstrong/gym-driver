import java.awt.Dimension;

/** MakerMenu class */
class MakerMenu extends MapMenu {

    /** MakerMenu constructors */
    MakerMenu() {
        super();
    }

    MakerMenu(Map m) {
        super(m);
    }

    /** Add a Panel to the MakerMenu */
    void addPanel() {
        panel = new MakerPanel(this);
        panel.setPreferredSize(new Dimension(MENU_WIDTH, WINDOW_HEIGHT));
        add(panel);
    }

}
