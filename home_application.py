import random as rd
import PySimpleGUI as sg
from PIL import Image

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

winning_layout = [
    [sg.Text("Parabéns!!! Você completou o Álbum da Copa!!!")],
    [sg.Button("Album")],
    [sg.Button("Sair")]
]

layout = [
    [sg.Text("O que deseja ver:")],
    [sg.Button("Album"), sg.Button("Troca e Venda"), sg.Button("Bozo"), sg.Button("Comprar Pacote")],
    [sg.Text("Créditos: "), sg.Text(f"${creditos}", key="-CREDITOS-")],
    [sg.Text("\n", key="-MSG-")],
    [sg.Button("Sair")]
]

window = sg.Window("Master Copa", layout, element_justification='c', font=pr.font)

album = Album("test.csv") # Create an album
msg_last_set = False

no_figurinha_missing = True
direct_exit_event = False

while True: 
    # Check if album is complete
    no_figurinha_missing = True

    try:
        for page_index in range(album.total_pages):
            for fig_index in range(pr.num_fig_pg):
                if not album.enables[page_index][fig_index]:
                    no_figurinha_missing = False
                    raise Exception() # break both loops
    except:
        pass

    if no_figurinha_missing:
        break

    event, values = window.read()

    # ----------------------------------           

    if msg_last_set:
        window["-MSG-"].update("\n")
        msg_last_set = False
    
    if event == sg.WIN_CLOSED or event == "Sair":
        direct_exit_event = True
        break
    elif event == "Album":
        show_album_window(album)
    elif event == "Bozo":
        creditos += 10
    elif event == "Troca e Venda":
        creditos = show_replicated_window(album, window, creditos)
    elif event == "Comprar Pacote":
        if (creditos >= pr.pkg_price):
            creditos -= pr.pkg_price

            msg_new_figs = "    Novas Figurinhas: "
            msg_rep_figs = "Figurinhas Repetidas: "

            for i in range(pr.figs_per_pkg):
                page_index = rd.randint(0, album.total_pages - 1)
                fig_index  = rd.randint(0, pr.num_fig_pg - 1)

                if not album.enables[page_index][fig_index]:
                    album.enables[page_index][fig_index] = True                        
                    msg_new_figs += f"{page_index + 1}-{fig_index + 1} "
                else:
                    replicated_figurinha = Figurinha(page_index, fig_index)

                    msg_rep_figs += f"{page_index + 1}-{fig_index + 1} "

                    if replicated_figurinha in album.replicated:
                        i = album.replicated.index(replicated_figurinha)
                        album.replicated[i].amount += 1

                    else:
                        album.replicated.append(replicated_figurinha)
                    
                window["-MSG-"].update(msg_new_figs + "\n" + msg_rep_figs)
                msg_last_set = True
        else:
            window["-MSG-"].update(f"Saldo insuficiente, um pacote custa ${pr.pkg_price}.\n")
            msg_last_set = True

    window["-CREDITOS-"].update(f"${creditos}")

window.close()

if no_figurinha_missing and not direct_exit_event:
    winning_window = sg.Window("Master Copa (Completo)", winning_layout, element_justification='c', font=pr.font)
    
    while True:
        event, values = winning_window.read()

        if event == "Album":
            show_album_window(album)
        elif event == "Sair" or event == sg.WIN_CLOSED:
            break
    
    winning_window.close()