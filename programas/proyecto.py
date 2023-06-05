

#lectura de archivo rango.txt
try:
    archivo = open('rango.txt', 'r+')
    rango = [linea.strip() for linea in archivo.readlines()]

    print(rango)
except FileNotFoundError:
    print("El archivo no existe. Checa que esté en el directorio jaja")
except IOError:
    print("No se pudo leer el archivo :(( pásame unos lentes ajaj")    
finally: 
    archivo.close()