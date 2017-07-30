/** Panel class */
abstract class Panel extends Menu {

    /** Panel attributes */
    Menu menu;

    /** Panel constructor */
    Panel(MapMenu m) {
        menu = m;
        map = menu.map;
        setLayout(null);
        setOpaque(false);
        setVisible(true);
    }

}
