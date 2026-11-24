import configparser
import json
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
        str(Path.home() / "dict.json")
    )

    with open(CONFIG_FILE, "w") as file:
        config.write(file)

# dict
DICT_FILE = Path(config["SETTINGS"]["trigger_dictionary"])
## check
if not DICT_FILE.exists():
    DICT_FILE.write_text(
        json.dumps({"trigger_words": {"std": [], "mid": []}}, indent=4)
    )

## open dict
with open(DICT_FILE, "r") as file:
    data = json.load(file)

# trigger words
trigger_words = data.get("trigger_words", {})
trigger_words_std = [
    word.strip().lower()
    for word in trigger_words.get("std", [])
    if word.strip()
]
trigger_words_mid = [
    word.strip().lower()
    for word in trigger_words.get("mid", [])
    if word.strip()
]