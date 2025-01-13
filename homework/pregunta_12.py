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
            sequence.append(line.split('\t')[:])
    return sequence

def line_preprocessing(sequence):
    #result = []
    #for letter,_,_,_,number in sequence:
    #    result.append((letter,number))
    return [(letter,number.strip()) for letter,_,_,_,number in sequence]
        


def dict_keys(sequence):
    result = {}
    for key,line in sequence:
        if key not in result.keys():
            result[key] = 0
        for number in line.split(','):
            result[key] += int(number[4:])

    return dict(sorted(result.items()))

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    sequence = load_input('files\input')
    sequence = line_preprocessing(sequence)
    sequence = dict_keys(sequence)

    return sequence
pregunta_12()