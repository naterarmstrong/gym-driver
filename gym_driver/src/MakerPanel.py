from Panel import Panel

from read_config import read_config

configs = read_config()
DEFAULT_TERRAIN = configs["DEFAULT_TERRAIN"]
RESIZE_Y = configs["RESIZE_Y"]
CHNG_TERRAIN_Y = configs["CHNG_TERRAIN_Y"]
NUM_CPUS_Y = configs["NUM_CPUS_Y"]
UPDATE_W = configs["UPDATE_W"]
CHNG_TERRAIN_W = configs["CHNG_TERRAIN_W"]
CHNG_TERRAIN_H = configs["CHNG_TERRAIN_H"]

# MakerPanel class
class MakerPanel(Panel):

    # MakerPanel constructor
    def __init__(self, maker_menu):
        Panel.__init__(self, maker_menu)
        self.add_buttons()
        self.terrain_selection = DEFAULT_TERRAIN

    # Populate the MakerPanel with buttons
    def add_buttons(self):
        self.add_resize()
        self.add_chng_terrain()
        self.add_num_CPUs()
        self.add_save()
        self.add_back()

    def add_resize(self):
        None

    def add_chng_terrain(self):
        None

    def add_num_CPUs(self):
        None

    def add_save(self):
        None

    def add_back(self):
        None

#     private TextField WIDTH_FIELD, HEIGHT_FIELD, NUM_CPUS_FIELD, NAME_FIELD;
#
#     /** Populate the MakerPanel with Map-resize options */
#     private void addResizeOptions() {
#         Map map          = getMap();
#         int yResizeW     = RESIZE_Y;
#         int yResizeH     = yResizeW + INPUT_H;
#         int fieldWidth   = PANEL_WIDTH - LABEL_W - UPDATE_W;
#         String w         = (new Integer(map.mapWidth())).toString();
#         WIDTH_FIELD      = addTextField("Width:", w, yResizeW, fieldWidth);
#         String h         = (new Integer(map.mapHeight())).toString();
#         HEIGHT_FIELD     = addTextField("Height:", h, yResizeH, fieldWidth);
#         int xUpdate      = PANEL_WIDTH - UPDATE_W;
#         int updateHeight = 2 * INPUT_H;
#         addButton("Update", xUpdate, yResizeW, UPDATE_W, updateHeight,
#                 (ActionEvent a) -> {
#                     try {
#                         String wField = WIDTH_FIELD.getText();
#                         int newWidth  = Integer.valueOf(wField);
#                         String hField = HEIGHT_FIELD.getText();
#                         int newHeight = Integer.valueOf(hField);
#                         changeMapSize(newWidth, newHeight);
#                     } catch (NumberFormatException e) {
#                         e.printStackTrace();
#                     }
#                 });
#     }
#
#     /** Populate the MakerPanel with toggle-terrain options */
#     private void addTerrainOptions() {
#         int xR  = MIDDLE;
#         int xL  = xR - TERRAIN_W;
#         int top = TERRAIN_Y;
#         int low = top + TERRAIN_H;
#         addTerrainButton("grass",  xL, top, TERRAIN_W, TERRAIN_H);
#         addTerrainButton("road",   xR, top, TERRAIN_W, TERRAIN_H);
#         addTerrainButton("gravel", xL, low, TERRAIN_W, TERRAIN_H);
#         addTerrainButton("ice",    xR, low, TERRAIN_W, TERRAIN_H);
#     }
#
#     private void addTerrainButton(String t, int x, int y, int w, int h) {
#         addButton(t, x, y, w, h, (ActionEvent e) -> setTerrain(t));
#     }
#
#     /** Populate the MakerPanel with options to adjust the number of CPUs */
#     private void addNumCPUsOptions() {
#         String numCPUs = String.valueOf(getMap().getNumCPUs());
#         int CPUs_W     = PANEL_WIDTH - LABEL_W;
#         NUM_CPUS_FIELD = addTextField("CPUs:", numCPUs, NUM_CPUS_Y, CPUs_W);
#     }
#
#     /** Populate the MakerPanel with zoom-in and zoom-out options */
#     private void addZoomOptions() {
#         int xR = MIDDLE;
#         int xL = MIDDLE - ZOOM_WH;
#         addButton("+", xL, ZOOM_Y, ZOOM_WH, ZOOM_WH,
#                 (ActionEvent a) -> {
#                     Map map       = getMap();
#                     int PPT       = Tile.PIXELS_PER_TILE;
#                     int stdZoom   = PPT + ZOOM_STEP;
#                     if (stdZoom < PANE_WIDTH && stdZoom < PANE_HEIGHT) {
#                         Tile.setPPT(stdZoom);
#                     }
#                     map.render();
#                 });
#         addButton("-", xR, ZOOM_Y, ZOOM_WH, ZOOM_WH,
#                 (ActionEvent a) -> {
#                     Map map       = getMap();
#                     int PPT       = Tile.PIXELS_PER_TILE;
#                     int minWidth  = PANE_WIDTH / map.mapWidth();
#                     int minHeight = PANE_HEIGHT / map.mapHeight();
#                     int stdZoom   = PPT - ZOOM_STEP;
#                     if (minWidth < stdZoom || minHeight < stdZoom) {
#                         Tile.setPPT(stdZoom);
#                     } else {
#                         Tile.setPPT(Math.min(minWidth, minHeight));
#                     }
#                     map.render();
#                 });
#     }
#
#     /** Populate the MakerPanel with save options */
#     private void addSaveOption() {
#         Map map       = getMap();
#         int ySave     = BOTTOM - INPUT_H;
#         int yName     = ySave - INPUT_H;
#         int nameWidth = PANEL_WIDTH - LABEL_W;
#         addButton("save map", 0, ySave, PANEL_WIDTH, INPUT_H,
#                 (ActionEvent a) -> {
#                     ObjectOutputStream out;
#                     try {
#                         String tag = NAME_FIELD.getText();
#                         map.setTag(tag);
#                         int CPUs = Integer.valueOf(NUM_CPUS_FIELD.getText());
#                         map.setNumCPUs(CPUs);
#                         String dir = String.format("%s/%s%s",
#                                 SAVE_DIR, tag, SAVE_EXT);
#                         FileOutputStream f = new FileOutputStream(dir);
#                         out = new ObjectOutputStream(f);
#                         out.writeObject(map);
#                         out.close();
#                     } catch (Exception e) {
#                         e.printStackTrace();
#                     }
#                 });
#         NAME_FIELD = addTextField("Name:", map.getTag(), yName, nameWidth);
#     }
#
#     /** Set the terrain pen to the specified terrain type */
#     private void setTerrain(String terrainSelection) {
#         Tile.terrainSelection = terrainSelection;
#     }
#
#     /** Change the dimensions of the Map */
#     private void changeMapSize(int width, int height) {
#         Map map                = getMap();
#         JScrollPane scrollPane = getPane();
#         map.setWidth(width);
#         map.setHeight(height);
#         scrollPane.updateUI();
#     }
#
#     /** Update fields in the MakerPanel after changing the Map */
#     void updateFields() {
#     }
