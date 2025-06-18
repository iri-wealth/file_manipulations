import FreeSimpleGUI as sg
from zip_creator import make_archive

# Create the window layout
layout = [
    [sg.Text("Select files to compress:")],
    [sg.Input(key="-FILES-"), sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse("Choose")],
    [sg.Button("Compress"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("File Compressor", layout)

# Event loop
while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    
    if event == "Compress":
        filepaths = values["-FILES-"].split(";")
        folder = values["-FOLDER-"]
        
        try:
            archive_path = make_archive(filepaths, folder)
            sg.popup(f"Archive created successfully!\nSaved at: {archive_path}")
        except Exception as e:
            sg.popup_error(f"An error occurred: {str(e)}")

window.close()