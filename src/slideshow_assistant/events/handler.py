import json
from pathlib import Path

import pyautogui

from .input import EVENT_HANDLERS as DEFAULT_EVENT_HANDLERS

EVENT_DEF_FILE = (Path.home() / "sasst_events.json")
_event_cache: dict | None = None

def load_events(refresh: bool = False):
    global _event_cache
    if _event_cache is not None and not refresh:
        return _event_cache
    if not EVENT_DEF_FILE.exists():
        _event_cache = {}
    else:
        with open(EVENT_DEF_FILE, "r", encoding="utf-8") as file:
            _event_cache = json.load(file).get("events", {})
    return _event_cache

def exec_custom_event(event):
    action = event.get("action")

    try:
        if action == "press":
            pyautogui.press(event["key"])
        elif action == "hotkey":
            pyautogui.hotkey(*event["keys"])
        else:
            print(f"unknown event {event}")
            return False
    except (KeyError, pyautogui.FailSafeException) as exception:
        print(f"event {event} failed due to {exception}")
        return False
    return True

def exec_event(event):
    handler = DEFAULT_EVENT_HANDLERS.get(event)

    if handler:
        handler()
        return True
    
    custom_events = load_events()
    custom_event = custom_events.get(event)

    if custom_event:
        return exec_custom_event(custom_event)

    print(f"Unknown event {event!r}")
    return False