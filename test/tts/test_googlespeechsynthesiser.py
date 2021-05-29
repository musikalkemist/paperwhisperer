from paperwhisperer.tts.googlespeechynthesiser import GoogleSpeechSynthesiser


def test_google_speech_synthesiser_returns_binary_object():
    gss = GoogleSpeechSynthesiser()
    speech_content = gss.synthesise("Hello world")
    assert isinstance(speech_content, bytes)