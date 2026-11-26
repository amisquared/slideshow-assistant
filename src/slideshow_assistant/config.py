import configparser
from pathlib import Path

CONFIG_FILE = Path.home() / "ssast.cfg"

def load_config():
    config = configparser.ConfigParser()

    if CONFIG_FILE.exists():
        config.read(CONFIG_FILE)
    else:
        config.setdefault("SETTINGS", {})
        config["SETTINGS"].setdefault(
            "trigger_dictionary",
            str(Path.home() / "dict.json")
        )
        config["SETTINGS"].setdefault(
            "event_dictionary",
            str(Path.home() / "ssast_events.json")
        )

        with open(CONFIG_FILE, "w") as file:
            config.write(file)

    return config

config = load_config()
DICT_FILE = Path(config["SETTINGS"]["trigger_dictionary"])
EVENT_FILE = Path(config["SETTINGS"]["event_dictionary"])