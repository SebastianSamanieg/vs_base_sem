# Guía de uso del Script

Este script está diseñado para analizar dos bases de datos semanales en formato Excel y encontrar registros que no se cruzan entre ellas. Asegúrate de seguir estos pasos antes de utilizar el script:

## Pasos Previos

1. **Limpieza de las Bases Semanales**:
   - Antes de utilizar el script, asegúrate de limpiar las bases semanales eliminando las hojas que no sigan el formato necesario.
   
2. **Asegurarse del Formato de Columnas**:
   - Verifica que todas las hojas que se van a analizar tengan las siguientes columnas con los nombres indicados:
     - CUENTA
     - Nombre_cuenta
     - VP
     - BP
     - N_doc
     - Cl
     - Mon
     - Importe_MD_
     - Importe_ML_
     - Referencia
     - Día
     - Fecha_Base_
     - Fe_Contab_
     - Compens
     - Fecha_pago_
     - Doc_comp
     - Texto
     - Nombre_Recept_pago
     - Clv_ref_3
     - Cta_CP
     - Lib_mayor
     - Bco_prp
     - Usuario
     - Texto_cab_documento
     - TpBc
     - Clave_banco
     - CONCEPTO
     - MES

   3. En la carpeta my_app se deben dejar los dos archivos excel


# Paso a paso generación del informe:
1. Se debe crear en las dos bases una columna nueva que sea la concatenación de las columnas: 'CUENTA','N_doc','Importe_ML_' y se llamara base 'Codigo'
2. En la base actual se debe crear otra columna llamada 'Cruce' y en esa columna se traera los valores de 'Codigo' de la base pasada que sean iguales a los valore de 'Codigo' de la base actual, si no crucan se debe poner 'Nuevo'
3. Del nuevo dataframe creado se debe contar todos los valores de la columna 'Cruce' que se hallan identificado como 'Nuevo'