from Tkinter import Canvas

from Tile import Tile

from read_config import read_config

configs = read_config()
PIXELS_PER_TILE = configs["PIXELS_PER_TILE"]
DEFAULT_MAP_W = configs["DEFAULT_MAP_W"]
DEFAULT_MAP_H = configs["DEFAULT_MAP_H"]
DEFAULT_NUM_CPUS = configs["DEFAULT_NUM_CPUS"]
DEFAULT_TAG = configs["DEFAULT_TAG"]
START_ANGLE = configs["START_ANGLE"]
BACKGROUND_COLOR = configs["BACKGROUND_COLOR"]

# Map class
class Map:

    # Map constructor
    def __init__(self, width=DEFAULT_MAP_W, height=DEFAULT_MAP_H):
        self.set_canvas(Canvas())
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
        self.set_cars([])

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

    # Getter method: cars
    def get_cars(self):
        return self.cars

    # Getter method: canvas
    def get_canvas(self):
        return self.canvas

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

    # Setter method: cars
    def set_cars(self, cars):
        self.cars = cars

    # Setter method: canvas
    def set_canvas(self, canvas):
        self.canvas = canvas

    # Step the Map forward
    def step(self, action):
        for car in self.get_cars():
            car.step(car_heuristic())

    # Render the Map
    def render(self, coordinates):
        None

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

    # Step

    # Reset

    # Render

    # TODO: putting cars on map, step, reset, render
