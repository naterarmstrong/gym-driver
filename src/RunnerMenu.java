import java.awt.Dimension;

/** RunnerMenu class */
class RunnerMenu extends MapMenu {

    /** RunnerMenu constructor */
    RunnerMenu(Map m) {
        super(m);
    }

    /** Add a Panel to the RunnerMenu */
    void addPanel() {
        panel = new RunnerPanel(this);
        panel.setPreferredSize(new Dimension(MENU_WIDTH, WINDOW_HEIGHT));
        add(panel);
    }

}
