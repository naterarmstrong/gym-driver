from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

DEFAULT_WIDTH = 5
DEFAULT_HEIGHT = 5
DEFAULT_NUM_CPUS = 0
DEFAULT_TAG = None
DEFAULT_START_ANGLE = None
BACKGROUND_COLOR = None
PIXELS_PER_TILE = 200


root = Tk()


PIXELS_PER_TILE = 200
DEFAULT_TERRAIN = 'grass'
DEFAULT_IMAGE = ImageTk.PhotoImage(Image.open("../resources/{}.png".format(DEFAULT_TERRAIN)))
TEXTURES = None
PATHS = ['straight', 'quarter']







def initialize_for_testing():
	h = ttk.Scrollbar(root, orient=HORIZONTAL)
	v = ttk.Scrollbar(root, orient=VERTICAL)
	canvas = Canvas(root, scrollregion=(0, 0, 1000, 1000), yscrollcommand=v.set, xscrollcommand=h.set)
	h['command'] = canvas.xview
	v['command'] = canvas.yview
	ttk.Sizegrip(root).grid(column=10, row=10, sticky=(S,E))
	canvas.grid(column=0, row=0, sticky=(N,W,E,S))
	h.grid(column=0, row=10, sticky=(W,E))
	v.grid(column=10, row=0, sticky=(N,S))
	root.grid_columnconfigure(0, weight=1)
	root.grid_rowconfigure(0, weight=1)

	Map(canvas)

	root.mainloop()




class ExistingMap:

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
		self.set_canvas(Canvas())
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

	# Setter method: canvas
	def set_canvas(self, canvas):
		self.canvas = canvas

	# Step

	# Reset

	# Render

class Map(ExistingMap):
	def __init__(self, canvas):
		self.canvas = canvas
		self.height = DEFAULT_HEIGHT
		self.width = DEFAULT_WIDTH
		self.tiles = []
		for i in range(self.height):
			row = []
			for j in range(self.width):
				id = canvas.create_image((PIXELS_PER_TILE / 2) + PIXELS_PER_TILE*j, \
					(PIXELS_PER_TILE / 2) + PIXELS_PER_TILE*i, image=DEFAULT_IMAGE)
				row.append([Tile(self), id])
			self.tiles.append(row)

		self.add_listeners()

	def add_listeners(self):
		for i in range(self.get_height()):
			row = self.tiles[i]
			for j in range(self.get_width()):
				tile = row[j][0]
				id = row[j][1]
				tile.add_listeners(id, self.canvas)

class Tile:
	def __init__(self, map):
		self.map = map
		self.texture = 'grass'
		self.orientation = 'N'

	def add_listeners(self, id, canvas):
		self.id = id
		canvas.tag_bind(id, '<Button-1>')




initialize_for_testing()


