# NLPulse

NLPulse is a cutting-edge web application that combines **text and speech analysis** in a seamless, user-friendly interface. Powered by Python, TextBlob, and SpeechRecognition, NLPulse allows users to analyze sentiments, extract keywords, and convert speech to text, providing insights from both written and spoken content.

---

## Features

- **Text Analysis**: Analyze any text for sentiment (polarity & subjectivity), word count, and key phrases / keywords.
- **Speech-to-Text Analysis**: Convert audio files (WAV, MP3, FLAC) to text and analyze them. Automatic conversion to WAV for optimized analysis.
- **Streamlit Web Interface**: Interactive and minimal design. Upload text or audio for instant analysis and display results clearly.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/xzyqiu/NLPulse.git
cd NLPulse
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Download TextBlob corpora:

```bash
python -m textblob.download_corpora
```

5. (Optional) Download NLTK corpora manually:

```python
import nltk
nltk.download('brown')
nltk.download('punkt')
```

---

## Usage

1. Run the Streamlit interface:

```bash
streamlit run gui/interface.py
```

2. Text Input: Type or paste your text into the input box and click **Analyze Text**.
3. Audio Input: Upload a WAV, MP3, or FLAC audio file, then click **Analyze Text** to transcribe and analyze it. Results include transcribed text, sentiment, word count, and keywords.

---

## Project Structure

```bash
NLPulse/
├─ analyzer/
│  ├─ text_analysis.py
│  └─ speech_analysis.py
├─ gui/
│  └─ interface.py
├─ assets/
├─ requirements.txt
├─ README.md
└─ venv/
```

---

## Advanced Features (Future Improvements)

- Multi-language support for speech and text analysis.
- Real-time audio transcription using microphone input.
- Visualizations for sentiment over time.
- Keyword cloud for quick insights.
- Optimized caching for repeated analyses.

---

## Contribution

Contributions are welcome! Fork the repository, create a feature branch, and submit a pull request. Follow Python best practices and keep code modular.

---

## Contact

For questions, suggestions, or bug reports:  
**Email:** selimhocaoglu9@gmail.com