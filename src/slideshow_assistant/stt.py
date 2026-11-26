import threading

from RealtimeSTT import AudioToTextRecorder

from .detection import detect_tr
from .dict import load_dict, normalize_words
from .events.handler import exec_event


class STTWorker:
    def __init__(self):
        self._thread: threading.Thread | None = None
        self._stop_event = threading.Event()
        self._recorder: AudioToTextRecorder | None = None

    def start(self):
        if self._thread and self._thread.is_alive():
            return
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._run, daemon=True)
        self._thread.start()

    def stop(self, wait=True):
        self._stop_event.set()
        if self._recorder:
            try: 
                self._recorder.shutdown()
            except Exception:
                pass
        if wait and self._thread:
            self._thread.join(timeout=3)

    def _run(self):
        triggers = load_dict()
        std = normalize_words(triggers.get("std", {}))
        mid = normalize_words(triggers.get("mid", {}))

        self._recorder = AudioToTextRecorder() # type: ignore
        try:
            while not self._stop_event.is_set():
                self._recorder.text(lambda t: self._handle_text(t, std, mid)) # type: ignore
        except Exception as exception:
            if not self._stop_event.is_set():
                print(f"STT {exception}")
        finally:
            if self._recorder is not None:
                try:
                    self._recorder.shutdown()
                except Exception:
                    pass
            self._recorder = None

    def _handle_text(self, text, std, mid):
        if self._stop_event.is_set():
            return
        print(text)
        result = detect_tr(text, std, mid)
        if result:
            print(f"{result['phrase']} -> {result['event']}")
            exec_event(result['event'])

    def restart(self):
        self.stop()
        from .events.handler import load_events
        load_events(refresh=True)
        self.start()