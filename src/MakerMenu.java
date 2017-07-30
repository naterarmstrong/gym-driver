/** MakerMenu class */
class MakerMenu extends MapMenu {

    /** MakerMenu constructors */
    MakerMenu() {
        super();
    }

    MakerMenu(Map m) {
        super(m);
    }

    /** Make a new Panel for the MakerMenu */
    Panel makePanel() {
        return new MakerPanel(this);
    }

}
