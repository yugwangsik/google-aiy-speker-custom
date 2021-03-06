#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Run a recognizer using the Google Assistant Library.

The Google Assistant Library has direct access to the audio API, so this Python
code doesn't need to record audio. Hot word detection "OK, Google" is supported.

It is available for Raspberry Pi 2/3 only; Pi Zero is not supported.
"""

import logging
import platform
import subprocess
import sys

from google.assistant.library.event import EventType

from aiy.assistant import auth_helpers
from aiy.assistant.library import Assistant
from aiy.board import Board, Led
from aiy.voice import tts


def process_event(assistant, led, event):
    logging.info(event)
    print('11')
    if event.type == EventType.ON_START_FINISHED:
        led.state = Led.BEACON_DARK  # Ready.
        print('Say "OK, Google" then speak, or press Ctrl+C to quit...')
        print('1')
    elif event.type == EventType.ON_CONVERSATION_TURN_STARTED:
        led.state = Led.ON  # Listening.
        print('2')
    elif event.type == EventType.ON_RECOGNIZING_SPEECH_FINISHED and event.args:
        print('You said:', event.args['text'])
        text = event.args['text'].lower()
        print('3')
        #print('---------------------------------')
        print(text)
    elif event.type == EventType.ON_END_OF_UTTERANCE:
        led.state = Led.PULSE_QUICK  # Thinking.
        print('7')
    elif (event.type == EventType.ON_CONVERSATION_TURN_FINISHED
          or event.type == EventType.ON_CONVERSATION_TURN_TIMEOUT
          or event.type == EventType.ON_NO_RESPONSE):
        led.state = Led.BEACON_DARK  # Ready.
        print('8')
    elif event.type == EventType.ON_ASSISTANT_ERROR and event.args and event.args['is_fatal']:
        print('9')
        sys.exit(1)


def main():
    #logging.basicConfig(level=logging.INFO)

    credentials = auth_helpers.get_assistant_credentials()
    with Board() as board, Assistant(credentials) as assistant:
        for event in assistant.start():
            #print('10')
            print('---------------------------------')
            process_event(assistant, board.led, event)


if __name__ == '__main__':
    main()
