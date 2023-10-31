import pandas as pd

class functions:

    def __init__(self):
        self.data_df = None  # DataFrame para almacenar los datos

    @staticmethod
    def crear_codigo(fila):
        """
        Crea un código a partir de las columnas 'CUENTA', 'N_doc' y 'Importe_ML_' en la fila.
        """
        return f"{fila['CUENTA']}{fila['N_doc']}{fila['Importe_ML_']}"

    @staticmethod
    def leer_hoja_excel(archivo, hoja):
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
        total_valor = registros_no_cruzados['Importe_ML_'].sum()
        cantidad_registros = len(registros_no_cruzados)

        print(f"Registros que no cruzan: {cantidad_registros}")
        print(f"Total Valor: {total_valor}")

        # Crear un DataFrame con las columnas 'Factura nueva' y 'Valor'
        df_resultado = pd.DataFrame({'Factura nueva': [cantidad_registros], 'Valor': [total_valor]})

        print(df_resultado)
