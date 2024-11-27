"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_06():
    import pandas as pd
    df = pd.read_csv("files/input/tbl1.tsv" , sep="\t")  # Usamos sep="\t" para archivos TSV
    lista=sorted(df['c4'].str.upper().unique())
    return lista

if __name__ == "__main__":
    resultado = pregunta_06()
    if resultado is not None:
        print(f"los valores unicos de la columna `c4` son: {resultado}")


    """
    Retorne una lista con los valores unicos de la columna `c4` del archivo
    `tbl1.csv` en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
