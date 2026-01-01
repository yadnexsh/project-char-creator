import os
import json

config_dir = os.path.dirname(__file__)

def load_config_data():
    try:
        with open(os.path.join(config_dir, "gears.json"), "r") as file:
            GEARS = json.load(file)

        with open(os.path.join(config_dir, "names.json"), "r") as file:
            NAMES = json.load(file)

        return GEARS, NAMES, True   
    
    except json.decoder.JSONDecodeError as e:
        print(f"JSON error: {e}")
    except Exception as e:
        print(f"Error: {e}")

    return None, None, False


if __name__ == "__main__":
    GEARS, NAMES, loaded = load_config_data()
    print("Files loaded:", loaded)
