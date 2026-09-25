import functions

import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

window1 = sg.Window("My todo app", layout=[[label], [input_box, add_button]])
window1.read()
window1.close()