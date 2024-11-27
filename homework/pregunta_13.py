"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en los archivos `tbl0.tsv`, `tbl1.tsv` y 
`tbl2.tsv`. En este laboratorio solo puede utilizar las funciones y 
librerias de pandas para resolver las preguntas.
"""


def pregunta_13():
    import pandas as pd
    df0 = pd.read_csv("files/input/tbl0.tsv", sep="\t")
    df2 = pd.read_csv("files/input/tbl2.tsv", sep="\t")
    
    # Unir 'df0' con 'df2' usando la columna 'c0' como clave
    df_merged = pd.merge(df0, df2, on='c0', how='inner')
    
    # Agrupar por 'c1' de 'df0' y sumar la columna 'c5b' de 'df2'
    result = df_merged.groupby('c1')['c5b'].sum()
    
    return result

if __name__ == "__main__":
    # Obtener el resultado
    resultado = pregunta_13()
    
    if resultado is not None:
        print(resultado)


    """
    Si la columna `c0` es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`,
    compute la suma de `tbl2.c5b` por cada valor en `tbl0.c1`.

    Rta/
    c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: c5b, dtype: int64
    """
