'''
Trabalho da disciplina de Programação Orientada a Objetos (SSC0103)
Álbum de figurinhas com Bozó
Grupo G16:
Gabriela Bacarin Marcondes - N°USP: 10873351 - 25% participação
Hélio Nogueira Cardoso     - N°USP: 10310227 - 25% participação
João Pedro Duarte Nunes    - N°USP: 12542460 - 25% participação
Thaís Ribeiro Lauriano     - N°USP: 12542518 - 25% participação

'''

import random as rd
from turtle import color
import PySimpleGUI as sg
from PIL import Image

from album import *
from figurinha import Figurinha
import sys
sys.path.insert(0, './bozo')
from Bozo import Bozo
from param import Param as pr

sg.theme(pr.theme)

# Creating window to show how to play
# Menu 'Ajuda' > 'Como Jogar'
def show_how_to_play_window():
    help_file = open('aux/how_to_play.txt', 'r')

    text = ""

    for line in help_file:
        text += line + '\n'

    how_to_play_layout = [
        [sg.Multiline(text, size=(50,25), font=pr.font, background_color='white', text_color='black')]
    ]

    window = sg.Window("Como Jogar", layout=how_to_play_layout)

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break

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

menu_def = [['&Opções', ['&Salvar', '&Carregar Último Save', '&Reiniciar']],['&Ajuda', ['&Como Jogar']]]

winning_layout = [
    [sg.Menu(menu_def)],
    [sg.Text("Parabéns!!! Você completou o Álbum da Copa!!!")],
    [sg.Button("Álbum")],
    [sg.Button("Sair")]
]

layout = [
    [sg.Menu(menu_def)],
    [sg.Text("O que deseja ver:", font=pr.title_font)],
    [sg.Button("Álbum"), sg.Button("Troca e Venda"), sg.Button("Bozó"), sg.Button("Comprar Pacote")],
    [sg.Text("Créditos: "), sg.Text(f"${creditos}", key="-CREDITOS-")],
    [sg.Text("\n", key="-MSG-")],
    [sg.Button("Sair")]
]

window = sg.Window("Master Copa", layout, element_justification='c', font=pr.font, size=(800,250))

album = Album("aux/selecoes.csv") # Create an album
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
    elif event == "Salvar":
        print("Salvando...")
        save_file = open('aux/save.txt', 'w')

        save_file.write(str(creditos) + '\n')

        n_figs = 0

        for page_index in range(album.total_pages):
            for fig_index in range(pr.num_fig_pg):
                if album.enables[page_index][fig_index]:
                    n_figs += 1

        save_file.write(str(n_figs) + '\n')

        for page_index in range(album.total_pages):
            for fig_index in range(pr.num_fig_pg):
                if album.enables[page_index][fig_index]:
                    save_file.write(str(page_index) + " " + str(fig_index) + '\n')

        # Save replicated

        save_file.write(str(len(album.replicated)) + '\n')

        for replicated in album.replicated:
            save_file.write(str(replicated.page_index) + " " + str(replicated.fig_index) + " " + str(replicated.amount) + '\n')

        save_file.close()              
    elif event == "Carregar Último Save":
        save_file = open('aux/save.txt', 'r')

        creditos = int(save_file.readline().strip())

        n = int(save_file.readline().strip())

        for page_index in range(album.total_pages):
            for fig_index in range(pr.num_fig_pg):
                album.enables[page_index][fig_index] = False

        for i in range(n):
            fig_page_index, fig_fig_index = save_file.readline().strip().split()

            fig_page_index = int(fig_page_index)
            fig_fig_index = int(fig_fig_index)
            
            album.enables[fig_page_index][fig_fig_index] = True

        # Load replicated

        album.replicated = []

        n_replicated = int(save_file.readline().strip())
        
        for i in range(n_replicated):
            rep_page_index, rep_fig_index, amt = save_file.readline().strip().split()

            rep_page_index = int(rep_page_index)
            rep_fig_index = int(rep_fig_index)
            amt = int(amt)

            repl = Figurinha(rep_page_index, rep_fig_index)
            repl.amount = amt

            album.replicated.append(repl)

        save_file.close()
    elif event == "Reiniciar":
        for page_index in range(album.total_pages):
            for fig_index in range(pr.num_fig_pg):
                album.enables[page_index][fig_index] = False

        album.replicated = []

        creditos = 0
    elif event == "Como Jogar":
        show_how_to_play_window()
    elif event == sg.WIN_CLOSED or event == "Sair":
        direct_exit_event = True
        break
    elif event == "Álbum":
        show_album_window(album)
    elif event == "Bozó":
        b = Bozo()
        creditos += b.lucro * 10
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

        if event == "Álbum":
            show_album_window(album)
        elif event == "Sair" or event == sg.WIN_CLOSED:
            break
    
    winning_window.close()

