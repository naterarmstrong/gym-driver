# Map class
class Map:

    None

# /** Map class */
# class Map extends JPanel implements Serializable {
#
#     /** Map attributes */
#     private static final int DEFAULT_WIDTH      = 6;
#     private static final int DEFAULT_HEIGHT     = 4;
#     private static final int DEFAULT_NUM_CPUS   = 4;
#     private static final String DEFAULT_TAG     = "New Map";
#     private static final Color BACKGROUND_COLOR = new Color(65, 136, 145);
#     private int width, height;
#     private int numCPUs;
#     private String tag;
#     private ArrayList<ArrayList<Tile>> tiles;
#     private Tile startTile;
#     private double startAngle;
#
#     /** Map constructors */
#     Map() {
#         this(DEFAULT_WIDTH, DEFAULT_HEIGHT);
#     }
#
#     Map(int w, int h) {
#         width = w;
#         height = h;
#         tiles = new ArrayList<>();
#         for (int i = 0; i < height; i += 1) {
#             ArrayList<Tile> row = new ArrayList<>();
#             for (int j = 0; j < width; j += 1) {
#                 row.add(new Tile(this));
#             }
#             tiles.add(row);
#         }
#         tag = DEFAULT_TAG;
#         if (tiles.size() != 0) {
#             setStartTile(tiles.get(0).get(0));
#         } else {
#             setStartTile(null);
#         }
#         numCPUs = DEFAULT_NUM_CPUS;
#         setBackground(BACKGROUND_COLOR);
#         setLayout(null);
#         render();
#     }
#
#     /** Get the width of the Map */
#     int mapWidth() {
#         return width;
#     }
#
#     /** Get the height of the Map */
#     int mapHeight() {
#         return height;
#     }
#
#     /** Get the number of CPUs to be generated on the Map */
#     int getNumCPUs() {
#         return numCPUs;
#     }
#
#     /** Get the tag of the Map */
#     String getTag() {
#         return tag;
#     }
#
#     /** Get the Tile where the UserCar will start */
#     Tile setStartTile() {
#         return startTile;
#     }
#
#     /** Get the angle at which the UserCar will start */
#     double setStartAngle() {
#         return startAngle;
#     }
#
#     /** Change the Map height */
#     void setHeight(int newHeight) {
#         if (newHeight >= height) {
#             for (int h = height; h < newHeight; h += 1) {
#                 ArrayList<Tile> row = new ArrayList<>();
#                 for (int w = 0; w < width; w += 1) {
#                     row.add(new Tile(this));
#                 }
#                 tiles.add(row);
#             }
#         } else {
#             for (int h = height; h > newHeight; h -= 1) {
#                 ArrayList<Tile> row = tiles.get(h - 1);
#                 for (Tile t: row) {
#                     remove(t);
#                 }
#                 tiles.remove(h - 1);
#             }
#         }
#         height = newHeight;
#         render();
#     }
#
#     /** Change the Map width */
#     void setWidth(int newWidth) {
#         if (newWidth >= width) {
#             for (ArrayList<Tile> row : tiles) {
#                 for (int w = width; w < newWidth; w += 1) {
#                     row.add(new Tile(this));
#                 }
#             }
#         } else {
#             for (ArrayList<Tile> row : tiles) {
#                 for (int w = width; w > newWidth; w -= 1) {
#                     remove(row.get(w-1));
#                     row.remove(w - 1);
#                 }
#             }
#         }
#         width = newWidth;
#         render();
#     }
#
#     /** Change the number of CPUs to the generated on the Map */
#     void setNumCPUs(int newNumCPUs) {
#         numCPUs = newNumCPUs;
#     }
#
#     /** Change the Map tag */
#     void setTag(String newTag) {
#         tag = newTag;
#     }
#
#     /** Set the Tile where the UserCar will start */
#     void setStartTile(Tile newStartTile) {
#         startTile = newStartTile;
#     }
#
#     /** Set the angle at which the UserCar will start */
#     void setStartAngle(double newStartAngle) {
#         startAngle = newStartAngle;
#     }
#
#     /** Get the Tile at a specific (x, y) pixel coordinate in the Map */
#     private Tile getTile(int x, int y) {
#         int xTile = x / Tile.PIXELS_PER_TILE;
#         int yTile = y / Tile.PIXELS_PER_TILE;
#         return tiles.get(yTile).get(xTile);
#     }
#
#     /** Get friction coeff at a specific (x, y) pixel coordinate in the Map */
#     private double getFriction(int x, int y) {
#         Tile tile = getTile(x, y);
#         int xTile = x % Tile.PIXELS_PER_TILE;
#         int yTile = y % Tile.PIXELS_PER_TILE;
#         return tile.getFriction(xTile, yTile);
#     }
#
#     /** Add listeners to every Tile in the Map */
#     void addListeners() {
#         for (int i = 0; i < height; i += 1) {
#             ArrayList<Tile> row = tiles.get(i);
#             for (int j = 0; j < width; j += 1) {
#                 Tile tile = row.get(j);
#                 tile.addListeners();
#             }
#         }
#     }
#
#     /** Render the Map */
#     void render() {
#         int PPT = Tile.PIXELS_PER_TILE;
#         setPreferredSize(new Dimension(width * PPT, height * PPT));
#         for (int i = 0; i < height; i += 1) {
#             ArrayList<Tile> row = tiles.get(i);
#             for (int j = 0; j < width; j += 1) {
#                 Tile tile = row.get(j);
#                 tile.setBounds(j * PPT, i * PPT, PPT, PPT);
#                 tile.setOpaque(true);
#                 tile.setBorderPainted(false);
#                 add(tile);
#             }
#         }
#     }
#
# }
