#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 21 16:10:57 2022

@author: cristian
"""

import platform
import speech_recognition as sr


if platform.system() == "Linux":
    from ctypes import CFUNCTYPE, c_char_p, c_int, cdll
    #Define error handler
    error_handler =CFUNCTYPE\
    (None,c_char_p, c_int, c_char_p, c_int, c_char_p)
    
    def py_error_handler(filename, line, function, err, fmt):
        pass
    
    c_error_handler = error_handler(py_error_handler)
    asound = cdll.LoadLibrary('libasound.so')
    asound.snd_lib_error_set_handler(c_error_handler)

def voice_to_text():
    voice_input = ""
    speech = sr.Recognizer()
    with sr.Microphone() as source:
        speech.adjust_for_ambient_noise(source)
        try:
            audio = speech.listen(source)
            voice_input = speech.recognize_google(audio)
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            pass
        except sr.WaitTimeoutError:
            pass
    return voice_input