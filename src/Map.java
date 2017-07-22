import java.util.ArrayList;
import java.util.HashMap;

/** Map class */
public class Map {

    /** Tile subclass */
    private class Tile {

        /** Tile attributes */
        private static final int PIXELS_PER_TILE = 100;
        private final String[] PATHS = new String[]
                {"flat", "convex", "concave"};
        private final String[] TEXTURES = new String[]
                {"grass", "gravel", "road", "ice"};
        private int pathInd;
        private int textureInd;
        private int orientationInd;

        /** Tile constructors */
        private Tile() {
            new Tile(0, 0, 0);
        }

        private Tile(int p, int t, int o) {
            pathInd = p;
            textureInd = t;
            orientationInd = o;
        }

        /** Getters for path, texture, and orientation attributes */
        private String getPath() {
            return PATHS[pathInd];
        }

        private String getTexture() {
            return TEXTURES[textureInd];
        }

        protected int getOrientation() {
            return 90 * orientationInd;
        }

        /** Cycle to the next path */
        protected void cyclePath() {
            pathInd = (pathInd + 1) % PATHS.length;
        }

        /** Change the texture */
        protected void changeTexture(int newTexture) {
            if (newTexture < TEXTURES.length) {
                textureInd = newTexture;
            }
        }

        /** Cycle to the next orientation */
        protected void cycleOrientation() {
            String path = getPath();
            if ("concave".equals(path) || "convex".equals(path)) {
                orientationInd = (orientationInd + 1) % 4;
            }
        }

        /** Get the friction coefficient */
        protected double getFrictionCoeff(String texture) {
            switch(texture) {
                case "grass":
                    return 0.5;
                case "gravel":
                    return 0.9;
                case "road":
                    return 0.5;
                case "ice":
                    return 0.1;
                default:
                    return 0.5;
            }
        }

        protected double getFrictionCoeff() {
            String texture = getTexture();
            // what about convex, concave
        }

    }

    /** Map attributes */
    private static final int DEFAULT_WIDTH = 10;
    private static final int DEFAULT_HEIGHT = 10;
    private int width, height;
    private ArrayList<ArrayList<Tile>> tiles;

    /** Map constructor */
    public Map() {
        new Map(DEFAULT_WIDTH, DEFAULT_HEIGHT);
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
    }

    /** Get the Tile at a specific (x, y) pixel coordinate in the Map */
    public Tile getTile(int x, int y) {
        int xTile = x / Tile.PIXELS_PER_TILE;
        int yTile = y / Tile.PIXELS_PER_TILE;
        return tiles.get(y).get(x);
    }

}
