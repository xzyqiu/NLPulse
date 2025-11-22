import streamlit as st
from analyzer.text_analysis import analyze_text
from analyzer.speech_analysis import speech_to_text

st.title("Text & Sentiment Analyzer")

user_input = st.text_area("Enter your text here: ")

audio_file = st.file_uploader("Or upload an audio file:", type=["wav", "mp3", "m4a", "flac"])

if st.button("Analyze"):
    if user_input.strip() != "":
        result = analyze_text(user_input)
        st.write("Sentiment: ", result['sentiment'])
        st.write("Word Count: ", result['word_count'])
        st.write("Keywords:", result['key_words'])
    elif audio_file is not None:
        with open("temp_audio", "wb") as f:
            f.write(audio_file.getbuffer())
        
        text = speech_to_text("temp_audio")
        result = analyze_text(text)
        st.write("Transcribed Text:", text)
        st.write("Sentiment: ", result['sentiment'])
        st.write("Word Count: ", result['word_count'])
        st.write("Keywords:", result['key_words'])
    else:
        st.write("Please enter text or upload an audio file for analysis.")