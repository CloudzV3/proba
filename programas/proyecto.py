import statistics as st

#lectura de archivo rango.txt
def read_and_load_data():
    try:
        archivo = open('datos.txt', 'r') 
        datos = [float(linea.strip()) for linea in archivo.readlines()]  
    except FileNotFoundError:
        print("El archivo no existe. Checa que esté en el directorio jaja")
    except IOError:
        print("No se pudo leer el archivo :(( pásame unos lentes ajaj")    
    finally: 
        archivo.close()
    return datos  

data = read_and_load_data()

def mean(datos):
    print('\t\tPROMEDIO\nEl promedio de los datos ingresados es de: ',round((sum(datos) / len(datos)),2))

def median(datos):
    print('\t\tMEDIANA\nLa mediana de los datos ingresados es de: ', (len(datos) + 1) / 2)

def mode(datos):
    print('\t\tMODA\nLa moda de los datos ingresados es de: ', st.mode(datos))

mean(data)
median(data)
mode(data)