#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 12:33:45 2022

@author: cristian
"""
#Import the platfrom module to identify the OS
import platform 

if platform.system() == "Windows":
    import pyttsx3
    try:
        engine = pyttsx3.init()
    except ImportError:
        pass
    except RuntimeError:
        pass
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate', 150)
    engine.setProperty('volume', 1.2)
    
    def print_say(txt):
        print(txt)
        engine.say(txt)
        engine.runAndWait()
elif platform.system() == "Darwin" or platform.system() == "Linux":
    import os
    
    def print_say(texts):
        print(texts)
        texts = texts.replace('"','')
        texts = texts.replace("'", "")
        os.system(f'gtts-cli --nocheck "{texts}" | mpg123 -q -')
        