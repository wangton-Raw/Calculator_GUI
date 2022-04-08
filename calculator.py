
import PySimpleGUI as sg

# create calculator layout
layout = [[sg.Text('Enter two numbers')],
          [sg.InputText('')],
          [sg.InputText('')],
          [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
          [sg.Button('='), sg.Button('Clear')]]



# Create the window
window = sg.Window("Demo2", layout, size = (500,300), resizable = True)

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    # Do something based on the ev

window.close()

