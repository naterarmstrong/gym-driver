import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * Created by robertsweeney on 7/21/17.
 */
public class Mapmaker extends JPanel implements ActionListener {

    Map map;
    public static String terrainType;

    public Mapmaker() {
        setBackground(Color.GREEN);
        addMouseListener(new mouseAdapter ());
        addKeyListener(new keyAdapter());
        setFocusable(true);
        setLayout(null);
        map = new Map();
    }

    static String getTerrain() {
        return terrainType;
    }

    static void setTerrainType(String newTerrainSelection) {
        terrainType = newTerrainSelection;
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
    }

    class mouseAdapter extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent event) {
            int xPress = event.getX();
            int yPress = event.getY();
            System.out.println("x: " + String.valueOf(xPress) + " y: " + String.valueOf(yPress));
        }

        public void mouseEntered(MouseEvent event) {
        }

    }

    class keyAdapter extends KeyAdapter {
        @Override
        public void keyPressed(KeyEvent event) {

        }
    }

    public class MenuPanel extends Mapmaker {

        int width_x = 65, width_y = 30;
        int height_x = 65, height_y = 80;
        JButton save_button, grass_button, road_button, gravel_button, ice_button;


        public MenuPanel() {
            setOpaque(false);
            setLayout(null);
            setVisible(true);
            addTextFields();
            addButtons();
        }

        private void addTextFields() {
            TextField width_box = new TextField();
            width_box.setBounds(width_x, width_y, 100, 20);
            TextField height_box = new TextField();
            height_box.setBounds(height_x, height_y, 100, 20);
            add(width_box);
            add(height_box);
        }

        private void addButtons() {

            //Save
            save_button = new JButton("SAVE");
            save_button.setBounds(50, 400, 100, 50);
            save_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {

                }
            });
            add(save_button);

            //Grass
            grass_button = new JButton("GRASS");
            grass_button.setBounds(0, 200, 100, 50);
            grass_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrainType("grass");
                }
            });
            add(grass_button);

            //Road
            road_button = new JButton("ROAD");
            road_button.setBounds(100, 200, 100, 50);
            road_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrainType("road");
                }
            });
            add(road_button);

            //Gravel
            gravel_button = new JButton("GRAVEL");
            gravel_button.setBounds(0, 300, 100, 50);
            gravel_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrainType("gravel");
                }
            });
            add(gravel_button);

            //Ice
            ice_button = new JButton("ICE");
            ice_button.setBounds(100, 300, 100, 50);
            ice_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrainType("ice");
                }
            });
            add(ice_button);
        }



        @Override
        public void paintComponent(Graphics g) {
            super.paintComponent(g);

            //Width String
            g.drawString("WIDTH:", width_x - 50, width_y + 15);

            //Height String
            g.drawString("HEIGHT:", height_x - 52, height_y + 15);
        }

    }

    public static void main(String args[]) {
        // Calculate Dimensions for full screen
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();
        int fullscreen_width = screenSize.width;
        int fullscreen_height = screenSize.height;
        // Initiate and setup preferences for the frame
        JFrame frame = new JFrame();
        frame.setPreferredSize(new Dimension(fullscreen_width, fullscreen_height - 175));
        frame.setLocationByPlatform(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setResizable(false);
        frame.setTitle("Edit Map");
        //Make Map panel and make it scrollable
        Map map = new Map();
        JScrollPane scroll = new JScrollPane();
        scroll.setViewportView(map);
        //Set Dimensions for Map
        scroll.setPreferredSize(new Dimension(fullscreen_width - 210, fullscreen_height - 200));
        map.setPreferredSize(new Dimension(fullscreen_width, fullscreen_height - 200));
        //Make Menu panel
        JPanel menuPanel = new Mapmaker().makeMenu();
        //Set Dimensions for Menu Panel
        menuPanel.setPreferredSize(new Dimension(200, fullscreen_height - 200));
        menuPanel.setBounds(0, 300, 100, 200);
        //Add the Map and Menu panels to a new Main panel
        JPanel mainPanel = new Mapmaker();
        mainPanel.add(scroll);
        mainPanel.add(menuPanel);
        mainPanel.setBackground(Color.WHITE);
        //Add the Main panel to the frame
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }
}

