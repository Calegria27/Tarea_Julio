import timee

st = time.time()

array=range(1,100001)
ruta_archivo = 'archivo.txt'

# Abrir el archivo en modo escritura
with open(ruta_archivo, 'w') as archivo:
    # Escribir el contenido en el archivo
    archivo.write(list(array))

et = time.time()

elapsed_time = et - st
print('Execution time:', elapsed_time, 'seconds')
