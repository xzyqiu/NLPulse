import speech_recognition as sr
from pydub import AudioSegment

def speech_to_text(file_path):
    audio = AudioSegment.from_file(file_path)
    audio.export("output.wav", format="wav")

    recognizer = sr.Recognizer()
    with sr.AudioFile("output.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    return text

if __name__ == "__main__":
    file_path = "assets/sample.mp3"
    print(speech_to_text(file_path))