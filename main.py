import FreeSimpleGUI as sg #widget creation for GUI, third-party library
label1 = sg.Text(text='Select files to compress:')
input1 = sg.Input()
choose_button1 = sg.FilesBrowse('Choose files')

label2 = sg.Text(text='Select destination folder:')
input2 = sg.Input()
choose_button2 = sg.FolderBrowse('Choose folder')


compress_button = sg.Button('Compress')
window = sg.Window('File Compressor',
                    layout=[[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [compress_button]])

window.read()
window.close()
