import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import keyboard
import colors
import subprocess as sub
import os
from pygame import mixer
from io import open
from tkinter import *
from PIL import Image, ImageTk

main_window = Tk()
main_window.title("Nina AI")

main_window.geometry("800x400")
main_window.resizable(0, 0)
main_window.configure(bg='#8E2DE2')

name = "nina"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 145)

sites = {'google': 'google.com',
         'youtube': 'youtube.com',
         'facebook': 'facebook.com',
         'whatsapp': 'web.whatsapp.com',
         'discord': 'discord.com',
         'pinterest': 'pinterest.com',
         'prime_video': 'primevideo.com',
         'anime_flv': 'animeflv.net'
         }


def talk(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    try:
        with sr.Microphone() as source:
            print("Escuchando . . .")
            pc = listener.listen(source)
            rec = listener.recognize_google(pc, language="es")
            rec = rec.lower()
            if name in rec:
                rec = rec.replace(name, '')

    except:
        pass
    return rec


def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, ya puedes revisarlo")
    sub.Popen("notas.txt", shell=True)


def ok_nina():
    rec = listen()
    if 'reproduce' in rec:
        music = rec.replace('reproduce', '')
        print("Reproduciendo . . ." + music)
        talk("Reproduciendo . . ." + music)
        pywhatkit.playonyt(music)
    elif 'busca' in rec:
        search = rec.replace('busca', '')
        wikipedia.set_lang("es")
        wiki = wikipedia.summary(search, 3)
        print(search + ": " + wiki)
        talk("Mira lo qu encontré: " + wiki)
    elif 'alarma' in rec:
        alarma = rec.replace('alarma', '')
        alarma = alarma.strip()
        talk("Alarma activada a las " + alarma + "horas")
        while True:
            if datetime.datetime.now().strftime('%H:%M') == alarma:
                print("DESPIERTA !!!")
                mixer.init()
                mixer.music.load("y2mate.com - Gravity Falls opening theme FULL.mp3")
                mixer.music.play()
                if keyboard.read_key() == "s":
                    mixer.music.stop()
                    break
    elif 'colores' in rec:
        talk("Enseguida")
        colors.capture()
    elif 'abre' in rec:
        abre = rec.replace('abre', '')
        abre = abre.strip()
        talk("Abriendo" + abre)
        if sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".txt", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".docx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".pptx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".xlsx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".pdf", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + abre + ".txt", shell=True) and sub.Popen(
                "C:/Users/juanb/OneDrive/Documentos/" + abre + ".docx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + abre + ".pptx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + abre + ".xlsx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + abre + ".pdf", shell=True) == False:
            talk("Uups, problema inesperado, revisa que el nombre sea el correcto")
    elif 'escribe' in rec:
        try:
            with open("notas.txt", 'a') as f:
                write(f)

        except FileNotFoundError as e:
            file = open("notas.txt", 'w')
            write(file)
    elif 'termina' in rec:
        talk('Como desees...')
