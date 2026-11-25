from RealtimeSTT import AudioToTextRecorder
from .detection import detect_tr
from .dict import trigger_words_std, trigger_words_mid
from .events.handler import exec_event

def handle_text(text: str):
    result = detect_tr(text, trigger_words_std, trigger_words_mid)
    if result:
        print(f"{result['phrase']} -> {result['event']}")
        exec_event(result['event'])

def run():
    with AudioToTextRecorder() as recorder:
        while True:
            recorder.text(handle_text)