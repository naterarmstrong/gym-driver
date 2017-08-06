import json

def read_config():
    # Extract the active config filepath from active.txt
    active_txt = open("../configs/active.txt")
    active_config_name = active_txt.read()
    active_txt.close()
    # Load the configs dictionary from the active config file
    active_config_path = "../configs/" + active_config_name
    active_config_file = open(active_config_path, "r")
    active_config_dict = json.load(active_config_file)
    active_config_file.close()
    return active_config_dict
