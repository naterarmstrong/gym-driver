import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Label;
import java.awt.TextField;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

/** Panel class */
abstract class Panel extends Menu {

    /** Panel attributes */
    static final int MIDDLE  = PANEL_WIDTH / 2;
    static final int MARGIN  = 2;
    static final int LABEL_W = 50;
    static final int INPUT_H = 25;
    static final int BOTTOM  = WINDOW_HEIGHT - INPUT_H - 60;
    private Menu menu;

    /** Panel constructor */
    Panel(MapMenu m) {
        menu       = m;
        map        = menu.map;
        scrollPane = menu.scrollPane;
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

}
