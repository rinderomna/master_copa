import random as rd
import PySimpleGUI as sg
from PIL import Image

import sys
sys.path.insert(0, './bozo')
from Bozo import Bozo

from album import *
from figurinha import Figurinha
from param import Param as pr

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
    [sg.Text("", key="-MSG-")],
    [sg.Button("Sair")]
]

window = sg.Window("Master Copa", layout, element_justification='c', font=pr.font)

album = Album() # Create an album
msg_last_set = False

while True: 
    event, values = window.read()

    if msg_last_set:
        window["-MSG-"].update("")
        msg_last_set = False
    
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Album":
        show_album_window(album)
    elif event == "Bozo":
        b = Bozo()
        creditos += b.lucro * 10
    elif event == "Figurinhas":
        show_replicated_window(album, window)
    elif event == "Comprar Pacote":
        if (creditos >= 30):
            creditos -= 30
            page_index = rd.randint(0, album.total_pages - 1)
            fig_index  = rd.randint(0, 5)

            if not album.unables[page_index][fig_index]:
                album.unables[page_index][fig_index] = True
                window["-MSG-"].update(f"Figurinha {page_index + 1}-{fig_index + 1} nova!")
                msg_last_set = True
            else:
                replicated_figurinha = Figurinha(page_index, fig_index)

                if replicated_figurinha in album.replicated:
                    pass
                    i = album.replicated.index(replicated_figurinha)
                    album.replicated[i].amount += 1
                else:
                    album.replicated.append(replicated_figurinha)
                
                window["-MSG-"].update(f"Figurinha {page_index + 1}-{fig_index + 1} já adquirida.")
                msg_last_set = True
        else:
            window["-MSG-"].update(f"Saldo insuficiente, um pacote custa $30.")
            msg_last_set = True

    window["-CREDITOS-"].update(f"${creditos}")

window.close()