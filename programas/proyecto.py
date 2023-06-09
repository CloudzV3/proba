import statistics as st
import math
import csv

#lectura de archivo rango.txt
def read_and_load_data():
    try:
        archivo = open('datospa.txt', 'r') 
        datos = [float(linea.strip()) for linea in archivo.readlines()]  
    except FileNotFoundError:
        print("El archivo no existe. Checa que esté en el directorio jaja")
    except IOError:
        print("No se pudo leer el archivo :(( pásame unos lentes ajaj")    
    finally: 
        archivo.close()
    return datos

#impresión de datos
def print_data(datos):  
    print("\t\tDATOS \nLos datos son : ", datos)
    print('==========================================================================')

#promedio e impresión del mismo también regresa el valor
def print_mean(datos):
    promedio = round((sum(datos) / len(datos)),2)
    print('\t\tPROMEDIO\nEl promedio de los datos ingresados es de: ', promedio)
    print('==========================================================================')

def mean(datos):
    return round((sum(datos) / len(datos)),2)

#mediana e impresión del mismo
def median(datos):
    tam = len(datos)
    if(tam % 2 != 0):
        pos_mediana = (tam + 1) // 2
        mediana = datos[pos_mediana - 1]
    else:
        pos_mediana = (tam + 1) / 2
        superior = datos[math.ceil(pos_mediana) - 1]
        inferior = datos[math.floor(pos_mediana) - 1]
        mediana = (superior + inferior) / 2
    print('\t\tMEDIANA\nLa mediana se encuentra en la posición: ', pos_mediana)
    print('El dato en dicha posición es: ',mediana)  #mediana - 1 por q la lista empieza desde 
    print('==========================================================================')
#moda e impresión del mismo
def mode(datos):
    print('\t\tMODA\nLa moda de los datos ingresados es de: ', st.mode(datos))
    print('==========================================================================')

#cuartiles e impresión del mismo
def quartiles(datos):
    print('\t\tCUARTILES Y PUNTOS ATÍPICOS')
    cuartiles = []
    for i in range(1,4):
        if(i == 2):
            pass
        else:
            cuartil = round(i * ((len(datos) + 1) / 4))
            print('La posición del cuartil Q' , i , ' es: ', cuartil)
            print('Dicha posición del cuartil Q' , i , ' tiene el valor de: ' , datos[cuartil - 1]) #cuartil - 1 por q la lista empieza desde cero
            cuartiles.append(cuartil)
    rango_intercuartil = datos[cuartiles[1]] - datos[cuartiles[0]]
    print('rango intercuartil',rango_intercuartil)
    print((datos[cuartiles[0] - 1] - (1.5 * rango_intercuartil)))
    print((datos[cuartiles[1] - 1] + (1.5 * rango_intercuartil)))
    atípicos_inferiores = [dato for dato in datos if dato < (datos[cuartiles[0] - 1] - (1.5 * rango_intercuartil))]
    atípicos_superiores = [dato for dato in datos if dato > (datos[cuartiles[1] - 1] + (1.5 * rango_intercuartil))]
    print('Los datos atípicos inferiores son: ', atípicos_inferiores)
    print('Los datos atípicos superiores son: ', atípicos_superiores)
    print('==========================================================================')

#varianza e impresión del mismo        
def print_variance_standard_deviation(datos,promedio):
    print('\t\tVARIANZA Y DESVIACIÓN ESTÁNDAR')
    sumatoria = [round((dato - promedio)**2,2) for dato in datos]
    varianza = sum(sumatoria) / (len(datos) - 1)  #si se requiere la fórmula de muestra es n - 1 en vez de n en el denominador
    print('La varianza (suponiendo que es una muestra) es de: ', round(varianza,2))
    print('La desviación estándar es: ', round((math.sqrt(round(varianza,2))),2))

    print('==========================================================================')

#varianza e impresión del mismo        
def variance(datos,promedio):
    sumatoria = [round((dato - promedio)**2,2) for dato in datos]
    varianza = round((sum(sumatoria) / (len(datos) - 1)),2)  #si se requiere la fórmula de muestra es n - 1 en vez de n en el denominador
    #desviacion_estandar = round((math.sqrt(round(varianza,2))),2)
    return varianza


