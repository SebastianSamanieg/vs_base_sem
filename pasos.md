# Paso a paso generación del informe:

1. Se debe crear en las dos bases una columna nueva que sea la concatenación de las columnas: 'CUENTA','N_doc','Importe_ML_' y se llamara base 'Codigo'
2. En la base actual se debe crear otra columna llamada 'Cruce' y en esa columna se traera los valores de 'Codigo' de la base pasada que sean iguales a los valore de 'Codigo' de la base actual, si no crucan se debe poner 'Nuevo'
3. Del nuevo dataframe creado se debe contar todos los valores de la columna 'Cruce' que se hallan identificado como 'Nuevo'