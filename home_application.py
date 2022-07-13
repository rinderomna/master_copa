import PySimpleGUI as sg
from PIL import Image

def resize_image(filename, basewidth, height=None):
    img = Image.open(filename)
    
    if not height:
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    else:
        img = img.resize((basewidth, height), Image.ANTIALIAS)

    img.save(filename)

layout = [
    [sg.Text("O que deseja ver:")],
    [sg.Button("Album"), sg.Button("Figurinhas"), sg.Button("Bozo")],
    [sg.Button("Sair")]
]

window = sg.Window("Master Copa", layout, element_justification='c')

def show_album_window():
    resize_image("images/placeholder.png", 200, 350)
    album_layout = [
        [sg.Text("Página 1")],
        [
            sg.Image(source="images/placeholder.png", key="-IMAGE1-"),
            sg.Image(source="images/placeholder.png", key="-IMAGE2-"),
            sg.Image(source="images/placeholder.png", key="-IMAGE3-") 
        ],

        [
            sg.Image(source="images/placeholder.png", key="-IMAGE4-"),
            sg.Image(source="images/placeholder.png", key="-IMAGE5-"),
            sg.Image(source="images/placeholder.png", key="-IMAGE6-") 
        ]
    ]

    album_window = sg.Window("Album de Figurinhas", album_layout, element_justification='c')

    while True: 
        event, values = album_window.read()
        if event == sg.WIN_CLOSED:
          break

    album_window.close()

while True: 
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    elif event == "Album":
        show_album_window()

window.close()