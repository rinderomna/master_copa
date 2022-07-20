import PySimpleGUI as sg
from PIL import Image
from param import Param as pr

class Album:
    def __init__(self):
        self.folders = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  
        self.total_pages = len(self.folders)
        
        disables = [False] * 6

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
    resize_image("images/placeholder.png", 200, 350)

    total_pages = album.total_pages
    page_index = 0 # page_index = page_number - 1 [from 0 to (total_pages - 1)]

    resize_image(f"images/1/1.png", 200, 350)
    resize_image(f"images/1/2.png", 200, 350)
    resize_image(f"images/1/3.png", 200, 350)
    resize_image(f"images/1/4.png", 200, 350)
    resize_image(f"images/1/5.png", 200, 350)
    resize_image(f"images/1/6.png", 200, 350)

    source1 =  "images/1/1.png" if album.unables[0][0] else "images/placeholder.png"
    source2 =  "images/1/2.png" if album.unables[0][1] else "images/placeholder.png"
    source3 =  "images/1/3.png" if album.unables[0][2] else "images/placeholder.png"
    source4 =  "images/1/4.png" if album.unables[0][3] else "images/placeholder.png"
    source5 =  "images/1/5.png" if album.unables[0][4] else "images/placeholder.png"
    source6 =  "images/1/6.png" if album.unables[0][5] else "images/placeholder.png"

    album_layout = [
        [sg.Text("Página 1", key="-SHOW PAGE-")],
        [
            sg.Image(source=source1, key="-IMAGE1-"),
            sg.Image(source=source2, key="-IMAGE2-"),
            sg.Image(source=source3, key="-IMAGE3-") 
        ],

        [
            sg.Image(source=source4, key="-IMAGE4-"),
            sg.Image(source=source5, key="-IMAGE5-"),
            sg.Image(source=source6, key="-IMAGE6-") 
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

        resize_image(f"images/{album.folders[page_index]}/1.png", 200, 350)
        resize_image(f"images/{album.folders[page_index]}/2.png", 200, 350)
        resize_image(f"images/{album.folders[page_index]}/3.png", 200, 350)
        resize_image(f"images/{album.folders[page_index]}/4.png", 200, 350)
        resize_image(f"images/{album.folders[page_index]}/5.png", 200, 350)
        resize_image(f"images/{album.folders[page_index]}/6.png", 200, 350)

        source1 =  f"images/{album.folders[page_index]}/1.png" if album.unables[page_index][0] else "images/placeholder.png"
        source2 =  f"images/{album.folders[page_index]}/2.png" if album.unables[page_index][1] else "images/placeholder.png"
        source3 =  f"images/{album.folders[page_index]}/3.png" if album.unables[page_index][2] else "images/placeholder.png"
        source4 =  f"images/{album.folders[page_index]}/4.png" if album.unables[page_index][3] else "images/placeholder.png"
        source5 =  f"images/{album.folders[page_index]}/5.png" if album.unables[page_index][4] else "images/placeholder.png"
        source6 =  f"images/{album.folders[page_index]}/6.png" if album.unables[page_index][5] else "images/placeholder.png"

        album_window["-IMAGE1-"].update(source=source1)
        album_window["-IMAGE2-"].update(source=source2)
        album_window["-IMAGE3-"].update(source=source3)
        album_window["-IMAGE4-"].update(source=source4)
        album_window["-IMAGE5-"].update(source=source5)
        album_window["-IMAGE6-"].update(source=source6)

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

