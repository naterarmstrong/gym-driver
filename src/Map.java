import java.util.ArrayList;
import javax.swing.JPanel;
import javax.swing.JButton;
import java.awt.Color;

/** Map class */
public class Map extends JPanel {

    /** Tile subclass */
    private class Tile extends JButton {

        /** Tile attributes */
        private static final int PIXELS_PER_TILE = 150;
        private final String[] PATHS = new String[]
                {"flat", "convex", "concave"};
        private final Object[][] TEXTURES = new Object[][]{
                new Object[]{"grass",  0.5, new Color(65, 145, 65)  },
                new Object[]{"gravel", 0.9, new Color(145, 116, 65) },
                new Object[]{"road",   0.5, new Color(86, 81, 72)   },
                new Object[]{"ice",    0.1, new Color(189, 239, 239)}};
        private int pathInd;
        private int textureInd;
        private int orientationInd;

        /** Tile constructors */
        private Tile() {
            this(0, 0, 0);
        }

        private Tile(int p, int t, int o) {
            pathInd = p;
            textureInd = t;
            orientationInd = o;
            setBackground((Color) TEXTURES[textureInd][2]);
        }

        /** Get path shape */
        private String getPath() {
            return PATHS[pathInd];
        }

        /** Get texture index at a specific (x, y) coordinate on the Tile */
        private int getPtTextureInd(int x, int y) {
            String path = getPath();
            if ("flat".equals(path)) {
                return textureInd;
            }
            boolean inCircle = true;
            switch(getOrientation()) {
                case 0:
                    inCircle = inCircle(x, y-PIXELS_PER_TILE);
                    break;
                case 90:
                    inCircle = inCircle(x-PIXELS_PER_TILE, y-PIXELS_PER_TILE);
                    break;
                case 180:
                    inCircle = inCircle(x-PIXELS_PER_TILE, y);
                    break;
                case 270:
                    inCircle = inCircle(x, y);
                    break;
            }
            if ("convex".equals(path)) {
                return (inCircle) ? textureInd : 0;
            } else {
                return (inCircle) ? 0 : textureInd;
            }
        }

        private boolean inCircle(int x, int y) {
            return x * x + y * y <= PIXELS_PER_TILE * PIXELS_PER_TILE;
        }

        /** Get orientation */
        protected int getOrientation() {
            return 90 * orientationInd;
        }

        /** Cycle to the next path */
        protected void cyclePath() {
            if (!"grass".equals(TEXTURES[textureInd][0])) {
                pathInd = (pathInd + 1) % PATHS.length;
            }
        }

        /** Change the texture */
        protected void changeTexture(int newTextureInd) {
            if (newTextureInd < TEXTURES.length) {
                textureInd = newTextureInd;
                setBackground((Color) TEXTURES[textureInd][2]);
                if ("grass".equals(TEXTURES[textureInd][0])) {
                    pathInd = 0;
                }
            }
        }

        /** Cycle to the next orientation */
        protected void cycleOrientation() {
            String path = getPath();
            if ("concave".equals(path) || "convex".equals(path)) {
                orientationInd = (orientationInd + 1) % 4;
            }
        }

        /** Get friction coeff */
        protected double getFriction(int x, int y) {
            int ptTextureInd = getPtTextureInd(x, y);
            return (double) TEXTURES[ptTextureInd][1];
        }

    }

    /** Map attributes */
    private static final int DEFAULT_WIDTH = 15;
    private static final int DEFAULT_HEIGHT = 15;
    private int width, height;
    private ArrayList<ArrayList<Tile>> tiles;

    /** Map constructor */
    public Map() {
        this(DEFAULT_WIDTH, DEFAULT_HEIGHT);
    }

    public Map(int w, int h) {
        width = w;
        height = h;
        tiles = new ArrayList<>();
        for (int i = 0; i < height; i += 1) {
            ArrayList<Tile> row = new ArrayList<>();
            for (int j = 0; j < width; j += 1) {
                row.add(new Tile());
            }
            tiles.add(row);
        }
        setBackground(new Color(65, 136, 145));
    }

    /** Change the Map height */
    public void changeHeight(int newHeight) {
        if (newHeight > height) {
            for (int h = height; h < newHeight; h += 1) {
                ArrayList<Tile> row = new ArrayList<>();
                for (int w = 0; w < width; w += 1) {
                    row.add(new Tile());
                }
                tiles.add(row);
            }
        } else {
            for (int h = height; h > newHeight; h -= 1) {
                tiles.remove(h);
            }
        }
        height = newHeight;
    }

    /** Change the Map width */
    public void changeWidth(int newWidth) {
        if (newWidth > width) {
            for (ArrayList<Tile> row : tiles) {
                for (int w = width; w < newWidth; w += 1) {
                    row.add(new Tile());
                }
            }
        } else {
            for (ArrayList<Tile> row : tiles) {
                for (int w = width; w > newWidth; w -= 1) {
                    row.remove(w);
                }
            }
        }
        width = newWidth;
    }

    /** Get the Tile at a specific (x, y) pixel coordinate in the Map */
    public Tile getTile(int x, int y) {
        int xTile = x / Tile.PIXELS_PER_TILE;
        int yTile = y / Tile.PIXELS_PER_TILE;
        return tiles.get(yTile).get(xTile);
    }

    /** Get friction coeff at a specific (x, y) pixel coordinate in the Map */
    public double getFriction(int x, int y) {
        Tile tile = getTile(x, y);
        int xTile = x % Tile.PIXELS_PER_TILE;
        int yTile = y % Tile.PIXELS_PER_TILE;
        return tile.getFriction(xTile, yTile);
    }

}
