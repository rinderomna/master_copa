import PySimpleGUI as sg
from PIL import Image

from album import Album

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

def show_album_window(album: Album):
    resize_image("images/placeholder.png", 200, 350)

    total_pages = 10
    page_index = 0 # page_index = page_number - 1 [from 0 to (total_pages - 1)]

    resize_image(f"images/1/1.png", 200, 350)
    resize_image(f"images/1/2.png", 200, 350)
    resize_image(f"images/1/3.png", 200, 350)
    resize_image(f"images/1/4.png", 200, 350)
    resize_image(f"images/1/5.png", 200, 350)
    resize_image(f"images/1/6.png", 200, 350)

    album_layout = [
        [sg.Text("Página 1", key="-SHOW PAGE-")],
        [
            sg.Image(source="images/1/1.png", key="-IMAGE1-"),
            sg.Image(source="images/1/2.png", key="-IMAGE2-"),
            sg.Image(source="images/1/3.png", key="-IMAGE3-") 
        ],

        [
            sg.Image(source="images/1/4.png", key="-IMAGE4-"),
            sg.Image(source="images/1/5.png", key="-IMAGE5-"),
            sg.Image(source="images/1/6.png", key="-IMAGE6-") 
        ],
        [sg.Button("<<<"), sg.Button(">>>")]
    ]

    album_window = sg.Window("Album de Figurinhas", album_layout, element_justification='c')

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
        album_window["-IMAGE1-"].update(source=f"images/{album.folders[page_index]}/1.png")
        album_window["-IMAGE2-"].update(source=f"images/{album.folders[page_index]}/2.png")
        album_window["-IMAGE3-"].update(source=f"images/{album.folders[page_index]}/3.png")
        album_window["-IMAGE4-"].update(source=f"images/{album.folders[page_index]}/4.png")
        album_window["-IMAGE5-"].update(source=f"images/{album.folders[page_index]}/5.png")
        album_window["-IMAGE6-"].update(source=f"images/{album.folders[page_index]}/6.png")

    album_window.close()

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