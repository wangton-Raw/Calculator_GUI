
import PySimpleGUI as sg

# create calculator layout 
layout = [[sg.Text('Enter two numbers')],
            [sg.Input(size=(5,1)), sg.Input(size=(5,1)), sg.Input(size=(5,1))],
            [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
            [sg.Button('='), sg.Button('Clear')]]   # end of layout


# Create the window
window = sg.Window("Demotheone", layout, size = (600,300), resizable = True)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()

