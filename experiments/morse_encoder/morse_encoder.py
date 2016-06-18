#!/usr/bin/env python3
from threading import Thread

import serial
from subprocess import DEVNULL, STDOUT, check_call
import sys
from time import sleep

short_beep_time = 0.1

codes = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----'
}

arduino = serial.Serial('/dev/ttyACM0', 9600)

def blink_alert(iterations = 1):
    arduino.write(b'A')

def blink_short(iterations = 1):
    arduino.write(b'S')

def blink_long(iterations = 1):
    arduino.write(b'L')

def clear_alerts():
    arduino.write(b'C')

def beep_short(iterations = 1):
    try:
        for i in range(iterations):
            check_call(['pactl', 'load-module', 'module-sine', 'frequency=1000'], stdout=DEVNULL, stderr=STDOUT)
            sleep(short_beep_time)
            check_call(['pactl', 'unload-module', 'module-sine'])
    except KeyboardInterrupt:
        check_call(['pactl', 'unload-module', 'module-sine'])

def beep_long(iterations = 1):
    try:
        for i in range(iterations):
            check_call(['pactl', 'load-module', 'module-sine', 'frequency=1000'], stdout=DEVNULL, stderr=STDOUT)
            sleep(3 * short_beep_time)
        check_call(['pactl', 'unload-module', 'module-sine'])
    except KeyboardInterrupt:
        check_call(['pactl', 'unload-module', 'module-sine'])

def pause():
    sleep(short_beep_time)

def encode(string):
    # Check if string is empty
    if not string:
        sys.exit("ERROR: Cannot encode empty string. Aborting!")

    # Capitalize string (if not already)
    string = string.upper()

    # Encode string char-by-char
    beep_array = []
    for char in string:
        if char in codes:
            beep_array.append(codes[char])

    return beep_array

def play(beeps):
    # Check if beep array is empty
    if not beeps:
        sys.exit("ERROR: Cannot play empty beep array. Aborting!")

    for beep in beeps:
        for char in beep:
            if char == '.':
                Thread(target = beep_short()).start()
                Thread(target = blink_short()).start()

            elif char == '-':
                Thread(target=beep_long()).start()
                Thread(target=blink_long()).start()

        pause()