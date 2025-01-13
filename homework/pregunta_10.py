"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

def load_input(input_directory):
    """Funcion load_input"""
    sequence = []
    files = glob.glob(f"{input_directory}/*")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append(line.split('\t'))

    return sequence

def pre_processing(sequence):
    #result = []
    #for line in sequence:
    #    last_line = line[4].strip().split(',')
    #    n_letters = line[3].split(',')
    #    result.append((line[0], len(n_letters), len(last_line)))
    return [(line[0], len(line[3].split(',')), len(line[4].strip().split(','))) for line
            in sequence]

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    sequence = load_input('files/input')
    sequence = pre_processing(sequence)


    return sequence
pregunta_10()