import json

from .config import DICT_FILE


def load_dict():
    if not DICT_FILE.exists():
        DICT_FILE.write_text(
            json.dumps(
                {"trigger_words": {"std": {}, "mid": {}}}, 
                indent=4
            ),
            encoding="utf8"
        )

    ## open dict
    with open(DICT_FILE, "r", encoding="utf8") as file:
        data = json.load(file)

    return data.get("trigger_words", {})

def normalize_words(words: dict) -> dict[str, str]:
    return {
        word.strip().lower(): event
        for word, event in words.items()
        if isinstance(word, str) and word.strip()
    }

# trigger words
trigger_words = load_dict()
trigger_words_std = normalize_words(
    trigger_words.get("std", {})
)
trigger_words_mid = normalize_words(
    trigger_words.get("mid", {})
)