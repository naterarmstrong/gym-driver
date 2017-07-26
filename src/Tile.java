import java.util.HashMap;

import javax.swing.JButton;
import javax.swing.SwingUtilities;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;

/** Tile subclass */
class Tile extends JButton {

    /** Tile attributes */
    static int PIXELS_PER_TILE = 150;
    private static final HashMap<String, Object[]> TEXTURES = new HashMap<>();
    static {
        TEXTURES.put("grass",  new Object[]{0.5, new Color(65,  145, 65 )});
        TEXTURES.put("gravel", new Object[]{0.9, new Color(145, 116, 65 )});
        TEXTURES.put("road",   new Object[]{0.5, new Color(86,  81,  72 )});
        TEXTURES.put("ice",    new Object[]{0.1, new Color(189, 239, 239)});
    }
    private static final String[] PATHS = new String[]
            {"flat", "convex", "concave"};
    private static boolean pressed;
    static String terrainSelection;
    private String texture;
    private int pathInd;
    private int orientationInd;

    /** Tile constructors */
    Tile() {
        this("grass", 0, 0);
    }

    private Tile(String t, int p, int o) {
        texture = t;
        pathInd = p;
        orientationInd = o;
        setBackground(getColor(texture));
        setActionCommand("change texture");
        addMouseListener(new MouseListener() {

            @Override
            public void mouseEntered(MouseEvent e) {
                requestFocus();
                if (pressed) {
                    changeTexture(terrainSelection);
                }
            }

            @Override
            public void mouseExited(MouseEvent e) {
            }

            @Override
            public void mouseClicked(MouseEvent e) {
            }

            @Override
            public void mousePressed(MouseEvent e) {
                if (SwingUtilities.isLeftMouseButton(e)) {
                    pressed = true;
                    changeTexture(terrainSelection);
                } else if (SwingUtilities.isRightMouseButton(e)) {
                    cyclePath();
                }
            }

            @Override
            public void mouseReleased(MouseEvent e) {
                pressed = false;
            }

        });
        addKeyListener(new KeyListener() {

            @Override
            public void keyTyped(KeyEvent e) {
                if (e.getKeyChar() == 'r') {
                    cycleOrientation();
                }
            }

            @Override
            public void keyPressed(KeyEvent e) {
            }

            @Override
            public void keyReleased(KeyEvent e) {
            }

        });
    }

    /** Update PIXELS_PER_TILE */
    static void setPPT(int pixelsPerTile) {
        PIXELS_PER_TILE = pixelsPerTile;
    }

    /** Get the friction coefficient for the specified texture */
    double getFriction(int x, int y) {
        String ptTexture = getPtTextureInd(x, y);
        return getFriction(ptTexture);
    }

    private static double getFriction(String texture) {
        return (double) TEXTURES.get(texture)[0];
    }

    /** Get the Color for the specified texture */
    private static Color getColor(String texture) {
        return (Color) TEXTURES.get(texture)[1];
    }

    /** Get path shape */
    private String getPath() {
        return PATHS[pathInd];
    }

    /** Get texture at a specific (x, y) coordinate on the Tile */
    private String getPtTextureInd(int x, int y) {
        String path = getPath();
        if ("flat".equals(path)) {
            return texture;
        }
        boolean inCircle = true;
        switch(getOrientation()) {
            case 0:
                inCircle = inCircle(x, y - PIXELS_PER_TILE);
                break;
            case 90:
                inCircle = inCircle(x - PIXELS_PER_TILE, y - PIXELS_PER_TILE);
                break;
            case 180:
                inCircle = inCircle(x - PIXELS_PER_TILE, y);
                break;
            case 270:
                inCircle = inCircle(x, y);
                break;
        }
        if ("convex".equals(path)) {
            return (inCircle) ? texture : "grass";
        } else {
            return (inCircle) ? "grass" : texture;
        }
    }

    private boolean inCircle(int x, int y) {
        return x * x + y * y <= PIXELS_PER_TILE * PIXELS_PER_TILE;
    }

    /** Get orientation */
    private int getOrientation() {
        return 90 * orientationInd;
    }

    /** Cycle to the next path */
    private void cyclePath() {
        if (!"grass".equals(texture)) {
            pathInd = (pathInd + 1) % PATHS.length;
            paint(getGraphics());
        }
    }

    /** Change the texture */
    private void changeTexture(String newTexture) {
        if (TEXTURES.containsKey(newTexture)) {
            texture = newTexture;
            setBackground(getColor(texture));
            if ("grass".equals(texture)) {
                pathInd = 0;
            }
        }
    }

    /** Cycle to the next orientation */
    private void cycleOrientation() {
        String path = getPath();
        if ("concave".equals(path) || "convex".equals(path)) {
            orientationInd = (orientationInd + 1) % 4;
            paint(getGraphics());
        }
    }

    /** Draw the Tile */
    @Override
    public void paint(Graphics g) {
        super.paintComponent(g);
        for (int i = 0; i < PIXELS_PER_TILE; i += 1) {
            for (int j = 0; j < PIXELS_PER_TILE; j += 1) {
                String texture = getPtTextureInd(i, j);
                Color color = getColor(texture);
                g.setColor(color);
                g.fillRect(i, j, 1, 1);
            }
        }
    }

}
