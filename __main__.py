import pandas as pd
from functions import functions

if __name__ == "__main__":

    # Creamos una instancia de la clase functions
    # functions = functions()
 
    df = pd.read_excel('base_actual.xlsx','Octubre')
    print(df.head())
    