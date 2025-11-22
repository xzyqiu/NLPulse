import subprocess
import argparse
from analyzer.text_analysis import analyze_text
from analyzer.speech_analysis import speech_to_text

def run_streamlit():
    subprocess.run("streamlit run gui/interface.py", shell=True)

def run_text_analysis(text):
    #Analyze text
    result = analyze_text(text)
    print("Sentiment:", result['sentiment'])
    print("Word Count:", result['word_count'])
    print("Keywords:", result['key_words'])

def run_audio_analysis(file_path):
    #Analyze audio
    text = speech_to_text(file_path)
    print("Transcribed Text:", text)
    run_text_analysis(text)

if __name__ == "__main__":
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
