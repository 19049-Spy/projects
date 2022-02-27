import PySimpleGUI as sg
array = []
layout = [
    [sg.Text('ToDo')],
    [sg.InputText('Sem pridejte Vasi polozku', key='input'), sg.Button(button_text='Pridat', key="pridat")],
    [sg.Listbox(values=array, size=(43, 10), key="polozky"), sg.Button('Odstranit')],
]

window = sg.Window('To-Do list v GUI', layout)
while True:
    event, values = window.Read()
    if event == "pridat":
        array.append(values['input'])
        window.FindElement('polozky').Update(values=array)
        window.FindElement('pridat').Update("Pridat")
    elif event == "Odstranit":
        array.remove(values["polozky"][0])
        window.FindElement('polozky').Update(values=array)
    elif event == None:
        break
window.Close()