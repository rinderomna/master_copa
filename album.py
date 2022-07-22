import PySimpleGUI as sg
from PIL import Image
from param import Param as pr
import pandas as pd
from figurinha import Figurinha

sg.theme(pr.theme)

class Album:
    def __init__(self, csv_name):
        #self.file_name = csv_name

        #self.folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
        df = pd.read_csv(csv_name)
        df = df.sort_values(['folder', 'posicao'])
        self.folders = df['folder'].unique()
        self.folders = list(self.folders)
        self.folders.sort()
        self.total_pages = len(self.folders)

        self.names = [[] for i in range(self.total_pages)]
        linha_atual = 0

        for i in range(self.total_pages):
            for j in range(pr.num_fig_pg):
                self.names[i].append(df['jogador'][linha_atual])
                linha_atual += 1

        disables = [False] * pr.num_fig_pg

        self.enables = []

        for i in range(self.total_pages):
            self.enables.append(list(disables))

        self.replicated = []

def resize_image(filename, basewidth, height=None):
    img = Image.open(filename)
    
    if not height:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    else:
        img = img.resize((basewidth, height), Image.ANTIALIAS)

    img.save(filename)

def show_album_window(album: Album):
    resize_image("images/placeholder.png", pr.width, pr.height)

    total_pages = album.total_pages
    page_index = 0 # page_index = page_number - 1 [from 0 to (total_pages - 1)]

    resize_image(f"images/{album.folders[0]}/1.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/2.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/3.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/4.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/5.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/6.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/7.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/8.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/9.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/10.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/11.png", pr.width, pr.height)
    resize_image(f"images/{album.folders[0]}/12.png", pr.width, pr.height)

    source1 =  f"images/{album.folders[0]}/1.png" if album.enables[0][0] else "images/placeholder.png"
    source2 =  f"images/{album.folders[0]}/2.png" if album.enables[0][1] else "images/placeholder.png"
    source3 =  f"images/{album.folders[0]}/3.png" if album.enables[0][2] else "images/placeholder.png"
    source4 =  f"images/{album.folders[0]}/4.png" if album.enables[0][3] else "images/placeholder.png"
    source5 =  f"images/{album.folders[0]}/5.png" if album.enables[0][4] else "images/placeholder.png"
    source6 =  f"images/{album.folders[0]}/6.png" if album.enables[0][5] else "images/placeholder.png"
    source7 =  f"images/{album.folders[0]}/7.png" if album.enables[0][6] else "images/placeholder.png"
    source8 =  f"images/{album.folders[0]}/8.png" if album.enables[0][7] else "images/placeholder.png"
    source9 =  f"images/{album.folders[0]}/9.png" if album.enables[0][8] else "images/placeholder.png"
    source10 =  f"images/{album.folders[0]}/10.png" if album.enables[0][9] else "images/placeholder.png"
    source11 =  f"images/{album.folders[0]}/11.png" if album.enables[0][10] else "images/placeholder.png"
    source12 =  f"images/{album.folders[0]}/12.png" if album.enables[0][11] else "images/placeholder.png"

    column1_layout = [
        [sg.Image(source=source1, key="-IMAGE1-")],
        [sg.Text(f"{album.names[0][0]}", key="-PLAYER1-", font=pr.small_font)],
        [sg.Image(source=source5, key="-IMAGE5-")],
        [sg.Text(f"{album.names[0][4]}", key="-PLAYER5-", font=pr.small_font)],
        [sg.Image(source=source9, key="-IMAGE9-")],
        [sg.Text(f"{album.names[0][8]}", key="-PLAYER9-", font=pr.small_font)],
        [sg.Text(pr.spacement)]
    ]

    column2_layout = [
        [sg.Image(source=source2, key="-IMAGE2-")],
        [sg.Text(f"{album.names[0][1]}", key="-PLAYER2-", font=pr.small_font)],
        [sg.Image(source=source6, key="-IMAGE6-")],
        [sg.Text(f"{album.names[0][5]}", key="-PLAYER6-", font=pr.small_font)],
        [sg.Image(source=source10, key="-IMAGE10-")],
        [sg.Text(f"{album.names[0][9]}", key="-PLAYER10-", font=pr.small_font)],
        [sg.Text(pr.spacement)]
    ]

    column3_layout = [
        [sg.Image(source=source3, key="-IMAGE3-")],
        [sg.Text(f"{album.names[0][2]}", key="-PLAYER3-", font=pr.small_font)],
        [sg.Image(source=source7, key="-IMAGE7-")],
        [sg.Text(f"{album.names[0][6]}", key="-PLAYER7-", font=pr.small_font)],
        [sg.Image(source=source11, key="-IMAGE11-")],
        [sg.Text(f"{album.names[0][10]}", key="-PLAYER11-", font=pr.small_font)],
        [sg.Text(pr.spacement)]
    ]

    column4_layout = [
        [sg.Image(source=source4, key="-IMAGE4-")],
        [sg.Text(f"{album.names[0][3]}", key="-PLAYER4-", font=pr.small_font)],
        [sg.Image(source=source8, key="-IMAGE8-")],
        [sg.Text(f"{album.names[0][7]}", key="-PLAYER8-", font=pr.small_font)],
        [sg.Image(source=source12, key="-IMAGE12-")],
        [sg.Text(f"{album.names[0][11]}", key="-PLAYER12-", font=pr.small_font)],
        [sg.Text(pr.spacement)]
    ]
    
    album_layout = [
        [sg.Text(f"Time: {album.folders[0]}", key="-TIME-")],

        [
            sg.Column(column1_layout, element_justification="c"),
            sg.Column(column2_layout, element_justification="c"),
            sg.Column(column3_layout, element_justification="c"),
            sg.Column(column4_layout, element_justification="c")
        ],
        [sg.Text("Página 1", key="-SHOW PAGE-")],
        [sg.Button("<<<"), sg.Button(">>>")]
    ]

    album_window = sg.Window("Álbum de Figurinhas", album_layout, element_justification='c', font=pr.font)

    while True: 
        event, values = album_window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "<<<":
            page_index = (total_pages + page_index - 1) % total_pages
        elif event == ">>>":
            page_index = (page_index + 1) % total_pages
        
        album_window["-SHOW PAGE-"].update(f"Página {page_index + 1}")
        album_window["-TIME-"].update(f"Time: {album.folders[page_index]}")

        resize_image(f"images/{album.folders[page_index]}/1.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/2.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/3.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/4.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/5.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/6.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/7.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/8.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/9.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/10.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/11.png", pr.width, pr.height)
        resize_image(f"images/{album.folders[page_index]}/12.png", pr.width, pr.height)

        source1 =  f"images/{album.folders[page_index]}/1.png" if album.enables[page_index][0] else "images/placeholder.png"
        source2 =  f"images/{album.folders[page_index]}/2.png" if album.enables[page_index][1] else "images/placeholder.png"
        source3 =  f"images/{album.folders[page_index]}/3.png" if album.enables[page_index][2] else "images/placeholder.png"
        source4 =  f"images/{album.folders[page_index]}/4.png" if album.enables[page_index][3] else "images/placeholder.png"
        source5 =  f"images/{album.folders[page_index]}/5.png" if album.enables[page_index][4] else "images/placeholder.png"
        source6 =  f"images/{album.folders[page_index]}/6.png" if album.enables[page_index][5] else "images/placeholder.png"
        source7 =  f"images/{album.folders[page_index]}/7.png" if album.enables[page_index][6] else "images/placeholder.png"
        source8 =  f"images/{album.folders[page_index]}/8.png" if album.enables[page_index][7] else "images/placeholder.png"
        source9 =  f"images/{album.folders[page_index]}/9.png" if album.enables[page_index][8] else "images/placeholder.png"
        source10 =  f"images/{album.folders[page_index]}/10.png" if album.enables[page_index][9] else "images/placeholder.png"
        source11 =  f"images/{album.folders[page_index]}/11.png" if album.enables[page_index][10] else "images/placeholder.png"
        source12 =  f"images/{album.folders[page_index]}/12.png" if album.enables[page_index][11] else "images/placeholder.png"

        album_window["-IMAGE1-"].update(source=source1)
        album_window["-IMAGE2-"].update(source=source2)
        album_window["-IMAGE3-"].update(source=source3)
        album_window["-IMAGE4-"].update(source=source4)
        album_window["-IMAGE5-"].update(source=source5)
        album_window["-IMAGE6-"].update(source=source6)
        album_window["-IMAGE7-"].update(source=source7)
        album_window["-IMAGE8-"].update(source=source8)
        album_window["-IMAGE9-"].update(source=source9)
        album_window["-IMAGE10-"].update(source=source10)
        album_window["-IMAGE11-"].update(source=source11)
        album_window["-IMAGE12-"].update(source=source12)

        album_window["-PLAYER1-"].update(album.names[page_index][0])
        album_window["-PLAYER2-"].update(album.names[page_index][1])
        album_window["-PLAYER3-"].update(album.names[page_index][2])
        album_window["-PLAYER4-"].update(album.names[page_index][3])
        album_window["-PLAYER5-"].update(album.names[page_index][4])
        album_window["-PLAYER6-"].update(album.names[page_index][5])
        album_window["-PLAYER7-"].update(album.names[page_index][6])
        album_window["-PLAYER8-"].update(album.names[page_index][7])
        album_window["-PLAYER9-"].update(album.names[page_index][8])
        album_window["-PLAYER10-"].update(album.names[page_index][9])
        album_window["-PLAYER11-"].update(album.names[page_index][10])
        album_window["-PLAYER12-"].update(album.names[page_index][11])

    album_window.close()

