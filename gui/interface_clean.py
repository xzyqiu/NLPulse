import streamlit as st
import tempfile

from analyzer._text import analyze_text
from analyzer._speech import speech_to_text


st.title("Text & Sentiment Analyzer — NLPulse (Demo)")

user_input = st.text_area("Enter your text here:")

audio_file = st.file_uploader("Or upload an audio file:", type=["wav", "mp3", "m4a", "flac"])

if st.button("Analyze"):
    if user_input and user_input.strip() != "":
        result = analyze_text(user_input)
        st.write("Sentiment:", result["sentiment"])
        st.write("Word Count:", result["word_count"])
        st.write("Keywords:", result["key_words"])
    elif audio_file is not None:
        with tempfile.NamedTemporaryFile(suffix="." + audio_file.type.split("/")[-1], delete=False) as tmp:
            tmp_path = tmp.name
            tmp.write(audio_file.getbuffer())

        try:
            text = speech_to_text(tmp_path)
            result = analyze_text(text)
            st.write("Transcribed Text:", text)
            st.write("Sentiment:", result["sentiment"])
            st.write("Word Count:", result["word_count"])
            st.write("Keywords:", result["key_words"])
        finally:
            try:
                import os

                os.remove(tmp_path)
            except Exception:
                pass
    else:
        st.write("Please enter text or upload an audio file for analysis.")
