import java.io.FileOutputStream;
import java.io.ObjectOutputStream;

import javax.swing.JScrollPane;

import java.awt.TextField;
import java.awt.event.ActionEvent;

/** MakerPanel class */
class MakerPanel extends Panel {

    /** MakerPanel attributes */
    private static final int RESIZE_Y   = TOP;
    private static final int TERRAIN_Y  = 200;
    private static final int NUM_CPUS_Y = 250;
    private static final int ZOOM_Y     = 350;
    private static final int UPDATE_W   = 60;
    private static final int TERRAIN_W  = MIDDLE;
    private static final int TERRAIN_H  = 50;
    private static final int ZOOM_WH    = 20;
    private static final int ZOOM_STEP  = 25;
    private TextField NAME_FIELD, WIDTH_FIELD, HEIGHT_FIELD, CPUS_FIELD;

    /** MakerPanel constructor */
    MakerPanel(MakerMenu m) {
        super(m);
        addResizeOptions();
        addTerrainOptions();
        addNumCPUSOptions();
        addZoomOptions();
        addSaveOption();
        addBackOption();
    }

    /** Populate the MakerPanel with Map-resize options */
    private void addResizeOptions() {
        Map map          = getMap();
        int yResizeW     = RESIZE_Y;
        int yResizeH     = yResizeW + INPUT_H;
        int fieldWidth   = PANEL_WIDTH - LABEL_W - UPDATE_W;
        String w         = (new Integer(map.mapWidth())).toString();
        WIDTH_FIELD      = addTextField("Width:", w, yResizeW, fieldWidth);
        String h         = (new Integer(map.mapHeight())).toString();
        HEIGHT_FIELD     = addTextField("Height:", h, yResizeH, fieldWidth);
        int xUpdate      = PANEL_WIDTH - UPDATE_W;
        int updateHeight = 2 * INPUT_H;
        addButton("Update", xUpdate, yResizeW, UPDATE_W, updateHeight,
                (ActionEvent a) -> {
                    try {
                        String wField = WIDTH_FIELD.getText();
                        int newWidth  = Integer.valueOf(wField);
                        String hField = HEIGHT_FIELD.getText();
                        int newHeight = Integer.valueOf(hField);
                        changeMapSize(newWidth, newHeight);
                    } catch (NumberFormatException e) {
                        e.printStackTrace();
                    }
                });
    }

    /** Populate the MakerPanel with toggle-terrain options */
    private void addTerrainOptions() {
        int xR  = MIDDLE;
        int xL  = xR - TERRAIN_W;
        int top = TERRAIN_Y;
        int low = top + TERRAIN_H;
        addTerrainButton("grass",  xL, top, TERRAIN_W, TERRAIN_H);
        addTerrainButton("road",   xR, top, TERRAIN_W, TERRAIN_H);
        addTerrainButton("gravel", xL, low, TERRAIN_W, TERRAIN_H);
        addTerrainButton("ice",    xR, low, TERRAIN_W, TERRAIN_H);
    }

    private void addTerrainButton(String t, int x, int y, int w, int h) {
        addButton(t, x, y, w, h, (ActionEvent e) -> setTerrain(t));
    }

    /** Populate the MakerPanel with options to adjust the number of CPUs */
    private void addNumCPUSOptions() {
        String numCPUs = String.valueOf(getMap().getNumCPUs());
        CPUS_FIELD     = addTextField("Num. CPUs:", numCPUs, NUM_CPUS_Y, PANEL_WIDTH - LABEL_W);
    }

    /** Populate the MakerPanel with zoom-in and zoom-out options */
    private void addZoomOptions() {
        int xR = MIDDLE;
        int xL = MIDDLE - ZOOM_WH;
        addButton("+", xL, ZOOM_Y, ZOOM_WH, ZOOM_WH,
                (ActionEvent a) -> {
                    Map map       = getMap();
                    int PPT       = Tile.PIXELS_PER_TILE;
                    int stdZoom   = PPT + ZOOM_STEP;
                    if (stdZoom < PANE_WIDTH && stdZoom < PANE_HEIGHT) {
                        Tile.setPPT(stdZoom);
                    }
                    map.render();
                });
        addButton("-", xR, ZOOM_Y, ZOOM_WH, ZOOM_WH,
                (ActionEvent a) -> {
                    Map map       = getMap();
                    int PPT       = Tile.PIXELS_PER_TILE;
                    int minWidth  = PANE_WIDTH / map.mapWidth();
                    int minHeight = PANE_HEIGHT / map.mapHeight();
                    int stdZoom   = PPT - ZOOM_STEP;
                    if (minWidth < stdZoom || minHeight < stdZoom) {
                        Tile.setPPT(stdZoom);
                    } else {
                        Tile.setPPT(Math.min(minWidth, minHeight));
                    }
                    map.render();
                });
    }

    /** Populate the MakerPanel with save options */
    private void addSaveOption() {
        Map map       = getMap();
        int ySave     = BOTTOM - INPUT_H;
        int yName     = ySave - INPUT_H;
        int nameWidth = PANEL_WIDTH - LABEL_W;
        addButton("save map", 0, ySave, PANEL_WIDTH, INPUT_H,
                (ActionEvent a) -> {
                    ObjectOutputStream out;
                    try {
                        String tag = NAME_FIELD.getText();
                        map.setTag(tag);
                        int CPUs   = Integer.valueOf(CPUS_FIELD.getText());
                        map.setCPUS(CPUs);
                        String dir = String.format("%s/%s%s",
                                SAVE_DIR, tag, SAVE_EXT);
                        FileOutputStream f = new FileOutputStream(dir);
                        out = new ObjectOutputStream(f);
                        out.writeObject(map);
                        out.close();
                    } catch (Exception e) {
                        e.printStackTrace();
                    }
                });
        NAME_FIELD = addTextField("Name:", map.getTag(), yName, nameWidth);
    }

    /** Set the terrain pen to the specified terrain type */
    private void setTerrain(String terrainSelection) {
        Tile.terrainSelection = terrainSelection;
    }

    /** Change the dimensions of the Map */
    private void changeMapSize(int width, int height) {
        Map map                = getMap();
        JScrollPane scrollPane = getPane();
        map.setWidth(width);
        map.setHeight(height);
        scrollPane.updateUI();
    }

    /** Update fields in the MakerPanel after changing the Map */
    void updateFields() {
    }

}
