"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_07():
    import pandas as pd
    df = pd.read_csv("files/input/tbl0.tsv" , sep="\t")  # Usamos sep="\t" para archivos TSV
    suma=df.groupby('c1')['c2'].sum()
    return suma

if __name__ == "__main__":
    resultado = pregunta_07()
    if resultado is not None:
        print(f"la suma de la columna `c2` por cada letra de la columna `c1`: {resultado}")

    
    """
    Calcule la suma de la `c2` por cada letra de la `c1` del archivo
    `tbl0.tsv`.

    Rta/
    c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: c2, dtype: int64
    """
