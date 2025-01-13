"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import fileinput
import glob

def load_input(input_directory):
    #se modifico la funcion para que agregara solo las dos primeras columnas en una lista, y agregara todas
    #las listas en una tupla
    """Funcion load_input"""
    sequence = []
    files = glob.glob(f"{input_directory}/*")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append(line.split('\t')[:2])
    return sequence

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

def reducer(sequence):
    """Reducer"""
    result = {}
    for key, value in sequence:
        if key not in result.keys():
            result[key] = []
        result[key].append(int(value))
    return list(result.items())

def filter(sequence):
    #filtra los max y min de cada letra y los devuelve en una lista de tuplas
    new_sequence = [
        (key, max(value), min(value))
        for key,value in sequence
    ]
    return new_sequence

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    sequence = load_input('files\input')
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    sequence = filter(sequence)

    return sequence

pregunta_05()