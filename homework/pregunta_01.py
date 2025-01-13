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
            sequence.append((fileinput.filename(), line))
    return sequence

def selecter (sequence):
    'selecciona la columna objetivo y la agrega a una nueva tupla'
    sum_column = []
    for i in sequence:
        new_line = i[1].split("\t")
        sum_column.append(int(new_line[1]))
    return sum_column

def pregunta_01():
    """
    Retorne la suma de la segunda columna.
    Rta/
    214

    """
    sequence = load_input("files/input")
    sequence = selecter (sequence)
    sequence = sum(sequence)

    return sequence

pregunta_01()