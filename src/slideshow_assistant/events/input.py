import pyautogui


def previous_slide():
    try:
        pyautogui.press("left")
    except pyautogui.FailSafeException as exception:
        print({exception})
        pass

def next_slide():
    try:
        pyautogui.press("right")
    except pyautogui.FailSafeException as exception:
        print({exception})
        pass

def stop_slide():
    try:
        pyautogui.press("esc")
    except pyautogui.FailSafeException as exception:
        print({exception})
        pass

EVENT_HANDLERS = {
    "previous_slide": previous_slide,
    "next_slide": next_slide,
    "stop_slide": stop_slide,
}