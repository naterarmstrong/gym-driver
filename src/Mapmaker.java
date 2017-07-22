import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * Created by robertsweeney on 7/21/17.
 */
public class Mapmaker extends JPanel implements ActionListener {

    private Timer timer;

    public Mapmaker() {
        setBackground(Color.GREEN);
        addMouseListener(new mouseAdapter ());
        addKeyListener(new keyAdapter());
        setFocusable(true);
        setLayout(null);
        timer = new Timer(100, this);
        timer.start();
    }

    public MenuPanel makeMenu() {
        return new MenuPanel();
    }

    @Override
    public void actionPerformed(ActionEvent e) {

    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLACK);
        g.fillOval(600, 50, 10, 10);
    }

    class mouseAdapter extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent event) {

        }
    }

    class keyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent event) {

        }
    }

    public class MenuPanel extends JPanel{

        int height_x = 100, height_y = 100;
        int width_x = 100, width_y = 200;
        int save_x = 100, save_y = 300;


        public MenuPanel() {
            setBackground(Color.GRAY);
            setLayout(null);
            setVisible(true);
            addTextFields();
        }

        private void addTextFields() {
            TextField width_box = new TextField();
            width_box.setBounds(width_x, width_y, 50, 50);
            TextField height_box = new TextField();
            height_box.setBounds(height_x, height_y, 50, 50);
            TextField save_box = new TextField();
            save_box.setBounds(save_x, save_y, 50, 50);
            add(width_box);
            add(height_box);
            add(save_box);
        }



        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);

            //Width String
            g.drawString("WIDTH", width_x, width_y - 2);

            //Height String
            g.drawString("HEIGHT", height_x, height_y - 2);

            //Save String
            g.drawString("SAVE", save_x, save_y - 2);
        }

    }

    public static void main(String args[]) {
        // Initiate and setup preferences for the frame
        JFrame frame = new JFrame();
        frame.setSize(500, 500);
        frame.setLocationByPlatform(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setTitle("Edit Map");
        //Make Map panel and make it scrollable
        Mapmaker map = new Mapmaker();
        JScrollPane scroll = new JScrollPane();
        scroll.setViewportView(map);
        scroll.setPreferredSize(new Dimension(500, 500));
        map.setPreferredSize(new Dimension(1000, 500));
        //Make Menu panel
        JPanel menuPanel = map.makeMenu();
        menuPanel.setPreferredSize(new Dimension(200, 500));
        menuPanel.setBounds(0, 300, 100, 200);
        //Add the Map and Menu panels to a new Main panel
        JPanel mainPanel = new JPanel();
        mainPanel.add(scroll);
        mainPanel.add(menuPanel);
        //Add the Main panel to the frame
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }
}

