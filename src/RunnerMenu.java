/** RunnerMenu class */
class RunnerMenu extends MapMenu {

    /** RunnerMenu constructor */
    RunnerMenu(Map m) {
        super(m);
    }

    /** Make a new Panel for the RunnerMenu */
    Panel makePanel() {
        return new RunnerPanel(this);
    }

}
