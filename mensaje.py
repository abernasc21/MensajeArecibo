# Esta parte son de las funciones para leer y mostrar
def mostrarMatriz(a,n,m):
#esto solo es una forma para mostrar el mensaje
    for i in range(0,n):
        print(' '.join(map(str,a[i])))#esta parte elimina los [ , ]
def leermatriz(a,n,m,mensajeAUX):
#rellenamos el rectangulo con el mensaje que esta sin ceros
    c=0
    for i in range(n):#filas
        b=[0]*m
        for j in range(m):#columnas
            b[j]=mensajeAUX[c]
            c+=1
        a[i]=b
#!--------------------------------------
# Aqui comienza el codigo para poder armar el mensaje
mensaje=input()
mensaje=mensaje.replace('0',' ') #eliminamos los ceros del mensaje
mensajeAUX=mensaje
tamañodeMensaje=len(mensaje) #calculamos el tamaño del mensaje
print (tamañodeMensaje)
print ("--------------------")
mensaje=tamañodeMensaje
dimensiones=[]
for i in range(2,mensaje): #aqui sacamos las dimensiones del mensaje
    if mensaje%i==0:
        dimensiones.append(i)
print(dimensiones)
print("---------------------")
#!--------------------------------------
matriz=[0]*dimensiones[1] #preparamos el rectangulo del mensaje
leermatriz(matriz,dimensiones[1],dimensiones[0],mensajeAUX) # aqui la funcion busca llenar los espacios del rectangulo
mostrarMatriz(matriz,dimensiones[1],dimensiones[0])
#!-----------------------------------------------
