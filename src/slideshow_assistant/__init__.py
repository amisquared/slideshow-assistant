import os
import sys

if "linux" in sys.platform.lower():
    os.environ.setdefault("PYSTRAY_BACKEND", "appindicator") # NEEEDED!!!

import threading

import pystray
from PIL import Image

from .stt import STTWorker

worker = STTWorker()

def draw_icon():
    img = Image.new('RGB', (64, 64), 'black')
    return img

def on_quit(icon):
    worker.stop()
    icon.stop()

def on_restart(icon, item):
    threading.Thread(target=worker.restart, daemon=True).start()

menu = pystray.Menu(
    pystray.MenuItem("Status: Listening", lambda: icon, enabled=False),
    pystray.MenuItem("Restart", on_restart),
    pystray.MenuItem("Quit", on_quit)
)

icon = pystray.Icon("ssast", draw_icon(), "Slideshow Assistant", menu)

def main() -> None:
    worker.start()
    icon.run()

if __name__ == "__main__":
    main()