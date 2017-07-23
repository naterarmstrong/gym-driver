import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JScrollPane;
import java.awt.TextField;
import java.awt.Graphics;
import java.awt.Dimension;
import java.awt.Toolkit;
import java.awt.Color;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;

public class Mapmaker extends JPanel {

    public  String TerrainType = "Green";
    public Map map;

    public Mapmaker() {
    }

    public Mapmaker(Map m) {
        map = m;
        addMouseListener(new Mouse());
    }

    public  void setTerrain(String i) {
        TerrainType = i;
    }

    public void changeTerrain() {
        Tile.terrainSelection = TerrainType;
    }

    public MenuPanel makeMenu() {
        return new MenuPanel();
    }

    class Mouse extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent event) {
            int xPress = event.getX();
            int yPress = event.getY();
            System.out.println("x: " + String.valueOf(xPress) + " y: " + String.valueOf(yPress));
        }
    }

    public class MenuPanel extends JPanel {

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
                    System.out.println("SAVE");
                }
            });
            add(save_button);

            //Grass
            grass_button = new JButton("GRASS");
            grass_button.setBounds(0, 200, 100, 50);
            grass_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrain("grass");
                }
            });
            add(grass_button);

            //Road
            road_button = new JButton("ROAD");
            road_button.setBounds(100, 200, 100, 50);
            road_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrain("road");
                }
            });
            add(road_button);

            //Gravel
            gravel_button = new JButton("GRAVEL");
            gravel_button.setBounds(0, 300, 100, 50);
            gravel_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrain("gravel");
                }
            });
            add(gravel_button);

            //Ice
            ice_button = new JButton("ICE");
            ice_button.setBounds(100, 300, 100, 50);
            ice_button.addActionListener(new ActionListener() {
                @Override
                public void actionPerformed(ActionEvent e) {
                    setTerrain("ice");
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
        //Make Menu panel
        JPanel menuPanel = new Mapmaker().makeMenu();
        //Set Dimensions for Menu Panel
        menuPanel.setPreferredSize(new Dimension(200, fullscreen_height - 200));
        menuPanel.setBounds(0, 300, 100, 200);
        //Add the Map and Menu panels to a new Main panel
        JPanel mainPanel = new Mapmaker(map);
        mainPanel.add(scroll);
        mainPanel.add(menuPanel);
        mainPanel.setBackground(Color.WHITE);
        //Add the Main panel to the frame
        frame.getContentPane().add(mainPanel);
        frame.pack();
    }
}

