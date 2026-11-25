import pyautogui


def previous_slide():
    pyautogui.press("left")

def next_slide():
    pyautogui.press("right")

def stop_slide():
    pyautogui.press("esc")

EVENT_HANDLERS = {
    "previous_slide": previous_slide,
    "next_slide": next_slide,
    "stop_slide": stop_slide,
}