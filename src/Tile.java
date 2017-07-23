import java.util.HashMap;

import javax.swing.JButton;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;

/** Tile subclass */
class Tile extends JButton implements ActionListener {

    /** Tile attributes */
    static final int PIXELS_PER_TILE = 150;
    private static final HashMap<String, Object[]> TEXTURES = new HashMap<>();
    static {
        TEXTURES.put("grass",  new Object[]{0.5, new Color(65,  145, 65 )});
        TEXTURES.put("gravel", new Object[]{0.9, new Color(145, 116, 65 )});
        TEXTURES.put("road",   new Object[]{0.5, new Color(86,  81,  72 )});
        TEXTURES.put("ice",    new Object[]{0.1, new Color(189, 239, 239)});
    }
    private static final String[] PATHS = new String[]
            {"flat", "convex", "concave"};
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
        setBackground((Color) TEXTURES.get(texture)[1]);
        setActionCommand("change texture");
        setMnemonic(KeyEvent.VK_D);
        addActionListener(this);
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
        }
    }

    /** Change the texture */
    private void changeTexture(String newTexture) {
        if (TEXTURES.containsKey(newTexture)) {
            texture = newTexture;
            setBackground((Color) TEXTURES.get(texture)[1]);
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
        }
    }

    /** Get friction coeff */
    double getFriction(int x, int y) {
        String ptTexture = getPtTextureInd(x, y);
        return (double) TEXTURES.get(ptTexture)[0];
    }

    /** Change texture on click */
    @Override
    public void actionPerformed(ActionEvent e) {
        if ("change texture".equals(e.getActionCommand())) {
            changeTexture(terrainSelection);
        }
    }

}
