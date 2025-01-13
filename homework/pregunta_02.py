"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob
import fileinput

def load_input(input_directory):
    """Funcion load_input"""
    sequence = []
    files = glob.glob(f"{input_directory}/*")
    with fileinput.input(files=files) as f:
        for line in f:
            sequence.append(line)
    return sequence

def filter(sequence):
    'filtra solo la primera columna del archivo en una nueva lista'
    new_sequence = [
        (line.split('\t')[0],1)
        for line in sequence
    ]
    return new_sequence

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

def reducer(sequence):
    """Reducer"""
    result = {}
    for key,value in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += value
    return list(result.items())

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]
    """
    
    sequence = load_input('files/input')
    sequence = filter(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)

    return sequence
pregunta_02()