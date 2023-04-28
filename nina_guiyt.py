import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import cv2
import datetime
import keyboard
import colors
import subprocess as sub
import os
from pygame import mixer
from io import open
from tkinter import *
from PIL import Image, ImageTk
import threading as tr

main_window = Tk()
main_window.title("Nina AI")

main_window.geometry("1800x900")
main_window.resizable(1, 1)
main_window.configure(bg='#3c1053')

comandos = """
            - Reproduce.......(canción)
            - Busca...........(de Wikipedia)
            - Abre............(página web)
            - Alarma..........(horario de 24 hrs)
            - Archivo.........(de documentos)
            - Escribe.........(archivo de notas)
            - Termina.........(Finalizar programa)
"""

label_title = Label(main_window, text="Nina AI", bg="#ad5389", fg="#FFEFBA",
                    font=('Lato', 30, 'bold'))
label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#7F00FF", height=500, width=580)
canvas_comandos.place(x=1200, y=0)
canvas_comandos.create_text(90, 80, text=comandos, fill="white", font='Arial 10')

text_info = Text(main_window, bg="#86A8E7", fg="white")
text_info.place(x=1200, y=505, height=500, width=580)

nina_photo = ImageTk.PhotoImage(Image.open("nina-AI.jpg"))
window_photo = Label(main_window, image=nina_photo)
window_photo.pack(pady=5)
#def latam_voice():
 #   change_voice(4)


#def change_voice(id):
 #   engine.setProperty('voices', voices[id].id)
 #  engine.setProperty('rate', 145)
 # talk("Hola soy Nina!")


name = "nina"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.setProperty('rate', 145)
# for voice in voices:
#   print(voice)

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

def read_and_talk:
    text = text_info.get("1.0","end")
    talk(text)
def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)
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


def clock(rec):
    alarma = rec.replace('alarma', '')
    alarma = alarma.strip()
    talk("Alarma activada a las " + alarma + "horas")
    while True:
        if num[0] != '0' and len(alarma) <5:
            num = '0' + alarma
        print(alarma)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == alarma:
            print("DESPIERTA !!!")
            mixer.init()
            mixer.music.load("y2mate.com - Gravity Falls opening theme FULL.mp3")
            mixer.music.play()
        else:
            continue
        if keyboard.read_key() == "s":
            mixer.music.stop()
            break

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
        talk("Mira lo qu encontré...... abro comillas " + wiki + "... cierro comillas")
        write_text(search + ": " + wiki)
        break
    elif 'alarma' in rec:
        t = tr.Thread(target=clock, args=(rec,))
        t.start()
    elif 'colores' in rec:
        talk("Enseguida")
        colors.capture()
    elif 'abre' in rec:
        for site in sites:
            if site in rec:
                sub.call(f'start opera.exe {sites[site]}', shell=True)
                talk(f'Abriendo {site}')
    elif 'archivo' in rec:
        archivo = rec.replace('archivo', '')
        archivo = archivo.strip()
        talk("Abriendo" + archivo)
        if sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".txt", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".docx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pptx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".xlsx", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pdf", shell=True) == True:
            exit()
        elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".txt", shell=True) and sub.Popen(
                "C:/Users/juanb/OneDrive/Documentos/" + archivo + ".docx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pptx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + archivo + ".xlsx", shell=True) and sub.Popen(
            "C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pdf", shell=True) == False:
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


# Command Voices
#button_voice_latam = Button(main_window, text="Voz Latino América", fg="white", bg="#FDC830",
 #                           font=("Lato", 20, "bold"), command=latam_voice)
button_listen = Button(main_window, text="Escuchar", fg="white", bg="#11998e",
                       font=("Lato", 20, "bold"), width=10, command=ok_nina)
button_listen.pack(pady=10)
button_speak = Button(main_window, text="Hablar", fg="white", bg="#91EAE4",
                            font=("Lato", 15, "bold"), command=read_and_talk)
button_speak.place(x=625, y=190, width=100, height=30)

main_window.mainloop()
