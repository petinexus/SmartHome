import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import minimalmodbus
import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()

engine = pyttsx3.init()
engine.setProperty('rate', 190)
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_hu-HU_Szabolcs')

q = queue.Queue()

def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

try:
    samplert = int(sd.query_devices('input')['default_samplerate'])
    with sd.RawInputStream(samplerate=samplert, blocksize = 8000, dtype='int16', channels=1, callback=callback):
            rec = vosk.KaldiRecognizer(vosk.Model("model"), samplert)
            print('#' * 80)
            print('Nyomd meg Ctrl+C a program megállításához')
            print('#' * 80)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):
                    res =  json.loads(rec.Result())["text"]
                    if "hey frank" in res:
                        engine.say("Várom a parancsát uram")
                        engine.runAndWait()
                        done = True
                        while done:
                            print("!!!Beszélhet!!!")
                            with sr.Microphone() as source:
                                audio = r.listen(source, phrase_time_limit=10)
                                try:
                                    gores = r.recognize_google(audio, language="hu-HU")
                                    print("Google hangfelismerő: " + gores)

                                    if "fel az első lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 10) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(1, 1)
                                        done = False 
                                    elif "le az első lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 10) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(1, 0)
                                        done = False
                                    elif "fel a 2 lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 10) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(0, 1)
                                        done = False 
                                    elif "le a 2 lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 10) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(0, 0)
                                        done = False
                                    elif "fel a 3. lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 255) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(0, 1)
                                        done = False 
                                    elif "le a 3. lámpát" in gores or "le a harmadik lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 255) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(0, 0)
                                        done = False
                                    elif "fel a 4 lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 15) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(3, 1)
                                        done = False 
                                    elif "le a 4 lámpát" in gores:
                                        instrument = minimalmodbus.Instrument('COM3', 15) 
                                        instrument.serial.baudrate = 9600
                                        modbus = instrument.write_bit(3, 0)
                                        done = False
                                    elif "fel az összes lámpát" in gores:
                                        engine.say("Még nincs késza modul, elnézését kérem!")
                                        engine.runAndWait()
                                        done = False 
                                    elif "le az összes lámpát" in gores:
                                        engine.say("Még nincs késza modul, elnézését kérem!")
                                        engine.runAndWait()
                                        done = False
                                    elif "mennyi az idő" in gores:
                                        engine.say("Még nincs késza modul, elnézését kérem!")
                                        engine.runAndWait()
                                        done = False 
                                    elif "hány fok van" in gores or "Hány fok van" in gores:
                                        engine.say("Még nincs késza modul, elnézését kérem!")
                                        engine.runAndWait()
                                        done = False  
                                    elif "stop" in gores:
                                        sys.exit(0)
                                    elif "Ügyes vagy" in gores or "ügyes vagy" in gores:
                                        engine.say("Köszönöm uram, ön se semmi")
                                        engine.runAndWait()
                                        done = False  
                                    else:
                                        engine.say("Megismételné kérem a parancsot!")
                                        engine.runAndWait()

                                except sr.UnknownValueError:
                                    engine.say("Nem hallottam jól, megismételné kérem a parancsot!")
                                    engine.runAndWait()
                                except sr.RequestError as e:
                                    engine.say("Valami elromlott!")
                                    engine.runAndWait()
                        
except KeyboardInterrupt:
    print('\nDone')