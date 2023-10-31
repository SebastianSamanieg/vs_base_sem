import pandas as pd

class functions:

    def __init__(self):
        print("Hola")
        self.data_df = None  # DataFrame para almacenar los datos

    @staticmethod
    def crear_codigo(fila):
        print("Hola")
        """
        Crea un código a partir de las columnas 'CUENTA', 'N_doc' y 'Importe_ML_' en la fila.
        """
        return f"{fila['CUENTA']}{fila['N_doc']}{fila['Importe_ML_']}"

    @staticmethod
    def leer_hoja_excel(archivo, hoja):
        print("Hola")
        """
        Lee una hoja de un archivo Excel y devuelve un DataFrame.
        Args:
            archivo (str): Ruta al archivo Excel.
            hoja (str): Nombre de la hoja que se va a leer.
        Returns:
            pd.DataFrame: DataFrame con los datos de la hoja.
        """
        try:
            return pd.read_excel(archivo, sheet_name=hoja)
        except Exception as e:
            print(f"Error al leer la hoja '{hoja}' del archivo '{archivo}': {e}")
            return None

    def obtener_registros_que_no_cruzan(self, base_pasada_file, base_actual_file, sheet_name_pasada, sheet_name_actual):
        """
        Obtiene registros de la base actual que no cruzan con la base pasada.
        Args:
            base_pasada_file (str): Ruta al archivo de la base pasada.
            base_actual_file (str): Ruta al archivo de la base actual.
            sheet_name_pasada (str): Nombre de la hoja en la base pasada.
            sheet_name_actual (str): Nombre de la hoja en la base actual.
        Returns:
            pd.DataFrame: DataFrame con registros que no cruzan entre la base pasada y la base actual.
        """
        base_pasada_df = self.leer_hoja_excel(base_pasada_file, sheet_name_pasada)
        base_actual_df = self.leer_hoja_excel(base_actual_file, sheet_name_actual)

        if base_pasada_df is None or base_actual_df is None:
            return None

        base_pasada_df['Codigo'] = base_pasada_df.apply(self.crear_codigo, axis=1)
        base_actual_df['Codigo'] = base_actual_df.apply(self.crear_codigo, axis=1)

        registros_no_cruzados = base_actual_df[~base_actual_df['Codigo'].isin(base_pasada_df['Codigo'])]

        print("Hola")

        # Esta fracción de codigo descarga el detalle del dataframe
        # try:
        #     registros_no_cruzados.to_excel(output_file, index=False)
        #     print(f"Registros que no cruzan guardados en '{output_file}'")
        # except Exception as e:
        #     print(f"Error al guardar los registros que no cruzan: {e}")  