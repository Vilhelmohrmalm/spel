# Python Typing Text Effect - www.101computing.net/python-typing-text-effect/
import time
import os
import sys


def typingPrint(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)


def typingInput(text):
    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.015)
    value = input()
    return value


def clearScreen():
    os.system("cls")
