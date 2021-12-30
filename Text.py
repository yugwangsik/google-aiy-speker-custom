from google.cloud import texttospeech
import pygame

def play():
    pygame.mixer.init()
    pygame.mixer.music.load("/home/pi/AIY-projects-python/src/examples/voice/test.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() == True:
        continue
    
    return None


def tts(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
            language_code = 'ko-KR', 
            ssml_gender = texttospeech.SsmlVoiceGender.FEMALE)

    audio_config = texttospeech.AudioConfig(
            audio_encoding = texttospeech.AudioEncoding.MP3)

    response = client.synthesize_speech(
            request={"input": input_text, "voice": voice, "audio_config": audio_config})

    with open('test.mp3', 'wb') as out:
        out.write(response.audio_content)
        print('test.mp3 file')

    play()

    return None