class ExistingTile(Button):

	# Tile class attributes
	terrain_selection = DEFAULT_TERRAIN
	pressed = False

	# Tile constructors
	def __init__(self, map, texture=DEFAULT_TERRAIN, path_ind=0, orientation=0):
		Button.__init__(self) # TODO: args to Button.__init__ ? perhaps don't subclass Button?
		self.set_map(map)
		self.set_texture(texture)
		self.set_path_ind(path_ind)
		self.set_orientation(orientation)
		# TODO: setBackground(getColor(texture));
		self.add_listeners()

	# Populate the Tile with listeners to allow user interfacing
	def add_listeners(self):
		self.bind("<Enter>", self.on_enter)
		self.bind("<Button-1>", self.on_leftclick)
		self.bind("<Button-2>", self.on_rightclick)
		self.bind("<Key>", self.on_keypress)

	def on_enter(self, event):
		# TODO: requestFocus()
		if Tile.pressed:
			self.set_texture(Tile.terrain_selection)

	def on_leftclick(self, event):
		Tile.pressed = True
		self.set_texture(Tile.terrain_selection)

	def on_rightclick(self, event):
		self.cycle_path()

	def on_keypress(self, event):
		char = event.char
		if char == "r":
			self.cycle_orientation()
		elif char == "w":
			self.map.set_start_angle(90)
		elif char == "a":
			self.map.set_start_angle(180)
		elif char == "s":
			self.map.set_start_angle(270)
		elif char == "d":
			self.map.set_start_angle(0)
		# TODO: self.repaint()

	# Getter method: texture
	def get_texture(self):
		return self.texture

	# Getter method: texture [given (x, y) coordinate]
	def get_point_texture(self, x, y):
		path = self.get_path()
		if path == "flat":
			return self.get_texture()
		else:
			orientation = self.get_orientation()
			if orientation == 0:
				in_circle = self.in_circle(x, y - PIXELS_PER_TILE)
			elif orientation == 90:
				in_circle = self.in_circle(x - PIXELS_PER_TILE, y - PIXELS_PER_TILE)
			elif orientation == 180:
				in_circle = self.in_circle(x - PIXELS_PER_TILE, y)
			elif orientation == 270:
				in_circle = self.in_circle(x, y)
			else:
				raise Exception("Unsupported orientation")
			if path == "convex":
				return self.get_texture() if in_circle else DEFAULT_TERRAIN
			elif path == "concave":
				return DEFAULT_TERRAIN if in_circle else self.get_texture()
			else:
				raise Exception("Unsupported path type")

	@staticmethod
	def in_circle(x, y):
		return x * x + y * y <= PIXELS_PER_TILE * PIXELS_PER_TILE

	# Getter method: path
	def get_path(self):
		return PATHS[self.path_ind]

	# Getter method: orientation
	def get_orientation(self):
		return self.orientation

	# Getter method: friction [provided texture]
	@staticmethod
	def get_texture_friction(texture):
		return TEXTURES[texture][0]

	# Getter method: friction [provided (x, y) coordinate]
	def get_point_friction(self, x, y):
		texture = self.get_point_texture(x, y)
		return Tile.get_texture_friction(texture)

	# Setter method: map
	def set_map(self, map):
		self.map = map

	# Setter method: texture
	def set_texture(self, texture):
		if texture in TEXTURES:
			self.texture = texture
			# TODO: setBackground(getColor(texture))
			if self.get_texture() == DEFAULT_TERRAIN:
				self.set_path_ind(0)

	# Setter method: path_ind
	def set_path_ind(self, path_ind):
		self.path_ind = path_ind

	# Setter method: orientation
	def set_orientation(self, orientation):
		self.orientation = orientation

	# Cycle to the next path type
	def cycle_path(self):
		if self.get_texture() != DEFAULT_TERRAIN:
			self.set_path_ind((self.path_ind + 1) % len(PATHS))
			# TODO: paint(getGraphics());

	# Cycle to the next orientation
	def cycle_orientation(self):
		path = self.get_path()
		if path == "convex" or path == "concave":
			self.set_orientation((self.orientation + 90) % 360)

	# TODO
	#     /** Draw the Tile */
	#     @Override
	#     public void paint(Graphics g) {
	#         super.paintComponent(g);
	#         for (int i = 0; i < PIXELS_PER_TILE; i += 1) {
	#             for (int j = 0; j < PIXELS_PER_TILE; j += 1) {
	#                 String texture = getPtTextureInd(i, j);
	#                 Color color = getColor(texture);
	#                 g.setColor(color);
	#                 g.fillRect(i, j, 1, 1);
	#             }
	#         }
	#         if (this == map.getStartTile()) {
	#             int x = PIXELS_PER_TILE / 2;
	#             int y = PIXELS_PER_TILE / 2;
	#             g.setColor(Color.ORANGE);
	#             switch (map.getStartAngle()) {
	#                 case 0:
	#                     g.drawString("\u25BA", x, y);
	#                     break;
	#                 case 90:
	#                     g.drawString("\u25B2", x, y);
	#                     break;
	#                 case 180:
	#                     g.drawString("\u25C4", x, y);
	#                     break;
	#                 case 270:
	#                     g.drawString("\u25BC", x, y);
	#                     break;
	#             }
	#         }
	#     }
	#
	# }

