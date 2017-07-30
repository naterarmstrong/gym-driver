import javax.swing.*;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

/** Panel class */
abstract class Panel extends JPanel {

    /** Panel attributes */
    static final String SAVE_DIR  = "saved maps";
    static final String SAVE_EXT  = ".ser";
    static final int WINDOW_WIDTH  = Menu.WINDOW_WIDTH;
    static final int WINDOW_HEIGHT = Menu.WINDOW_HEIGHT;
    static final int PANEL_WIDTH   = Menu.PANEL_WIDTH;
    static final int PANEL_HEIGHT  = Menu.PANEL_HEIGHT;
    static final int PANE_WIDTH    = Menu.PANE_WIDTH;
    static final int PANE_HEIGHT   = Menu.PANE_HEIGHT;
    static final int TOP           = 30;
    static final int MIDDLE        = PANEL_WIDTH / 2;
    static final int MARGIN        = 2;
    static final int LABEL_W       = 50;
    static final int INPUT_H       = 25;
    static final int BOTTOM        = WINDOW_HEIGHT - INPUT_H - 60;
    Menu menu;

    /** Panel constructor */
    Panel(MapMenu m) {
        menu       = m;
        setLayout(null);
        setOpaque(false);
        setVisible(true);
        setPreferredSize(new Dimension(PANEL_WIDTH, PANEL_HEIGHT));
    }

    /** Utility method for populating the Panel with TextFields */
    TextField addTextField(String lTx, String fTx, int y, int w) {
        Label label = new Label(lTx);
        label.setBackground(Color.WHITE);
        label.setBounds(0, y, LABEL_W, INPUT_H);
        TextField field = new TextField(fTx);
        field.setBounds(LABEL_W, y, w, INPUT_H);
        add(label);
        add(field);
        return field;
    }

    /** Utility method for populating the Panel with JButtons */
    JButton addButton(String t, int x, int y, int w, int h,
                              ActionListener a) {
        JButton button = new JButton(t);
        button.setBounds(x + MARGIN, y + MARGIN, w - MARGIN, h - MARGIN);
        button.addActionListener(a);
        button.setBorder(BorderFactory.createLineBorder(Color.BLACK));
        add(button);
        return button;
    }

    /** Populate the MakerPanel with back options */
    void addBackOption() {
        addButton("main menu", 0, BOTTOM, PANEL_WIDTH, INPUT_H,
                (ActionEvent a) -> {
                    JFrame frame = (JFrame)
                            SwingUtilities.getWindowAncestor(menu);
                    frame.remove(menu);
                    try {
                        frame.getContentPane().add(new MainMenu());
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                    frame.pack();
                });
    }

    /** Get the Menu's Map */
    Map getMap() {
        return menu.map;
    }

    /** Get the Menu's JScrollPane */
    JScrollPane getPane() {
        return menu.scrollPane;
    }

    /** Set the Menu's Map to the one specified */
    void setMap(Map m) {
        menu.map = m;
        menu.scrollPane.setViewportView(m);
        updateFields();
    }

    /** Update fields in the Panel after changing the Map */
    abstract void updateFields();

}
