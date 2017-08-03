import json

configs = {

    # Menu & Panel
    "WINDOW_WIDTH": 1000,
    "WINDOW_HEIGHT": 600,
    "PANE_WIDTH": 400,
    "PANE_HEIGHT": 600,
    "PANEL_WIDTH": 200,
    "PANEL_HEIGHT": 600,
    "SAVE_DIR": "../maps/",
    "SAVE_EXT": ".ser",

    # Map
    "DEFAULT_NUM_CPUS": 4,
    "DEFAULT_TAG": "New Map",
    "DEFAULT_START_ANGLE": 0,
    "BACKGROUND_COLOR": "#4286f4",

    # Tile
    "PIXELS_PER_TILE": 200,
    "DEFAULT_TERRAIN": "grass",
    "TEXTURES": {
        "grass": [0.5, "#419141"],
        "gravel": [0.9, "#917441"],
        "road": [0.5, "#565148"],
        "ice": [0.1, "#bdefef"]
    },
    "PATHS": ["straight", "convex", "concave"]

}

with open("DEFAULTS.json", "w") as f:
    json.dump(configs, f, indent=4)
