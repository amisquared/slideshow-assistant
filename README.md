# Slideshow Assistant

> Just say the magic word, and I'll switch it. Alright?

STT app running during a presentation that lets you say trigger words for the next slide.

## Requirements

- Python 3.14
- [uv](https://docs.astral.sh/uv/)
- A microphone
- `libayatana-appindicator-gtk3` and `python3-gobject`

## Usage

To use slideshow-assistant:

1. Clone the repo
```bash
$ git clone https://github.com/amisquared/slideshow-assistant
```
2. Install dependencies via uv
```bash
$ uv sync
```

3. Configure your trigger words.
The project repo has [a premade dictionary](dict.json), which you can base off.
Standard (`std`) triggers are triggered only when:
- it is at the start of a sentence; or
- it is at the end of a sentence.

Middle (`mid`) triggers are triggered mid-sentence, after transcribing.

4. Configure your events.
Events are the matching action with every trigger word in your dictionary. The project repo has [premade entries](ssast_event.json), which you can also base off.


slideshow-assistant uses [pyautogui](https://pyautogui.readthedocs.io/en/latest/), so it should be the same behavior. Only supported events are `press` and `hotkey`.

5. Point your files

On launch, there should be a config file at `~/ssast.cfg`. This is where you configure your dictionary files for both events and triggers.
```cfg
[SETTINGS]
trigger_dictionary = /path/to/dict.json
event_dictionary = /path/to/ssast_events.json
```

6. Run

With uv:
```bash
uv run slideshow-assistant
```

There should be a tray icon, where you can restart, for when you change the config or something else.

## Limitations
### Speech to Text (STT)
Since this is STT, where computers are the ones figuring out your speech, there are quite a number of limitations.

This list is not exhaustive, but:
- Non-english speech is likely not supported (faster-whisper, may work with other engines;)
- Accents are poorly recognized (general issue with STT in general;)
- Speed

### Platforms
This has been written for Linux in mind, but cross-platform support *should be* there, just untested.
#### Wayland
Target windows need to be ran under XWayland, as pyautogui doesn't support Wayland.

## AI Usage

AI was used during development. Commits have been marked with an `Assisted-by:` tag to disclose if AI was ever used. 

This project isn't pure AI slop :3c

## Brief thanks to...

the unlisted people giving me voice samples to test! <3

## Licensing
slideshow-assistant is licensed under the GNU General Public License v3. See [LICENSE.](LICENSE)