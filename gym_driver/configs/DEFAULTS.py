import json

# Menu
WINDOW_W = 1000
WINDOW_H = 600
PANEL_W = 200
PANEL_H = WINDOW_H
PANE_W = WINDOW_W - PANEL_W
PANE_H= WINDOW_H
SAVE_DIR = "../maps/"
SAVE_EXT = ".pkl"

# Panel
LABEL_W = 50
LABEL_H = 30

# Map
DEFAULT_NUM_CPUS = 4
DEFAULT_TAG = "New Map"
DEFAULT_START_ANGLE = 0
BACKGROUND_COLOR = "#4286f4"

# Tile
PIXELS_PER_TILE = 200
DEFAULT_TERRAIN = "grass"
TEXTURES = {
    "grass": [0.5, "#419141"],
    "gravel": [0.9, "#917441"],
    "road": [0.5, "#565148"],
    "ice": [0.1, "#bdefef"]
}
PATHS = ["straight", "convex", "concave"]

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

    # Panel
    "LABEL_W": LABEL_W,
    "LABEL_H": LABEL_H,

    # Map
    "DEFAULT_NUM_CPUS": DEFAULT_NUM_CPUS,
    "DEFAULT_TAG": DEFAULT_TAG,
    "DEFAULT_START_ANGLE": DEFAULT_START_ANGLE,
    "BACKGROUND_COLOR": BACKGROUND_COLOR,

    # Tile
    "PIXELS_PER_TILE": PIXELS_PER_TILE,
    "DEFAULT_TERRAIN": DEFAULT_TERRAIN,
    "TEXTURES": TEXTURES,
    "PATHS": PATHS

}

with open("DEFAULTS.json", "wb") as f:
    json.dump(configs, f, indent=4)
