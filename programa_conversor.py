import pandas as pd

def cm_a_pulgadas(cm):
    return cm / 2.54

# Leer el archivo excel con las medidas en centímetros
df = pd.read_excel("muebles_medidas.xlsx")

# Crear una nueva columna con las medidas convertidas a pulgadas
df["Pulgadas"] = df["Centimetros"].apply(cm_a_pulgadas) 

# Exportar el DataFrame actualizado a un nuevo archivo Excel
df.to_excel("muebles_medidas_pulgadas.xlsx", index=False)   