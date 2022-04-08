
import PySimpleGUI as sg

# create calculator layout
layout = [[sg.Text('Enter two numbers')],
          [sg.InputText('')],
          [sg.InputText('')],
          [sg.Button('+'), sg.Button('-'), sg.Button('*'), sg.Button('/')],
          [sg.Button('='), sg.Button('Clear')]]



# Create the window
<<<<<<< HEAD
window = sg.Window("Demotheone", layout, size = (500,300), resizable = True)
=======
window = sg.Window("Demo2", layout, size = (500,300), resizable = True)
>>>>>>> c54081896a8d6547e29a97aa7d24702f15a36f32

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

    # Do something based on the ev

window.close()

