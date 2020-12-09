
##FUNCIONES
def esPotenciaDeDos(numero):
    if((numero & (numero-1)) == 0 ):
        return True
    else:
        return False

## fin FUNCIONES
print("-------------------------------------------------------------------------------------")
print("\tCÓDIGO HAMMING")
#SE ingresan los datos de entrada.
datosEntrada = input("Ingresa la información que desea enviar: ")
datosEnLista = list(datosEntrada)

#Se cambia a int los numeros de la lista que estan como string
for bucle in range(0, len(datosEnLista)):
    datosEnLista[bucle] = int(datosEnLista[bucle])

#Tamano de la lista
m = len(datosEnLista)
#En esta lista se colocan las posiciones de los bits de paridad e informaciones
ubicaciones = []
#En esta lista se colocan los bits de la posicion de la informacion
bitsDePosicionInfo = []
#Un contador
contador = 1

#Agrega una lista que contiene posiciones donde van bits de paridad e informacion
#Ejm: si agrego de entrada '1010', se forma la lista ['P', 'P', 'I', 'P', 'I', 'I', 'I']
while ubicaciones.count("I") != m:
    if(esPotenciaDeDos(contador)):
        ubicaciones.append("P")
    else:
        ubicaciones.append("I")
        bitsDePosicionInfo.append(bin(contador)[2:])

    contador = contador + 1

# print(datosEnLista)
# print(posiciones)
# print(posImpares)


#AQUI EMPIEZA A ANALIZAR PARA COLOCAR LOS BITS DE PARIDAD.
bitsDeParidad = []
#Este identificador, identifica el numero de posicion a analizar, es decir
#Si tengo '001' el idPosicion[-1] es el '1'
idPosicion = -1 


#Va a agreagar los bits de paridad, si son 1 o 0, estos se agregar a la lista de bitsDEParidad
filasAContar = (len(ubicaciones)- len(bitsDePosicionInfo)) #0, 1, 2
for bucleUno in range(0, filasAContar): 
    contadorParidad = 0   
    for bucleDos in range(0, len(datosEnLista)): # 0, 1, 2, 3
        #Analiza el tamano
        if(len(bitsDePosicionInfo[bucleDos]) >= ( -1*idPosicion)):
    
            if( int(bitsDePosicionInfo[bucleDos][idPosicion]) == 1):
                
                if(int(datosEnLista[bucleDos]) == 1):
                    contadorParidad = contadorParidad + 1

    #En esta parte se decide si los bits de paridad que se van a agregar son 0 o 1                
    if(contadorParidad % 2 == 0):
        bitsDeParidad.append(0)
    else:
        bitsDeParidad.append(1)

    idPosicion = idPosicion - 1       

#En este punto ya se tiene todo esto,:
#por ejemplo, si se ingresa de entrada 1010, se tiene esta info:
#INformacion:  [1, 0, 1, 0]
#Paridad  [1, 0, 1]
#Ubicaciones:  ['P', 'P', 'I', 'P', 'I', 'I', 'I']
# print("Informacion: ", datosEnLista)
# print("Paridad ", bitsDeParidad)
# print("Ubicaciones: ", ubicaciones)
# print("Bits de posiciones info: ", bitsDePosicionInfo)



#Ahora se agregan todos los bits de paridad e informacion en sus respectivas posiciones
#En esta lista ['P', 'P', 'I', 'P', 'I', 'I', 'I']. (Se la cambia por los bits correspondientes.)
contadorGeneral = 0
nContadorDeParidad = 0
nContadorDeInfo = 0
for nuevoBucle in ubicaciones:
    if(nuevoBucle == 'P'):
        ubicaciones[contadorGeneral] = int(bitsDeParidad[nContadorDeParidad])
        nContadorDeParidad = nContadorDeParidad  + 1
    else:
        ubicaciones[contadorGeneral] = int(datosEnLista[nContadorDeInfo])
        nContadorDeInfo = nContadorDeInfo + 1

    contadorGeneral = contadorGeneral +1


print(f"Se muestra la información de ({datosEntrada}) codificada en código hamming: {ubicaciones}")
    


#Ahora empieza el proceso de DECODIFICACIÓN Y CONTROL DE ERRORES. *******************************
# se tiene [1, 0, 1, 1, 0, 1, 0]
datosRecibidos = input("\nPor favor ingrese la información recibida: ")
listaDeDatosRecibidos = list(datosRecibidos)

for bucle in range(0, len(listaDeDatosRecibidos)):
    listaDeDatosRecibidos[bucle] = int(listaDeDatosRecibidos[bucle]) #Se cambia la lista a numeros enteros

#Se crea una lista que tiene los numeros binarios de todo el hamming
todosBinarios = []

for numBinario in range(1, len(ubicaciones)+1):
    todosBinarios.append(bin(numBinario)[2:])

#print("Todos los binarios", todosBinarios)


bitsDeVerificacion = [] #Aqui se guardan los bits d everificacion para porteriormente analizarlos.
idPosicionDec = (-1 * filasAContar)  # depende los bits que se hayan aumentado para paridad.

for bucleUno in range(0, filasAContar): 
    miContador = 0
     
    for bucleDos in range(0, len(ubicaciones)): # 0, 1, 2, 3, 4 , 5, 6
        #Analiza el tamano
        if(len(todosBinarios[bucleDos]) >= (-1*idPosicionDec)): 
    
            if( int(todosBinarios[bucleDos][idPosicionDec]) == 1):
                
                if(int(listaDeDatosRecibidos[bucleDos]) == 1):
                    miContador = miContador + 1
                    
    if(miContador % 2 == 0):
        bitsDeVerificacion.append(0)
    else:
        bitsDeVerificacion.append(1)

    idPosicionDec = idPosicionDec + 1 

#print("Bits de verificacion", bitsDeVerificacion)

#Ahora se analiza si existe algun error
esValido = True
for bucle in bitsDeVerificacion:
    if int(bucle) != 0 :
        esValido = False


#Se identifca el error en caso que sea falso o sino se confirma que esta bien la informacon en caso que sea verdadero
if(esValido):
    print("\n\tNo se detectaron errores")
    print("Trama codificada  enviada: \t", ubicaciones)
    print("Trama codificada recibida: \t", datosRecibidos) 
else:
    #En esta parte se analiza porque se ha detectado algun error.
    print("\n\tSe ha identificado un error")
    posError = ""

    for bucle in bitsDeVerificacion:
        posError += str(bucle)

    posError = int(str(posError), 2) #Se lo cambia a formato decimal y a entero

    print(f"El error se encuentra en el bit #({posError})")
    print("Por lo tanto se debe corregir el error. Se tiene lo siguiente: ")
    print("Trama     codificada      enviada: \t", ubicaciones)
    print("Trama codificada erronea recibida: \t", listaDeDatosRecibidos)

    #Se corrige el error:
    if(listaDeDatosRecibidos[posError -1] == 1):
        listaDeDatosRecibidos[posError-1] = 0
    else:
        listaDeDatosRecibidos[posError-1] = 1

    #Ahora ya se encuentra corregido el error.
    print("Trama     codificada    corregida: \t", listaDeDatosRecibidos)

print("-------------------------------------------------------------------------------------")




