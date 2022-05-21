import PySimpleGUI as sg
import math

sg.theme('DarkAmber')

layout = [
    [sg.Text('Calculate Volume of Sphere')],
    [sg.InputText(key = '-NAME-')],
    [sg.InputText(key = '-RADIUS-')],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Fred\'s First Python GUI Project', layout)

event,values = window.read()

window.close()

def calculate_sphere_volume(radius):
    volume = (4/3)*math.pi*(radius**3)
    return volume

float_radius = float(values['-RADIUS-'])
volume_of_sphere = calculate_sphere_volume(float_radius)

sg.popup('You entered: ', values['-NAME-'], ' and a radius of ', values['-RADIUS-'])
sg.popup('There volume of sphere of radius: ', values['-RADIUS-'], ' is ', volume_of_sphere)