'''Robust Config Reader
You'll practice
Layered error handling with fallbacks
Write a function that reads a JSON config file and ALWAYS returns a usable config, handling every failure with sensible defaults:
• file not found  -> create it with the defaults
• invalid JSON    -> warn, then use the defaults
• missing keys    -> fill them in from the defaults
• wrong types (e.g. a string where a number is expected) -> replace with the default
'''





import json

DEFAULT_CONFIG = {
    "app_name": "MyApp",
    "retry_count": 3,
    "timeout": 30,
    "debug": False
}


def read_config(filename):
    try:
        with open(filename, "r") as file:
            config = json.load(file)

    except FileNotFoundError:
        print("Config file not found. Creating default config.")

        with open(filename, "w") as file:
            json.dump(DEFAULT_CONFIG, file, indent=4)

        return DEFAULT_CONFIG.copy()

    except json.JSONDecodeError:
        print("Invalid JSON. Using default config.")
        return DEFAULT_CONFIG.copy()

    except OSError:
        print("Could not read the file. Using defaults.")
        return DEFAULT_CONFIG.copy()
    
    if not isinstance(config, dict):
        print("Invalid config format. Using defaults.")
        return DEFAULT_CONFIG.copy()

    for key, default_value in DEFAULT_CONFIG.items():

        if key not in config:
            print(f"Missing key '{key}'. Using default.")
            config[key] = default_value

        elif type(config[key]) != type(default_value):
            print(f"Wrong type for '{key}'. Using default.")
            config[key] = default_value

    return config

config = read_config("config.json")
print(config)
