import subprocess
import argparse
from analyzer._text import analyze_text
from analyzer._speech import speech_to_text


def run_streamlit() -> None:
    """Launch the Streamlit demo UI."""

    subprocess.run("streamlit run gui/interface_clean.py", shell=True)


def run_text_analysis(text: str) -> None:
    """Run text analysis and print results to stdout."""

    result = analyze_text(text)
    sentiment = result.get("sentiment", {})
    print("Sentiment:", sentiment)
    print("Word Count:", result.get("word_count"))
    print("Keywords:", result.get("key_words"))


def run_audio_analysis(file_path: str) -> None:
    """Run audio-to-text followed by text analysis."""

    text = speech_to_text(file_path)
    print("Transcribed Text:", text)
    run_text_analysis(text)


def main() -> int:
    parser = argparse.ArgumentParser(description="NLPulse: Text & Speech Analyzer")
    parser.add_argument("--text", type=str, help="Analyze the provided text")
    parser.add_argument("--audio", type=str, help="Analyze the provided audio file (WAV/MP3/FLAC)")
    parser.add_argument("--gui", action="store_true", help="Launch the Streamlit interface")

    args = parser.parse_args()

    if args.gui:
        run_streamlit()
    elif args.text:
        run_text_analysis(args.text)
    elif args.audio:
        run_audio_analysis(args.audio)
    else:
        print("No input provided. Use --gui to launch Streamlit, --text to analyze text, or --audio to analyze audio.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
