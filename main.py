import PySimpleGUI as sg
from zip_creator import make_archive, extract_archive

# Create the window layout
layout = [
    [sg.Text("Select files to compress:")],
    [sg.Input(key="-FILES-"), sg.FilesBrowse("Choose")],
    [sg.Text("Select destination folder:")],
    [sg.Input(key="-FOLDER-"), sg.FolderBrowse("Choose")],
    [sg.Button("Compress")],
    [sg.Text("Select zip file to extract:")],
    [sg.Input(key="-ZIP-"), sg.FileBrowse("Choose", file_types=(("ZIP Files", "*.zip"),))],
    [sg.Text("Select extraction destination:")],
    [sg.Input(key="-EXTRACT-FOLDER-"), sg.FolderBrowse("Choose")],
    [sg.Button("Extract")],
    [sg.Button("Exit")]
]

# Create the window
window = sg.Window("File Compressor/Extractor", layout)

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
            sg.popup_error(f"An error occurred during compression: {str(e)}")

    if event == "Extract":
        zip_path = values["-ZIP-"]
        extract_folder = values["-EXTRACT-FOLDER-"]
        
        try:
            extracted_path = extract_archive(zip_path, extract_folder)
            sg.popup(f"Files extracted successfully!\nExtracted to: {extracted_path}")
        except Exception as e:
            sg.popup_error(f"An error occurred during extraction: {str(e)}")

window.close()