def show_replicated_window(album: Album, original_window: sg.Window, initial_creditos: int):
    new_creditos = initial_creditos
    rep_values = []
    for replicated in album.replicated:
        rep_values.append(f"Figurinha {replicated.page_index + 1}-{replicated.fig_index + 1} - qtd: {replicated.amount}")
    
    col1_rep = [
        [sg.Listbox(
            values=rep_values, enable_events=True, size=(40,20),
            key="-REPLICATED LIST-"
        )]
    ]

    pages = list(range(1, album.total_pages + 1))
    positions = list(range(1, pr.num_fig_pg + 1))

    col2_rep = [
        [
            sg.Button("Trocar Selecionado"), 
            sg.Text("por:"), 
            sg.Combo(pages, default_value=str(pages[0]), readonly=True, key='page_change'),
            sg.Text("-",font=pr.small_font),
            sg.Combo(positions, default_value=str(positions[0]), readonly=True, key='position_change')
        ],
        [sg.Button("Vender Selecionado")],
        
        [sg.Text("", key="-MSG-")],
        [sg.Text(pr.double_spacement)]
    ]

    replicated_layout = [
        [
            sg.Column(col1_rep),
            sg.VSeparator(),
            sg.Column(col2_rep, vertical_alignment='c', element_justification='c')
        ]
    ]
    
    replicated_window = sg.Window("Figurinhas Repetidas", replicated_layout, font = pr.font)

    msg_last_set = False

    while True:
        event, values = replicated_window.read()

        if msg_last_set:
            replicated_window["-MSG-"].update("")
            msg_last_set = False
        

        if event == sg.WIN_CLOSED:
            break
        elif event == "Vender Selecionado":
            selected_index = replicated_window.Element("-REPLICATED LIST-").Widget.curselection()

            if (len(selected_index) > 0): # Some figurinha is selected
                i = selected_index[0]
                album.replicated[i].amount -= 1
                new_creditos += pr.cr_per_fig
                original_window["-CREDITOS-"].update(f"${new_creditos}")

                if album.replicated[i].amount == 0:
                    album.replicated.pop(i)

                replicated_window["-MSG-"].update(f"Você ganhou ${pr.cr_per_fig}.")
                msg_last_set = True

                # Update Listbox
                rep_values = []

                for replicated in album.replicated:
                    rep_values.append(f"Figurinha {replicated.page_index + 1}-{replicated.fig_index + 1} - qtd: {replicated.amount}")

                replicated_window["-REPLICATED LIST-"].update(values=rep_values)
            else:
                replicated_window["-MSG-"].update("Nenhuma figurinha selecionada.")
                msg_last_set = True
        elif event == "Trocar Selecionado":
            selected_index = replicated_window.Element("-REPLICATED LIST-").Widget.curselection()
            new_fig_infos = [0, 0]

            new_fig_infos[0] = int(values['page_change'])
            new_fig_infos[1] = int(values['position_change'])

            if len(new_fig_infos) != 2:
                replicated_window["-MSG-"].update(f"Má formatação. <pag>-<pos>")
                msg_last_set = True
                continue
        
            new_fig_page_index = -1
            new_fig_fig_index  = -1

            try:
                new_fig_page_index = int(new_fig_infos[0]) - 1
                new_fig_fig_index  = int(new_fig_infos[1]) - 1

                if (new_fig_page_index >= album.total_pages or new_fig_fig_index >= pr.num_fig_pg):
                    raise Exception()
            except:
                replicated_window["-MSG-"].update(f"Má formatação. <pag>-<pos>")
                msg_last_set = True
                continue
            
            if (len(selected_index) > 0): # Some figurinha is selected
                i = selected_index[0]
                
                if album.replicated[i].amount >= pr.figs_to_exchange: # Enough to exchange
                    album.replicated[i].amount -= pr.figs_to_exchange 

                    if album.replicated[i].amount == 0:
                        album.replicated.pop(i)

                    # Obtain requested figurinha
                    if not album.enables[new_fig_page_index][new_fig_fig_index]:
                        album.enables[new_fig_page_index][new_fig_fig_index] = True   
                        replicated_window["-MSG-"].update(f"Figurinha {new_fig_page_index + 1}-{new_fig_fig_index + 1} nova!")
                        msg_last_set = True                     
                    else:
                        replicated_figurinha = Figurinha(new_fig_page_index, new_fig_fig_index)


                        if replicated_figurinha in album.replicated:
                            i = album.replicated.index(replicated_figurinha)
                            album.replicated[i].amount += 1

                        else:
                            album.replicated.append(replicated_figurinha)
                        
                        replicated_window["-MSG-"].update(f"Figurinha {new_fig_page_index + 1}-{new_fig_fig_index + 1} repetida!")
                        msg_last_set = True                     


                    # Update Listbox
                    rep_values = []

                    for replicated in album.replicated:
                        rep_values.append(f"Figurinha {replicated.page_index + 1}-{replicated.fig_index + 1} - qtd: {replicated.amount}")

                    replicated_window["-REPLICATED LIST-"].update(values=rep_values)
                else: # not enough to exchange
                    replicated_window["-MSG-"].update(f"{pr.figs_to_exchange} repetidas iguais para trocar.")
                    msg_last_set = True   
                    
            else:
                replicated_window["-MSG-"].update(f"Nenhuma figurinha selecionada.")
                msg_last_set = True

    replicated_window.close()
    
    return new_creditos