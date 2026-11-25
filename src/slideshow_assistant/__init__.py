from slideshow_assistant.stt import run as stt_run

def main() -> None:
    stt_run()

if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt):
        print("\nStopped")