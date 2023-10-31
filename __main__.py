import pandas as pd
from functions import functions

if __name__ == "__main__":
    functions_instance = functions()
    output_file = 'resumen_vs.xlsx'  # Nombre del archivo de salida
    resumen = functions_instance.obtener_registros_que_no_cruzan('base_pasada.xlsx', 'base_actual.xlsx', output_file)