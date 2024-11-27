"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_01():
    import pandas as pd
    df = pd.read_csv("files/input/tbl0.tsv" , sep="\t")  # Usamos sep="\t" para archivos TSV
    return len(df)

if __name__ == "__main__":
    resultado = pregunta_01()
    if resultado is not None:
        print(f"El número de filas en la tabla es: {resultado}")

    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
