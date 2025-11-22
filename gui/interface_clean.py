import streamlit as st
import tempfile
import os
import sys

# Ensure project root is on sys.path so `analyzer` package can be imported when
# Streamlit runs this file from the `gui/` directory.
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from analyzer._text import analyze_text
from analyzer._speech import speech_to_text


def get_sentiment_summary(polarity: float) -> str:
    """Generate a human-readable sentiment summary based on polarity score."""
    if polarity > 0.3:
        return "✅ This text is **positive**"
    elif polarity > 0.05:
        return "🙂 This text is **slightly positive**"
    elif polarity > -0.05:
        return "😐 This text is **neutral**"
    elif polarity > -0.3:
        return "🙁 This text is **slightly negative**"
    else:
        return "❌ This text is **negative**"


st.title("Text & Sentiment Analyzer — NLPulse (Demo)")

user_input = st.text_area("Enter your text here:")

audio_file = st.file_uploader("Or upload an audio file:", type=["wav", "mp3", "m4a", "flac"])

if st.button("Analyze"):
    if user_input and user_input.strip() != "":
        with st.spinner("Analyzing text..."):
            result = analyze_text(user_input)
        
        # Display sentiment summary
        polarity = result["sentiment"]["polarity"]
        sentiment_summary = get_sentiment_summary(polarity)
        st.markdown(f"### {sentiment_summary}")
        
        st.write("**Detailed Sentiment:**", result["sentiment"])
        st.write("**Word Count:**", result["word_count"])
        st.write("**Keywords:**", result["key_words"])
    elif audio_file is not None:
        with tempfile.NamedTemporaryFile(suffix="." + audio_file.type.split("/")[-1], delete=False) as tmp:
            tmp_path = tmp.name
            tmp.write(audio_file.getbuffer())

        try:
            with st.spinner("Transcribing audio..."):
                text = speech_to_text(tmp_path)
            
            with st.spinner("Analyzing transcribed text..."):
                result = analyze_text(text)
            
            st.write("**Transcribed Text:**", text)
            
            # Display sentiment summary
            polarity = result["sentiment"]["polarity"]
            sentiment_summary = get_sentiment_summary(polarity)
            st.markdown(f"### {sentiment_summary}")
            
            st.write("**Detailed Sentiment:**", result["sentiment"])
            st.write("**Word Count:**", result["word_count"])
            st.write("**Keywords:**", result["key_words"])
        finally:
            try:
                import os

                os.remove(tmp_path)
            except Exception:
                pass
    else:
        st.write("Please enter text or upload an audio file for analysis.")
