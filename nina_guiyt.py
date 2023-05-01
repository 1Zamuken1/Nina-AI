import tkinter

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
main_window.resizable(0, 0)
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
canvas_comandos.place(x=1215, y=0)
canvas_comandos.create_text(90, 80, text=comandos, fill="white", font='Arial 10')

text_info = Text(main_window, bg="#86A8E7", fg="black")
text_info.place(x=1218, y=505, height=500, width=580)

nina_photo = ImageTk.PhotoImage(Image.open("nina-AI.jpg"))
window_photo = Label(main_window, image=nina_photo)
window_photo.pack(padx=0)
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

sites = dict()

files = dict()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def read_and_talk():
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

def open_w_files():
    window_files = Toplevel()
    window_files.title("Agregar archivos")
    window_files.configure(bg="#000046")
    window_files.geometry("500x200")
    window_files.resizable(0,0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')

    title_label = Label(window_files, text="Agrega un archivo", fg="white", bg="#000046", font=('Lato',15,'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_files, text="Nombre del archivo", fg="white", bg="#000046", font=('Lato', 12, 'bold'))
    name_label.pack(pady=2)

    namefile_entry = Entry(window_files)
    namefile_entry.pack(pady=1)

    path_label = Label(window_files, text="Ruta del archivo", fg="white", bg="#000046", font=('Lato', 12, 'bold'))
    path_label.pack(pady=2)

    path_entry = Entry(window_files, width=35)
    path_entry.pack(pady=1)

    save_button = Button(window_files, text="Guardar", bg='#0082c8', fg="white", width=8, height=1) #, command=add_files)
    save_button.pack(pady=4)

def open_w_apps():
    window_apps = Toplevel()
    window_apps.title("Agregar apps")
    window_apps.configure(bg="#11998e")
    window_apps.geometry("500x200")
    window_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')

    title_label = Label(window_apps, text="Agrega una app", fg="white", bg="#11998e", font=('Lato', 15, 'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_apps, text="Nombre de la app", fg="white", bg="#11998e", font=('Lato', 12, 'bold'))
    name_label.pack(pady=2)

    namefile_entry = Entry(window_apps)
    namefile_entry.pack(pady=1)

    path_label = Label(window_apps, text="Ruta de la app", fg="white", bg="#11998e", font=('Lato', 12, 'bold'))
    path_label.pack(pady=2)

    path_entry = Entry(window_apps, width=35)
    path_entry.pack(pady=1)

    save_button = Button(window_apps, text="Guardar", bg='#78ffd6', fg="black", width=8,
                         height=1)  # , command=add_files)
    save_button.pack(pady=4)
def open_w_pages():
    window_paginas = Toplevel()
    window_paginas.title("Agregar páginas")
    window_paginas.configure(bg="#F37335")
    window_paginas.geometry("500x200")
    window_paginas.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_paginas)} center')

    title_label = Label(window_paginas, text="Agrega una página", fg="white", bg="#F37335", font=('Lato', 15, 'bold'))
    title_label.pack(pady=3)
    name_label = Label(window_paginas, text="Nombre de la página", fg="white", bg="#F37335", font=('Lato', 12, 'bold'))
    name_label.pack(pady=2)

    namefile_entry = Entry(window_paginas)
    namefile_entry.pack(pady=1)

    path_label = Label(window_paginas, text="URL de la página", fg="white", bg="#F37335", font=('Lato', 12, 'bold'))
    path_label.pack(pady=2)

    path_entry = Entry(window_paginas, width=35)
    path_entry.pack(pady=1)

    save_button = Button(window_paginas, text="Guardar", bg='#605C3C', fg="white", width=8,
                         height=1)  # , command=add_files)
    save_button.pack(pady=4)

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
        #break
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
        for file in files:
            if file in rec:
                sub.Popen([files[file]], shell=True)
                talk(f'Abriendo{file}')
    #elif 'archivo' in rec:
        #archivo = rec.replace('archivo', '')
        #archivo = archivo.strip()
        #talk("Abriendo" + archivo)
        #if sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".txt", shell=True) == True:
            #exit()
        #elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".docx", shell=True) == True:
            #exit()
        #elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pptx", shell=True) == True:
            #exit()
        #elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".xlsx", shell=True) == True:
            #exit()
        #elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pdf", shell=True) == True:
            #exit()
        #elif sub.Popen("C:/Users/juanb/OneDrive/Documentos/" + archivo + ".txt", shell=True) and sub.Popen(
                #"C:/Users/juanb/OneDrive/Documentos/" + archivo + ".docx", shell=True) and sub.Popen(
            #"C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pptx", shell=True) and sub.Popen(
            #"C:/Users/juanb/OneDrive/Documentos/" + archivo + ".xlsx", shell=True) and sub.Popen(
            #"C:/Users/juanb/OneDrive/Documentos/" + archivo + ".pdf", shell=True) == False:
            #talk("Uups, problema inesperado, revisa que el nombre sea el correcto")
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
                            font=("Lato", 20, "bold"), command=read_and_talk)
button_speak.place(x=800, y=550, width=200, height=60)
button_add_files = Button(main_window, text="Agregar archivos", fg="white", bg="#000046",
                            font=("Lato", 20, "bold"), command=open_w_files)
button_add_files.place(x=780, y=620, width=250, height=60)
button_add_apps = Button(main_window, text="Agregar apps", fg="white", bg="#11998e",
                            font=("Lato", 20, "bold"), command=open_w_apps)
button_add_apps.place(x=800, y=690, width=200, height=60)
button_add_pages = Button(main_window, text="Agregar páginas", fg="white", bg="#F37335",
                            font=("Lato", 20, "bold"), command=open_w_pages)
button_add_pages.place(x=780, y=760, width=250, height=60)

main_window.mainloop()
