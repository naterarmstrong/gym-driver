import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.WindowConstants;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Label;
import java.awt.TextField;
import java.awt.Toolkit;
import java.awt.event.ActionEvent;

/** MapMaker class */
class MapMaker extends JPanel {

    /** MenuPanel subclass */
    private class MenuPanel extends JPanel {

        /** MenuPanel attributes */
        private final MapMaker mapmaker;
        private final int MIDDLE = MENU_WIDTH / 2;
        private final int TEXT_INPUT_Y = 30,    BUTTONS_Y = 200;
        private final int LABEL_WIDTH = 80,     INPUT_HEIGHT = 25;
        private final int BUTTON_WIDTH = 100,   BUTTON_HEIGHT = 50;
        private final String SAVE_DIR = "saved maps";
        private TextField NAME_FIELD, WIDTH_FIELD, HEIGHT_FIELD;

        /** MenuPanel constructor */
        private MenuPanel(MapMaker m) {
            mapmaker = m;
            setLayout(null);
            setOpaque(false);
            setVisible(true);
            addTextFields();
            addButtons();
        }

        /** Populate the MenuPanel with TextAreas and TextFields */
        private void addTextFields() {
            int yName     = TEXT_INPUT_Y;
            int yWidth    = yName + INPUT_HEIGHT;
            int yHeight   = yWidth + INPUT_HEIGHT;
            NAME_FIELD    = addTextField("Name:", "New Map", yName);
            String width  = (new Integer(map.getTilesWidth())).toString();
            WIDTH_FIELD   = addTextField("Width:", width, yWidth);
            String height = (new Integer(map.getTilesHeight())).toString();
            HEIGHT_FIELD  = addTextField("Height:", height, yHeight);
        }

        private TextField addTextField(String labelTx, String fieldTx, int y) {
            Label label = new Label(labelTx);
            label.setBackground(Color.WHITE);
            label.setBounds(0, y, LABEL_WIDTH, INPUT_HEIGHT);
            TextField field = new TextField(fieldTx);
            int fieldWidth = MENU_WIDTH - LABEL_WIDTH;
            field.setBounds(LABEL_WIDTH, y, fieldWidth, INPUT_HEIGHT);
            add(label);
            add(field);
            return field;
        }

        /** Populate the MenuPanel with JButtons */
        private void addButtons() {
            int xL = MIDDLE - BUTTON_WIDTH, xR = MIDDLE;
            int top = BUTTONS_Y,            low = BUTTONS_Y + BUTTON_HEIGHT;
            addTerrainButton("grass",  xL, top, BUTTON_WIDTH, BUTTON_HEIGHT);
            addTerrainButton("road",   xR, top, BUTTON_WIDTH, BUTTON_HEIGHT);
            addTerrainButton("gravel", xL, low, BUTTON_WIDTH, BUTTON_HEIGHT);
            addTerrainButton("ice",    xR, low, BUTTON_WIDTH, BUTTON_HEIGHT);
            int ySave = WINDOW_HEIGHT - INPUT_HEIGHT - 60;
            int yLoad = ySave - INPUT_HEIGHT;
            addSaveButton(0, ySave, MENU_WIDTH, INPUT_HEIGHT);
            addLoadButton(0, yLoad, MENU_WIDTH, INPUT_HEIGHT);
        }

        private void addTerrainButton(String t, int x, int y, int w, int h) {
            JButton button = addButton(t, x, y, w, h);
            button.addActionListener((ActionEvent e) -> setTerrain(t));
        }

        private void addSaveButton(int x, int y, int w, int h) {
            JButton button = addButton("save map", x, y, w, h);
            button.addActionListener((ActionEvent a) -> {
                ObjectOutputStream out;
                try {
                    String f = String.format("%s/%s.data", SAVE_DIR,
                                             NAME_FIELD.getText());
                    out = new ObjectOutputStream(new FileOutputStream(f));
                    out.writeObject(map);
                    out.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }

        private void addLoadButton(int x, int y, int w, int h) {
            JButton button = addButton("load map", x, y, w, h);
            button.addActionListener((ActionEvent a) -> {
                ObjectInputStream in;
                try {
                    String f = String.format("%s/%s.data", SAVE_DIR,
                            NAME_FIELD.getText());
                    in = new ObjectInputStream(new FileInputStream(f));
                    map = (Map) in.readObject();
                    mapmaker.setMap(map);
                    in.close();
                } catch (Exception e) {
                    e.printStackTrace();
                }
            });
        }

        private JButton addButton(String t, int x, int y, int w, int h) {
            JButton button = new JButton(t);
            button.setBounds(x, y, w, h);
            add(button);
            return button;
        }

    }

    /** MapMaker attributes */
    private Map map;
    private static final int WINDOW_WIDTH, WINDOW_HEIGHT;
    static {
        final Dimension screen = Toolkit.getDefaultToolkit().getScreenSize();
        WINDOW_WIDTH  = screen.width - 200;
        WINDOW_HEIGHT = screen.height - 200;
    }
    private static final int MENU_WIDTH = 200;

    /** MapMaker constructor */
    private MapMaker() {
        setBackground(Color.WHITE);
        /* Initialize scrollable map pane */
        map = new Map();
        JScrollPane scrollPane = new JScrollPane();
        int paneWidth = WINDOW_WIDTH - MENU_WIDTH - 15;
        int paneHeight = WINDOW_HEIGHT - 60;
        scrollPane.setPreferredSize(new Dimension(paneWidth, paneHeight));
        scrollPane.setViewportView(map);
        add(scrollPane);
        /* Initialize menu panel */
        JPanel menuPanel = new MenuPanel(this);
        menuPanel.setPreferredSize(new Dimension(MENU_WIDTH, WINDOW_HEIGHT));
        add(menuPanel);
    }

    /** Set the Map to the one specified */
    private void setMap(Map m) {
        map = m;
    }

    /** Set the terrain pen to the specified terrain type */
    private void setTerrain(String terrainSelection) {
        Tile.terrainSelection = terrainSelection;
    }

    public static void main(String args[]) {
        JFrame frame = new JFrame();
        frame.setPreferredSize(new Dimension(WINDOW_WIDTH, WINDOW_HEIGHT));
        frame.setLocationByPlatform(true);
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setTitle("Map Maker");

        JPanel mainPanel = new MapMaker();
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }

}
// TODO: get height & width text boxes working
// TODO: get save & load working
// TODO: alter WIDTH and HEIGHT inputs to reflect size of loaded map
