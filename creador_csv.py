import pandas as pd

# Dataframe es la información basica con el nombre de las piezas y los centimetros para poder usar el excel

Data = {
    "Piezas": ["Pata","Tablero" ,"Mesa","Estante","Panel lateral"],
    "Centimetros": [40, 120, 60, 30, 180]
}

pf = pd.DataFrame(Data)

# Exportar el DataFrame en un archivo CSV

pf.to_excel("muebles_medidas.xlsx", index=False)
