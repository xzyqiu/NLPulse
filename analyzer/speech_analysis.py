import os
import tempfile
from typing import Optional

import speech_recognition as sr
from pydub import AudioSegment


def speech_to_text(file_path: str) -> str:
    """Convert an audio file to text.

    The audio is converted to WAV in a temporary file for compatibility with
    the `speech_recognition` library. The temporary file is removed on exit.

    Raises FileNotFoundError if `file_path` doesn't exist.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    recognizer = sr.Recognizer()
    tmp_wav_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_wav_path = tmp.name

        audio = AudioSegment.from_file(file_path)
        audio.export(tmp_wav_path, format="wav")

        with sr.AudioFile(tmp_wav_path) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = ""

        return text
    finally:
        if tmp_wav_path and os.path.exists(tmp_wav_path):
            try:
                os.remove(tmp_wav_path)
            except OSError:
                pass
import speech_recognition as sr
from pydub import AudioSegment
import os
import tempfile
from typing import Optional

def speech_to_text(file_path: str) -> str:
    """Convert an audio file to text.

    The audio is converted to WAV in a temporary file for compatibility with
    the `speech_recognition` library. The temporary file is removed on exit.

    Raises FileNotFoundError if `file_path` doesn't exist.
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Audio file not found: {file_path}")

    recognizer = sr.Recognizer()

    tmp_wav_path = None
    try:
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
            tmp_wav_path = tmp.name

        audio = AudioSegment.from_file(file_path)
        audio.export(tmp_wav_path, format="wav")

        with sr.AudioFile(tmp_wav_path) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data)
        except sr.UnknownValueError:
            text = ""

        return text
    finally:
        if tmp_wav_path and os.path.exists(tmp_wav_path):
            try:
                os.remove(tmp_wav_path)
            except OSError:
                pass


if __name__ == "__main__":
    sample = "assets/sample.mp3"
    try:
        print(speech_to_text(sample))
    except FileNotFoundError:
        print("Sample audio not found. Place an audio file at assets/sample.mp3 to run this demo.")