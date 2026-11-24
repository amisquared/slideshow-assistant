import re


def normalize_text(text: str):
    return text.strip().lower()

def detect_std_tr(text: str, triggers: dict[str, str]):
    text = normalize_text(text)

    for word, event in triggers.items():
        pattern = rf"(?<!\w){re.escape(word)}(?!\w)"

        matches = re.finditer(pattern, text)

        for match in matches:
            before = text[:match.start()].strip()
            after = text[match.end():].strip()

            if not before or not after:
                return {
                    "phrase": word,
                    "event": event,
                    "type": "std"
                }

    return None 

def detect_mid_tr(text: str, triggers: dict[str, str]):
    text = normalize_text(text)

    for word, event in triggers.items():
        pattern = rf"(?<!\w){re.escape(word)}(?!\w)"

        if re.search(pattern, text):
            return {
                "phrase": word,
                "event": event,
                "type": "mid"
            }

    return None

def detect_tr(text, std_triggers, mid_triggers):
    result = detect_std_tr(text, std_triggers)

    if result:
        return result

    result = detect_mid_tr(text, mid_triggers)

    if result:
        return result

    return None