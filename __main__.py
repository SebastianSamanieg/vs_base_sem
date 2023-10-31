import pandas as pd
from functions import functions

if __name__ == "__main__":

    # Creamos una instancia de la clase functions
    functions = functions()
 
    functions.obtener_registros_que_no_cruzan('base_pasada.xlsx', 'base_actual.xlsx', 'Octubre', 'Octubre')



    # df = pd.read_excel('base_actual.xlsx','Octubre')
    # print(df.head())
    