import re

def normalize_text(text):
    return text.strip().lower()

def detect_std_tr(text, triggers):
    text = normalize_text(text)

    for word in triggers:
        pattern = rf"(?<!\w){re.escape(word)}(?!\w)"

        matches = list(re.finditer(pattern, text))

        for match in matches:
            before = text[:match.start()].strip()
            after = text[match.end():].strip()

            if not before or not after:
                return word

    return None 

def detect_mid_tr(text, triggers):
    text = normalize_text(text)

    for word in triggers:
        pattern = rf"(?<!\w){re.escape(word)}(?!\w)"

        if re.search(pattern, text):
            return word

    return None

def detect_tr(text, std_triggers, mid_triggers):
    std_match = detect_std_tr(text, std_triggers)
    mid_match = detect_mid_tr(text, mid_triggers)

    if std_match:
        return {
            "type": "std",
            "trigger": std_match
        }
    else:
        return {
            "type": "mid",
            "trigger": mid_match
        }