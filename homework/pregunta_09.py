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
    for key,_ in sequence:
        if key not in result.keys():
            result[key] = 0
        result[key] += 1
    return dict(sorted(result.items()))

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    sequence = load_input('files\input')
    sequence = line_processing(sequence)
    sequence = mapper(sequence)
    sequence = reducer(sequence)

    return sequence
pregunta_09()