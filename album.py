import PySimpleGUI as sg
from PIL import Image
from param import Param as pr

class Album:
    def __init__(self):
        self.folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  
        self.total_pages = len(self.folders)
        
        disables = [False] * 12

        self.unables = []

        for i in range(self.total_pages):
            self.unables.append(list(disables))

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

    source1 =  f"images/{album.folders[0]}/1.png" if album.unables[0][0] else "images/placeholder.png"
    source2 =  f"images/{album.folders[0]}/2.png" if album.unables[0][1] else "images/placeholder.png"
    source3 =  f"images/{album.folders[0]}/3.png" if album.unables[0][2] else "images/placeholder.png"
    source4 =  f"images/{album.folders[0]}/4.png" if album.unables[0][3] else "images/placeholder.png"
    source5 =  f"images/{album.folders[0]}/5.png" if album.unables[0][4] else "images/placeholder.png"
    source6 =  f"images/{album.folders[0]}/6.png" if album.unables[0][5] else "images/placeholder.png"
    source7 =  f"images/{album.folders[0]}/7.png" if album.unables[0][6] else "images/placeholder.png"
    source8 =  f"images/{album.folders[0]}/8.png" if album.unables[0][7] else "images/placeholder.png"
    source9 =  f"images/{album.folders[0]}/9.png" if album.unables[0][8] else "images/placeholder.png"
    source10 =  f"images/{album.folders[0]}/10.png" if album.unables[0][9] else "images/placeholder.png"
    source11 =  f"images/{album.folders[0]}/11.png" if album.unables[0][10] else "images/placeholder.png"
    source12 =  f"images/{album.folders[0]}/12.png" if album.unables[0][11] else "images/placeholder.png"

    column1_layout = [
        [sg.Image(source=source1, key="-IMAGE1-")],
        [sg.Text("Jogador 1")],
        [sg.Image(source=source5, key="-IMAGE5-")],
        [sg.Text("Jogador 5")],
        [sg.Image(source=source9, key="-IMAGE9-")],
        [sg.Text("Jogador 9")]
    ]

    column2_layout = [
        [sg.Image(source=source2, key="-IMAGE2-")],
        [sg.Text("Jogador 2")],
        [sg.Image(source=source6, key="-IMAGE6-")],
        [sg.Text("Jogador 6")],
        [sg.Image(source=source10, key="-IMAGE10-")],
        [sg.Text("Jogador 10")]
    ]

    column3_layout = [
        [sg.Image(source=source3, key="-IMAGE3-")],
        [sg.Text("Jogador 3")],
        [sg.Image(source=source7, key="-IMAGE7-")],
        [sg.Text("Jogador 7")],
        [sg.Image(source=source11, key="-IMAGE11-")],
        [sg.Text("Jogador 11")]
    ]

    column4_layout = [
        [sg.Image(source=source4, key="-IMAGE4-")],
        [sg.Text("Jogador 4")],
        [sg.Image(source=source8, key="-IMAGE8-")],
        [sg.Text("Jogador 8")],
        [sg.Image(source=source12, key="-IMAGE12-")],
        [sg.Text("Jogador 12")]
    ]
    


    album_layout = [
        [sg.Text("Página 1", key="-SHOW PAGE-")],

        [
            sg.Column(column1_layout, element_justification="c"),
            sg.Column(column2_layout, element_justification="c"),
            sg.Column(column3_layout, element_justification="c"),
            sg.Column(column4_layout, element_justification="c")
        ],

        [sg.Button("<<<"), sg.Button(">>>")]
    ]

    album_window = sg.Window("Album de Figurinhas", album_layout, element_justification='c', font=pr.font)

    while True: 
        event, values = album_window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event == "<<<":
            page_index = (total_pages + page_index - 1) % total_pages
        elif event == ">>>":
            page_index = (page_index + 1) % total_pages
        
        album_window["-SHOW PAGE-"].update(f"Página {page_index + 1}")

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

        source1 =  f"images/{album.folders[page_index]}/1.png" if album.unables[page_index][0] else "images/placeholder.png"
        source2 =  f"images/{album.folders[page_index]}/2.png" if album.unables[page_index][1] else "images/placeholder.png"
        source3 =  f"images/{album.folders[page_index]}/3.png" if album.unables[page_index][2] else "images/placeholder.png"
        source4 =  f"images/{album.folders[page_index]}/4.png" if album.unables[page_index][3] else "images/placeholder.png"
        source5 =  f"images/{album.folders[page_index]}/5.png" if album.unables[page_index][4] else "images/placeholder.png"
        source6 =  f"images/{album.folders[page_index]}/6.png" if album.unables[page_index][5] else "images/placeholder.png"
        source7 =  f"images/{album.folders[page_index]}/7.png" if album.unables[page_index][6] else "images/placeholder.png"
        source8 =  f"images/{album.folders[page_index]}/8.png" if album.unables[page_index][7] else "images/placeholder.png"
        source9 =  f"images/{album.folders[page_index]}/9.png" if album.unables[page_index][8] else "images/placeholder.png"
        source10 =  f"images/{album.folders[page_index]}/10.png" if album.unables[page_index][9] else "images/placeholder.png"
        source11 =  f"images/{album.folders[page_index]}/11.png" if album.unables[page_index][10] else "images/placeholder.png"
        source12 =  f"images/{album.folders[page_index]}/12.png" if album.unables[page_index][11] else "images/placeholder.png"

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

    album_window.close()

def show_replicated_window(album: Album, original_window: sg.Window):
    values = []
    for replicated in album.replicated:
        values.append(f"Figurinha {replicated.page_index + 1}-{replicated.fig_index + 1} - qtd: {replicated.amount}")
    
    replicated_layout = [
        [sg.Listbox(
            values=values, enable_events=True, size=(40,20),
            key="-REPLICATED LIST-"
        )]
    ]
    
    replicated_window = sg.Window("Figurinhas Repetidas", replicated_layout, font = pr.font)

    while True:
        event, values = replicated_window.read()

        if event == sg.WIN_CLOSED:
            break

    replicated_window.close()

