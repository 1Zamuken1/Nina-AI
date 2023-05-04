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

#label_title = Label(main_window, text="Nina AI", bg="#ad5389", fg="#FFEFBA",
 #                   font=('Lato', 30, 'bold'))
#label_title.pack(pady=10)

canvas_comandos = Canvas(bg="#7F00FF", height=200, width=300)
canvas_comandos.place(x=5, y=380)
canvas_comandos.create_text(90, 80, text=comandos, fill="white", font='Arial 10')

text_info = Text(main_window, bg="#86A8E7", fg="black")
text_info.place(x=380, y=100, height=490, width=500)

nina_photo = ImageTk.PhotoImage(Image.open("nina-AI.jpg"))
window_photo = Label(main_window, image=nina_photo)
window_photo.place(x=5, y=5)


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

def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                print(line.split)
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass


#Diccionaries
pages = dict()
charge_data(pages, "pages.txt")
files = dict()
charge_data(files, "files.txt")
programs = dict()
charge_data(programs, "apps.txt")


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
    global namefile_entry, path_files_entry
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

    path_files_entry = Entry(window_files, width=35)
    path_files_entry.pack(pady=1)

    save_button = Button(window_files, text="Guardar", bg='#0082c8', fg="white", width=8, height=1, command=add_files)
    save_button.pack(pady=4)

def open_w_apps():
    global nameapp_entry, path_apps_entry
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

    nameapp_entry = Entry(window_apps)
    nameapp_entry.pack(pady=1)

    path_label = Label(window_apps, text="Ruta de la app", fg="white", bg="#11998e", font=('Lato', 12, 'bold'))
    path_label.pack(pady=2)

    path_apps_entry = Entry(window_apps, width=35)
    path_apps_entry.pack(pady=1)

    save_button = Button(window_apps, text="Guardar", bg='#78ffd6', fg="black", width=8, height=1, command=add_apps)
    save_button.pack(pady=4)
def open_w_pages():
    global namepages_entry, path_pages_entry
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

    namepages_entry = Entry(window_paginas)
    namepages_entry.pack(pady=1)

    path_label = Label(window_paginas, text="URL de la página", fg="white", bg="#F37335", font=('Lato', 12, 'bold'))
    path_label.pack(pady=2)

    path_pages_entry = Entry(window_paginas, width=35)
    path_pages_entry.pack(pady=1)

    save_button = Button(window_paginas, text="Guardar", bg='#605C3C', fg="white", width=8, height=1, command=add_pages)
    save_button.pack(pady=4)

def add_files():
    name_file = namefile_entry.get().strip()
    path_file = path_files_entry.get().strip()

    files[name_file] = path_file
    save_data(name_file, path_file, "files.txt")
    namefile_entry.delete(0, "end")
    path_files_entry.delete(0, "end")

def add_apps():
    name_file = nameapp_entry.get().strip()
    path_apps = path_apps_entry.get().strip()

    programs[name_file] = path_apps
    save_data(name_file, path_apps, "apps.txt")
    nameapp_entry.delete(0, "end")
    path_apps_entry.delete(0, "end")

def add_pages():
    name_page = namepages_entry.get().strip()
    url_page = path_pages_entry.get().strip()

    pages[name_page] = url_page
    save_data(name_page, url_page, "pages.txt")
    namepages_entry.delete(0, "end")
    path_pages_entry.delete(0, "end")

def save_data(key, value, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write(key + "," + value + "\n")
    except FileNotFoundError as f:
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

def talk_pages():
    if bool(pages) == True:
        talk("has agregado las siguientes páginas web . . .")
        for page in pages:
            talk(page)
    else:
        talk("Aún no has agregado páginas web . . .")
def talk_files():
    if bool(files) == True:
        talk("has agregado los siguientes archivos . . .")
        for file in files:
            talk(file)
    else:
        talk("Aún no has agregado archivos . . .")
def talk_programs():
    if bool(programs) == True:
        talk("has agregado los siguientes programas . . .")
        for program in programs:
            talk(program)
    else:
        talk("Aún no has agregado programas . . .")

def give_me_name():
    talk("Hola, ¿cómo te llamas?")
    name = listen()
    name = name.strip()
    talk(f"Bienvenido {name}")

    try:
        with open("name.txt", 'w') as f:
            f.write(name)
    except FileNotFoundError:
        file = open("name.txt")
        file.write(name)

def say_hello():
    if os.path.exists("name.txt"):
        with open("name.txt") as f:
            for name in f:
                talk(f"Hola de nuevo, {name}")
    else:
        give_me_name()

def thread_hello():
    t = tr.Thread(target=say_hello)
    t.start()

thread_hello()



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
        task = rec.replace('abre', '').strip()
        if task in pages:
            for task in pages:
                if task in rec:
                    sub.call(f'start opera.exe {pages[task]}', shell=True)
                    talk(f'Abriendo {task}')
        elif task in programs:
            for task in programs:
                if task in rec:
                    talk(f'Abriendo {task}')
                    sub.Popen(programs[task])
        else:
            talk("Lo siento, parece que aún no has agregado la app o página web. Por favor usa los botones de Agregar ")
    elif 'archivo' in rec:
        file = rec.replace('Archivo', '').strip()
        if file in files:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell=True)
                    talk(f'Abriendo{file}')
        else:
            talk("Lo siento, parece que aún no has agregado el archivo. Por favor usa el botón de Agregar ")
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
button_listen.place(x=60, y=600, width=200, height=60)
button_speak = Button(main_window, text="Hablar", fg="white", bg="#91EAE4",
                            font=("Lato", 20, "bold"), command=read_and_talk)
button_speak.place(x=550, y=600, width=200, height=60)
button_add_files = Button(main_window, text="Agregar archivos", fg="white", bg="#000046",
                            font=("Lato", 20, "bold"), command=open_w_files)
button_add_files.place(x=980, y=120, width=250, height=60)
button_add_apps = Button(main_window, text="Agregar apps", fg="white", bg="#11998e",
                            font=("Lato", 20, "bold"), command=open_w_apps)
button_add_apps.place(x=980, y=190, width=250, height=60)
button_add_pages = Button(main_window, text="Agregar páginas", fg="white", bg="#F37335",
                            font=("Lato", 20, "bold"), command=open_w_pages)
button_add_pages.place(x=980, y=260, width=250, height=60)

#View files, apps and pages saved

button_tell_files = Button(main_window, text="Archivos guardados", fg="white", bg="#000046",
                            font=("Lato", 20, "bold"), command=talk_files)
button_tell_files.place(x=1250, y=120, width=280, height=60)
button_tell_apps = Button(main_window, text="Apps guardadas", fg="white", bg="#11998e",
                            font=("Lato", 20, "bold"), command=talk_programs)
button_tell_apps.place(x=1250, y=190, width=280, height=60)
button_tell_pages = Button(main_window, text="Páginas guardadas", fg="white", bg="#F37335",
                            font=("Lato", 20, "bold"), command=talk_pages)
button_tell_pages.place(x=1250, y=260, width=280, height=60)

main_window.mainloop()
