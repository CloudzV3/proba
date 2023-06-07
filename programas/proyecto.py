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

def print_data(datos):  
    print("\t\tDATOS ORDENADOS\nLos datos son : ", datos)
    print('==========================================================================')

def mean(datos):
    promedio = round((sum(datos) / len(datos)),2)
    print('\t\tPROMEDIO\nEl promedio de los datos ingresados es de: ', promedio)
    print('==========================================================================')
    return promedio

def median(datos):
    mediana = ((len(datos) + 1) // 2)
    print('\t\tMEDIANA\nLa mediana se encuentra en la posición: ', mediana)
    print('El dato en dicha posición es: ',datos[mediana - 1])  #mediana - 1 por q la lista empieza desde 
    print('==========================================================================')

def mode(datos):
    print('\t\tMODA\nLa moda de los datos ingresados es de: ', st.mode(datos))
    print('==========================================================================')

def quartiles(datos):
    print('\t\tCUARTILES')
    for i in range(1,4):
        cuartil = i * ((len(datos) + 1) // 4)
        print('La posición del cuartil Q' , i , ' es: ', cuartil)
        print('Dicha posición del cuartil Q' , i , ' tiene el valor de: ' , datos[cuartil - 1]) #cuartil - 1 por q la lista empieza desde cero
    print('==========================================================================')
        
def variance(datos,promedio):
    print('\t\tVARIANZA')
    sumatoria = [round(((dato - promedio) ** 2),2) for dato in datos]
    varianza = sum(sumatoria) / len(datos)
    print('La varianza (suponiendo que es una muestra) es de: ', round(varianza,2))
    print('==========================================================================')

def diagrama_tallo_hojas(data):
    tallos = []
    hojas = []

    # Dividir los números en tallos y hojas
    for num in data:
        tallo = int(num)
        hoja = int((num - tallo) * 10)
        tallos.append(tallo)
        hojas.append(hoja)

    # Encontrar el valor mínimo y máximo para determinar la longitud del tallo
    min_val = min(tallos)
    max_val = max(tallos)

    # Imprimir el diagrama de tallo y hojas
    print('\t\tDIAGRAMA DE TALLO Y HOJAS')
    for tallo in range(min_val, max_val + 1):
        print(f'{tallo} |', end=' ')
        for i in range(len(tallos)):
            if tallos[i] == tallo:
                print(f'{hojas[i]}', end=' ')
        print()
    print('==========================================================================')




data = read_and_load_data()
data.sort()

print_data(data)
mean(data)  
median(data) #revisar si puede colocar un lugar para números pares (o sea que se coloque entre los dos números donde debería de estar)
mode(data)
quartiles(data) #revisar si puede colocar un lugar para números pares (o sea que se coloque entre los dos números donde debería de estar)
variance(data,mean(data))
diagrama_tallo_hojas(data)
