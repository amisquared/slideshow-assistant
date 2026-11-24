import configparser
from pathlib import Path

from RealtimeSTT import AudioToTextRecorder

# Handle config
config = configparser.ConfigParser()

## config file
CONFIG_FILE = Path.home() / "ssast.cfg"
if CONFIG_FILE.exists():
    config.read(CONFIG_FILE)
else:
    config.setdefault("SETTINGS", {})
    config["SETTINGS"].setdefault(
        "trigger_dictionary",
        str(Path.home() / "dict.txt")
    )

    with open(CONFIG_FILE, "w") as file:
        config.write(file)

# dict
DICT_FILE = Path(config["SETTINGS"]["trigger_dictionary"])
## check
if not DICT_FILE.exists():
    DICT_FILE.touch(exist_ok=True)
## open dict
with open(DICT_FILE, "r") as file:
    trigger_words = [line.strip().lower() for line in file if line.strip()]

print(trigger_words)