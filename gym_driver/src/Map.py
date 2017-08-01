from Tile import Tile

from read_config import read_config

configs = read_config()
DEFAULT_WIDTH = configs["DEFAULT_WIDTH"]
DEFAULT_HEIGHT = configs["DEFAULT_HEIGHT"]
DEFAULT_NUM_CPUS = configs["DEFAULT_NUM_CPUS"]
DEFAULT_TAG = configs["DEFAULT_TAG"]
DEFAULT_START_ANGLE = configs["DEFAULT_START_ANGLE"]
BACKGROUND_COLOR = configs["BACKGROUND_COLOR"]
PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]

# Map class
class Map:

    # Map constructor
    def __init__(self, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.width = width
        self.height = height
        self.tiles = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(Tile(self))
            self.tiles.append(row)
        self.set_num_CPUs(DEFAULT_NUM_CPUS)
        self.set_tag(DEFAULT_TAG)
        if self.tiles and self.tiles[0]:
            self.set_start_tile(self.tiles[0][0])
        else:
            self.set_start_tile(None)
        self.set_start_angle(DEFAULT_START_ANGLE)
        # TODO: setBackground(BACKGROUND_COLOR)
        # TODO: setLayout(null)
        # TODO: render()

    # Add listeners to every Tile on the Map
    def add_listeners(self):
        for i in range(self.get_height()):
            row = self.tiles[i]
            for j in range(self.get_width()):
                tile = row[j]
                tile.add_listeners()

    # Getter method: width
    def get_width(self):
        return self.width

    # Getter method: height
    def get_height(self):
        return self.height

    # Getter method: num_CPUs
    def get_num_CPUs(self):
        return self.num_CPUs

    # Getter method: tag
    def get_tag(self):
        return self.tag

    # Getter method: start_tile
    def get_start_tile(self):
        return self.start_tile

    # Getter method: start_angle
    def get_start_angle(self):
        return self.start_angle

    # Getter method: Tile [provided (x, y) coordinate]
    def get_tile(self, x, y):
        x_tile = x // PIXELS_PER_TILE
        y_tile = y // PIXELS_PER_TILE
        return self.tiles[x_tile][y_tile]

    # Getter method: friction [provided (x, y) coordinate]
    def get_point_friction(self, x, y):
        x_pixel = x % PIXELS_PER_TILE
        y_pixel = y % PIXELS_PER_TILE
        return self.get_tile(x, y).get_point_friction(x_pixel, y_pixel)

    # Setter method: width
    def set_width(self, width):
        if width >= self.width:
            for row in self.tiles:
                for _ in range(width - self.width):
                    row.append(Tile(self))
        else:
            for row in self.tiles:
                for _ in range(self.width - width):
                    row.pop()
        self.width = width
        # TODO: render()

    # Setter method: height
    def set_height(self, height):
        if height >= self.height:
            for _ in range(height - self.height):
                row = [Tile(self) for _ in range(self.width)]
                self.tiles.append(row)
        else:
            for _ in range(self.height - height):
                self.tiles.pop()
        self.height = height
        # TODO: render()

    # Setter method: num_CPUs
    def set_num_CPUs(self, num_CPUs):
        self.num_CPUs = num_CPUs

    # Setter method: tag
    def set_tag(self, tag):
        self.tag = tag

    # Setter method: start_tile
    def set_start_tile(self, start_tile):
        self.start_tile = start_tile

    # Setter method: start_angle
    def set_start_angle(self, start_angle):
        self.start_angle = start_angle

    # TODO
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
