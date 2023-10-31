# En el archivo functions.py
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

    def obtener_registros_que_no_cruzan(self, base_pasada_file, base_actual_file, output_file):
        """
        Obtiene registros de la base actual que no cruzan con la base pasada para todas las hojas en ambos archivos y
        guarda un resumen y el detalle en hojas separadas del archivo de salida.
        Args:
            base_pasada_file (str): Ruta al archivo de la base pasada.
            base_actual_file (str): Ruta al archivo de la base actual.
            output_file (str): Nombre del archivo de salida.
        """
        base_pasada = pd.ExcelFile(base_pasada_file)
        base_actual = pd.ExcelFile(base_actual_file)
        hojas_pasada = base_pasada.sheet_names
        hojas_actual = base_actual.sheet_names

        resumen_df = pd.DataFrame(columns=['Facturas nuevas en', 'Cantidad', 'Total Valor'])

        with pd.ExcelWriter(output_file, engine='xlsxwriter') as writer:
            writer.book.use_zip64()  # Para permitir hojas grandes

            for hoja in hojas_pasada:
                if hoja in hojas_actual:
                    base_pasada_df = self.leer_hoja_excel(base_pasada_file, hoja)
                    base_actual_df = self.leer_hoja_excel(base_actual_file, hoja)

                    if base_pasada_df is not None and base_actual_df is not None:
                        base_pasada_df['Codigo'] = base_pasada_df.apply(self.crear_codigo, axis=1)
                        base_actual_df['Codigo'] = base_actual_df.apply(self.crear_codigo, axis=1)

                        registros_no_cruzados = base_actual_df[~base_actual_df['Codigo'].isin(base_pasada_df['Codigo'])]
                        total_valor = registros_no_cruzados['Importe_ML_'].sum()
                        cantidad_registros = len(registros_no_cruzados)

                        resumen_df = pd.concat([resumen_df, pd.DataFrame({'Facturas nuevas en': [hoja], 'Cantidad': [cantidad_registros], 'Total Valor': [total_valor]})], ignore_index=True)

                        # Guardar los detalles en una hoja separada
                        registros_no_cruzados.to_excel(writer, sheet_name=f'Detalle_{hoja[:20]}', index=False)

            resumen_df.to_excel(writer, sheet_name='Resumen', index=False)
