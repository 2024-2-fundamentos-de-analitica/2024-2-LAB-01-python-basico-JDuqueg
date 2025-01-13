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
            sequence.append(line.split('\t')[1:4])
    return sequence

def dict_keys(sequence):
    result = {}
    for line in sequence:
        for key in line[2]:
            if key == ',':
                continue
            if key not in result.keys():
                result[key] = 0
            result[key] += int(line[0])
    return dict(sorted(result.items()))

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    sequence = load_input('files/input')
    sequence = dict_keys(sequence)

    return sequence
pregunta_11()