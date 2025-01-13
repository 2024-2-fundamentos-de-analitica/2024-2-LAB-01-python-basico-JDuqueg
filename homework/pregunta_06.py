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
            sequence.append(line.split('\t')[4].strip())
    return sequence

def line_processing(sequence):
    #esta funcion procesa cada item de la lista y devuelve listas con los elementos para
    #crear el diccionario
    new_sequence = []
    for line in sequence:
        items = line.split(',')
        new_sequence.extend(items)

    return new_sequence 

def mapper(sequence):
    """Mapper"""
    return [(key, int(value)) for line in sequence for key,value in [line.split(':')]]

def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += value
    return list(result.items())

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = []
        result[key].append(value)
    return list(result.items())

def filter(sequence):
    #filtra los max y min de cada letra y los devuelve en una lista de tuplas
    new_sequence = [
        (key, min(value), max(value))
        for key,value in sequence
    ]
    return new_sequence

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    sequence = load_input('files\input')
    sequence = line_processing(sequence)
    sequence = mapper(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    sequence = filter(sequence)

    return sequence

pregunta_06()