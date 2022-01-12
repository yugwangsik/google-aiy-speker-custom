# _*_ coding: utf-8 _*_
import argparse
import locale
import logging

from google.assistant.library.event import EventType
from aiy.board import Board, Led
from aiy.cloudspeech import CloudSpeechClient
import aiy.voice.tts

import database
import Text

def call(client, hints):
    trigger = '유비스'
    trigger_text = client.recognize(language_code='ko_KR', hint_phrases=hints)
    if trigger in trigger_text:
        aiy.voice.tts.say('yes')
        print(trigger_text)
        return True
    else:
        return False


def get_hints(language_code):
    if language_code.startswith('ko_'):
        return None

    return None

def locale_language():
    language, _ = locale.getdefaultlocale()
    return language

def main():
    address = '/home/pi/cloud_speech.json'
    logging.basicConfig(level=logging.DEBUG)
    #a = locale_language()
    #print(a)
    trigger = '유비스'

    parser = argparse.ArgumentParser(description='Assistant service example.')
    parser.add_argument('--language', default=locale_language())
    args = parser.parse_args()

    logging.info('Initializing for language %s...', 'ko_KR')
    hints = get_hints('ko_KR')
    #print(hints)
    client = CloudSpeechClient()
    #print(client)
    #trigger_text = client.recoginze(language_code='ko_KR', hint_phrases=hints)
    

    with Board() as board:
        while True:
            try:
                stat = call(client, hints)
                if stat:
                    if hints:
                        logging.info('Say something, e.g. %s.' % ','.join(hints))
                    else:
                        logging.info('Say someting.')

                    text = client.recognize(language_code='ko_KR', hint_phrases=hints)
                    #text = text.lower()
                    print(text)

                    if text is None:
                        logging.info('You said nothing.')
                        continue
                    elif text is not None:
                        speech = database.myDB(text)
                        print(speech)
                        Text.tts(speech)

                    logging.info('Your said: "%s"' % text)
                    #text = text.lower()
                    if '안녕' in text:
                        aiy.voice.tts.say('goodbye')
                        break
            except Exception as e:
                continue
            


if __name__ == '__main__':
    main()
