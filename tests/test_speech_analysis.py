import pytest

from analyzer._speech import speech_to_text


def test_speech_to_text_missing_file():
    with pytest.raises(FileNotFoundError):
        speech_to_text("this_file_does_not_exist.xyz")
import os
import pytest

from analyzer._speech import speech_to_text


def test_speech_to_text_missing_file():
    with pytest.raises(FileNotFoundError):
        speech_to_text("this_file_does_not_exist.xyz")
