import java.util.ArrayList;

import java.io.Serializable;

import javax.swing.JPanel;

import java.awt.Color;
import java.awt.Dimension;

/** Map class */
class Map extends JPanel implements Serializable {

    /** Map attributes */
    private static final int DEFAULT_WIDTH = 6;
    private static final int DEFAULT_HEIGHT = 4;
    private static final Color BACKGROUND_COLOR = new Color(65, 136, 145);
    private int width, height;
    private ArrayList<ArrayList<Tile>> tiles;

    /** Map constructor */
    Map() {
        this(DEFAULT_WIDTH, DEFAULT_HEIGHT);
    }

    private Map(int w, int h) {
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
        setBackground(BACKGROUND_COLOR);
        setLayout(null);
        render();
    }

    /** Get the width of the Map */
    public int mapWidth() {
        return width;
    }

    /** Get the height of the Map */
    public int mapHeight() {
        return height;
    }

    /** Render the Map */
    private void render() {
        int ppt = Tile.PIXELS_PER_TILE;
        setPreferredSize(new Dimension(width * ppt, height * ppt));
        for (int i = 0; i < height; i += 1) {
            ArrayList<Tile> row = tiles.get(i);
            for (int j = 0; j < width; j += 1) {
                Tile tile = row.get(j);
                tile.setBounds(j * ppt, i * ppt, ppt, ppt);
                tile.setOpaque(true);
                tile.setBorderPainted(false);
                add(tile);
            }
        }
    }

    /** Change the Map height */
    void setHeight(int newHeight) {
        if (newHeight >= height) {
            for (int h = height; h < newHeight; h += 1) {
                ArrayList<Tile> row = new ArrayList<>();
                for (int w = 0; w < width; w += 1) {
                    row.add(new Tile());
                }
                tiles.add(row);
            }
        } else {
            for (int h = height; h > newHeight; h -= 1) {
                ArrayList<Tile> row = tiles.get(h - 1);
                for (Tile t: row) {
                    remove(t);
                }
                tiles.remove(h - 1);
            }
        }
        height = newHeight;
        render();
    }

    /** Change the Map width */
    void setWidth(int newWidth) {
        if (newWidth >= width) {
            for (ArrayList<Tile> row : tiles) {
                for (int w = width; w < newWidth; w += 1) {
                    row.add(new Tile());
                }
            }
        } else {
            for (ArrayList<Tile> row : tiles) {
                for (int w = width; w > newWidth; w -= 1) {
                    remove(row.get(w-1));
                    row.remove(w - 1);
                }
            }
        }
        width = newWidth;
        render();
    }

    /** Get the Tile at a specific (x, y) pixel coordinate in the Map */
    private Tile getTile(int x, int y) {
        int xTile = x / Tile.PIXELS_PER_TILE;
        int yTile = y / Tile.PIXELS_PER_TILE;
        return tiles.get(yTile).get(xTile);
    }

    /** Get friction coeff at a specific (x, y) pixel coordinate in the Map */
    private double getFriction(int x, int y) {
        Tile tile = getTile(x, y);
        int xTile = x % Tile.PIXELS_PER_TILE;
        int yTile = y % Tile.PIXELS_PER_TILE;
        return tile.getFriction(xTile, yTile);
    }

}
