"""
Realizar un programa que permite actualizar una lista de precios
en forma masiva, ingresando un porcentaje de incremento.
Debera:
1- Mediante una funcion generarOriginal crear el archivo original se
    llama precios.csv y fue generado utilizando el siguiente diseno de registro:
    • Código (entero de 4 digitos)
    • Precio (valor real)
    • Descripción
    Se dispone un registro por producto, y los campos son separados por ;
2- Desarrollar la funcion actualizarPrecios que recibe el nombre del archivo
    original y el porcentaje de incremento, y se encarga de recorrer el archivo y actualizar
    los precios correspondientes. Para ello se creara el archivo Precios_actualizados.csv.
3- Al finalizar informar la cantidad de productos comercializados, y el precio promedio
   con el incremento aplicado
RESOLVER VALIDANDO EL INGRESO DE LOS DATOS,  y MANEJANDO
CORRECTAMENTE LAS EXCEPCIONES

-------------------------------------------------------

Se dispone de un archivo medicamentos.csv que contiene codigo, precio, rubro y  stock de cada uno de los medicamentos.
Los rubros que trabajan son : PEDIATRICO, ODONTOLOGIA , VTALIBRE
El formato de cada registro sera:
CODIGO;PRECIO;RUBRO;STOCK finalizando con un enter o \n
 
1- Generar el archivo de muestra con 10 registros aproximadamente
 
2 - Se actualizara de forma masiva el precio en un 25% los medicamentos
del rubro VTALIBRE, y se actualizara el archivo en
un nuevo medicamentos_actu.csv
 
3- Obtener e informar el precio Maximo (Unico) del medicamento del RUBRO ODONTOLOGIA
 
4- Generar un archivo STOCKBAJO.txt que contenga los codigos de los productos con stock menor a 100 unidades
y la cantidad de stock actual
 
5- Generar un diccionario con los datos que se obtienen de STOCKBAJO
 
IMPORTANTE!!!! EL CODIGO DEBERA ESTAR CORRECTAMENTE MODULARIZADO
 
"""