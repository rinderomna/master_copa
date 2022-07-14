import PySimpleGUI as sg
from PIL import Image

from album import *

def resize_image(filename, basewidth, height=None):
    img = Image.open(filename)
    
    if not height:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    else:
        img = img.resize((basewidth, height), Image.ANTIALIAS)

    img.save(filename)

creditos = 0

layout = [
    [sg.Text("O que deseja ver:")],
    [sg.Button("Album"), sg.Button("Figurinhas"), sg.Button("Bozo"), sg.Button("Comprar Pacote")],
    [sg.Text("Créditos: "), sg.Text(f"${creditos}", key="-CREDITOS-")],
    [sg.Button("Sair")]
]

window = sg.Window("Master Copa", layout, element_justification='c')

album = Album() # Create an album

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Album":
        show_album_window(album)
    elif event == "Bozo":
        creditos += 10
    elif event == "Comprar Pacote":
        if (creditos >= 30):
            creditos -= 30

    window["-CREDITOS-"].update(f"${creditos}")

window.close()