#geenrar diagrama de tallo hojas
def diagrama_tallo_hojas(data):
    tallos = []
    hojas = []

    # Dividir los números en tallos y hojas para enteros
    for num in data:
        tallo = int(num // 10)
        hoja = int((num % 10)) 
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

def intervals (datos):
    print('\t\tINTERVALOS')
    minimo = min(datos)
    maximo = max(datos)
    rango = maximo - minimo
    k_intervalos = 1 + 3.322*math.log10(len(datos))
    print(k_intervalos)
    if(math.floor(k_intervalos) % 2 != 0):  #se recomienda redondear a abajo, pero si es par ese número
        k_intervalos = math.floor(k_intervalos)
        pass                                #-> se redondea a arriba
    else:
        k_intervalos = math.ceil(k_intervalos)

    print('número de intervalos: ', k_intervalos)
    print('rango: ', rango)
    amplitud = round(rango / k_intervalos)
    print('amplitud: ', amplitud)
    intervalos = []
    inicio = 0

    for i in range(k_intervalos - 1):
        if(i == 0):
            inicio = minimo + amplitud
            intervalo = [minimo, inicio]
            intervalos.append(intervalo)
        inicio = inicio + amplitud
        intervalo = [inicio - amplitud, inicio]
        intervalos.append(intervalo)
    
    for intervalo in intervalos:
        intervalo_frecuencia = [dato for dato in datos if dato >= intervalo[0] and dato < intervalo[1]]
        frecuencia = len(intervalo_frecuencia)
        print('Intervalo: ', intervalo, '\tFrecuencia: ', frecuencia)
    print('==========================================================================')

def covariance(x,y):
    prom_x = mean(x)
    prom_y = mean(y)
    n = len(x)
    numerador_valores = []
    for i in range(n):
        valor = (x[i] - prom_x) * (y[i] - prom_y)
        numerador_valores.append(round(valor,2))
    covarianza = round(sum(numerador_valores) / (n - 1),2)
    return covarianza

def matriz_covarianza(cols):
    fila_1 = [variance(cols[0],mean(cols[0])),      covariance(cols[1],  cols[0]),      covariance(cols[2],cols[0]),        covariance(cols[3],cols[0])]
    fila_2 = [covariance(cols[0],cols[1]),          variance(cols[1],mean(cols[1])),    covariance(cols[2],cols[1]),        covariance(cols[3],cols[1])]
    fila_3 = [covariance(cols[0],cols[2]),          covariance(cols[1],  cols[2]),      variance(cols[2],mean(cols[2])),    covariance(cols[3],cols[2])]
    fila_4 = [covariance(cols[0],cols[3]),          covariance(cols[1],  cols[3]),      covariance(cols[2],cols[3]),        variance(cols[3],mean(cols[3]))]
    matriz = [fila_1, fila_2, fila_3, fila_4]
    return matriz

def read_data():
        # Ruta al archivo CSV
    archivo_csv = "otrosDatos.csv"

    # Listas vacías para almacenar las columnas
    columna1 = []
    columna2 = []
    columna3 = []
    columna4 = []

    # Lectura del archivo CSV y almacenamiento de las columnas en las listas correspondientes
    with open(archivo_csv, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            columna1.append(int(fila[0]))
            columna2.append(int(fila[1]))
            columna3.append(int(fila[2]))
            columna4.append(int(fila[3]))
    columna1.sort()
    columna2.sort()
    columna3.sort()
    columna4.sort()
    columnas = [columna1, columna2, columna3,columna4]
    return columnas


datos = read_data()
matriz = matriz_covarianza(datos)
print('Matriz de covarianza: ')
for row in matriz:
    print(row)
print('==============================================================')
for data in datos:
                        # llamada a funciones
    print_data(data)  
    median(data) #revisar si puede colocar un lugar para números pares (o sea que se coloque entre los dos números donde debería de estar)
    mode(data)
    print_mean(data)
    print_variance_standard_deviation(data,mean(data))
    quartiles(data) #revisar si puede colocar un lugar para números pares (o sea que se coloque entre los dos números donde debería de estar)
    diagrama_tallo_hojas(data)
    intervals(data)



