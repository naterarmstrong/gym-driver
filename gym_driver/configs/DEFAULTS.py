from json import dump

# Menu
WINDOW_W = 1000
WINDOW_H = 600
PANEL_W = 200
PANEL_H = WINDOW_H
PANE_W = WINDOW_W - PANEL_W
PANE_H= WINDOW_H
SAVE_DIR = "../maps/"
SAVE_EXT = ".json"
RESOURCE_DIR = "../resources/"

# Panel
LABEL_W = 60
LABEL_H = 25
MARGIN = 2
ELEMENT_H = LABEL_H
BACK_Y = PANEL_H - ELEMENT_H
SECTION_BREAK = ELEMENT_H

# MainPanel
MAP_LABEL_Y = 0
EDIT_MAP_Y = MAP_LABEL_Y + ELEMENT_H
RUN_MAP_Y = EDIT_MAP_Y + ELEMENT_H
CYCLE_MAP_Y = RUN_MAP_Y + ELEMENT_H
NEW_MAP_Y = CYCLE_MAP_Y + ELEMENT_H
SELECT_MAP_Y = NEW_MAP_Y + ELEMENT_H

# MakerPanel
SET_WIDTH_Y = 0
SET_HEIGHT_Y = SET_WIDTH_Y + ELEMENT_H
UPDATE_SIZE_W = 70
SET_TERRAIN_H = 2 * ELEMENT_H
SET_TERRAIN_Y = SET_HEIGHT_Y + SECTION_BREAK
NUM_CPUS_Y = SET_HEIGHT_Y + 2 * SET_TERRAIN_H + SECTION_BREAK
SAVE_Y = BACK_Y - ELEMENT_H
NAME_Y = SAVE_Y - ELEMENT_H

# RunnerPanel

# Tile
PIXELS_PER_TILE = 200
DEFAULT_TERRAIN = "grass"
TEXTURES = {
    "grass": [0.5, "#419141"],
    "gravel": [0.9, "#917441"],
    "road": [0.5, "#565148"],
    "ice": [0.1, "#bdefef"]
}
PATHS = ["straight", "quarter_turn"]
ORIENTATIONS = [0, 90, 180, 270]

# Map
DEFAULT_MAP_W = PANE_W // PIXELS_PER_TILE + 1
DEFAULT_MAP_H = PANE_H // PIXELS_PER_TILE + 1
DEFAULT_NUM_CPUS = 4
DEFAULT_TAG = "New Map"
START_ANGLE = 0
BACKGROUND_COLOR = "#4286f4"

configs = {

    # Menu
    "WINDOW_W": WINDOW_W,
    "WINDOW_H": WINDOW_H,
    "PANEL_W": PANEL_W,
    "PANEL_H": PANEL_H,
    "PANE_W": PANE_W,
    "PANE_H": PANE_H,
    "SAVE_DIR": SAVE_DIR,
    "SAVE_EXT": SAVE_EXT,
    "RESOURCE_DIR": RESOURCE_DIR,

    # Panel
    "LABEL_W": LABEL_W,
    "LABEL_H": LABEL_H,
    "MARGIN": MARGIN,
    "ELEMENT_H": ELEMENT_H,
    "BACK_Y": BACK_Y,

    # MainPanel
    "MAP_LABEL_Y": MAP_LABEL_Y,
    "EDIT_MAP_Y": EDIT_MAP_Y,
    "RUN_MAP_Y": RUN_MAP_Y,
    "CYCLE_MAP_Y": CYCLE_MAP_Y,
    "NEW_MAP_Y": NEW_MAP_Y,
    "SELECT_MAP_Y": SELECT_MAP_Y,

    # MakerPanel
    "SET_WIDTH_Y": SET_WIDTH_Y,
    "SET_HEIGHT_Y": SET_HEIGHT_Y,
    "UPDATE_SIZE_W": UPDATE_SIZE_W,
    "SET_TERRAIN_H": SET_TERRAIN_H,
    "SET_TERRAIN_Y": SET_TERRAIN_H,
    "NUM_CPUS_Y": NUM_CPUS_Y,
    "SAVE_Y": SAVE_Y,
    "NAME_Y": NAME_Y,

    # RunnerPanel

    # Tile
    "PIXELS_PER_TILE": PIXELS_PER_TILE,
    "DEFAULT_TERRAIN": DEFAULT_TERRAIN,
    "TEXTURES": TEXTURES,
    "PATHS": PATHS,
    "ORIENTATIONS": ORIENTATIONS,

    # Map
    "DEFAULT_MAP_W": DEFAULT_MAP_W,
    "DEFAULT_MAP_H": DEFAULT_MAP_H,
    "DEFAULT_NUM_CPUS": DEFAULT_NUM_CPUS,
    "DEFAULT_TAG": DEFAULT_TAG,
    "START_ANGLE": START_ANGLE,
    "BACKGROUND_COLOR": BACKGROUND_COLOR

}

with open("DEFAULTS.json", "wb") as f:
    dump(configs, f, indent=4)
