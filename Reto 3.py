'''
Situación
El programa de Ingeniería ambiental de la Universidad El Bosque en una de sus salidas de campo, ha registrado un par de
temperaturas diarias (máxima, mínima) para todos los días que permanecieron en campo. Dadas las condiciones del terreno
donde se encontraban, no era posible tener temperaturas menores de 5 grados ni mayores de 35 grados, que se consideraron
errores, pero igual se registraron para su estudio posterior. La pareja de temperaturas (0,0) indicará que se han terminado
los datos de la salida de campo.

El director del programa le ha solicitado a usted como programador, que le desarrolle un programa en lenguaje Python
que le permita:

• Leer desde el teclado todos los datos registrados en la salida de campo.
• Mostrar en consola el número total de días que duró la salida de campo.
• Mostrar en consola cuantos días en total se tuvieron temperaturas con error,
  de los cuales se debe informar cuántos fueron por temperaturas menores de 5 grados,
  cuántos fueron por temperaturas mayores de 35 grados y cuántos por ambos errores.

• Mostrar en consola la temperatura media mínima y máxima, sin tener en cuenta los días en que se reportaron errores.
• Mostrar en consola el porcentaje de días que se reportaron errores respecto del total de días reportados.

Autor: Alejandro Meneses Roldan
Fecha: 16/05/2021

'''
temp_1 = float(0)              #registra el valor de la primera temperatura
temp_2 = float(0)              #registra el valor de la segunda temperatura
temp_max = float(0)            #variable que asume el valor de la temperatura maxima
temp_min = float(0)            #variable que asume el valor de la temperatura minima
mediamax = float(0)            #saca el promedio o la media de la temperatura maxima sin errores
mediamin = float(0)            #saca el promedio o la media de la temperatura minima sin errores
participacion = float (0)      #saca la particiapacion de errores en los dias totales en porcentaje
acu_tempmax = float(0)         #acumulador de las temperaturas Maximas sin error para sacar la media o promedio
con_diassinerrormax = int(0)   #contador de dias sin error en la temperatura maxima para sacar la media o promedio
acu_tempmin = float(0)         #acumulador de las temperaturas Minimas sin error para sacar la media o promedio
con_diassinerrormin = int(0)   #contador de dias sin error en la temperatura minima para sacar la media o promedio
con_diastotales = int(1)       #contador para dias totales por temas de presentacion lo inicio en 1 porque el dia 0 no deberia existir
con_diaserror = int(0)         #contador para dias con al menos un error
con_diaserrormax = int(0)      #contador para dias con error en el rango mayor de 35
con_diaserrormin = int(0)      #contador para dias con error en el rango menor de 5
con_diaserrorambas  = int(0)   #contador para dias con error en ambos limites

def max_min (temp_1 ,temp_2):
  global temp_max
  global temp_min
  if temp_1 >= temp_2 :
    temp_max = temp_1      #determina cual de las dos temperaturas es la maxima y la minima,
    temp_min = temp_2      #si son iguales entra al primer condicional y los asigna como si
  else:                    #la temp_1 fuera la Maxima y la temp_2 fuera la minima,
    temp_max = temp_2      #matematicamente da igual ya que son iguales
    temp_min = temp_1

def dias_error(temp_max,temp_min):
    global con_diaserror
    if temp_max < 5 or temp_max > 35 or temp_min < 5 or temp_min > 35:
       con_diaserror += 1

def error_varios(temp_max,temp_min):
    global con_diaserrorambas
    global con_diaserrormin
    global con_diaserrormax
    if (temp_max < 5 or temp_min < 5) and (temp_max > 35 or temp_min > 35) :      #cuenta los dias con errores en ambos rangos
        con_diaserrorambas  += 1
    elif temp_max < 5 or temp_min < 5 :     #cuenta los dias con errores en minima
        con_diaserrormin += 1
    elif temp_max > 35 or temp_min > 35 :    #cuenta dias con errores en maxima
        con_diaserrormax += 1

def datos_media_participacion(temp_min,temp_max):
    global acu_tempmin
    global acu_tempmax
    global con_diassinerrormin
    global con_diassinerrormax
    if temp_min >= 5 and temp_min <= 35 and temp_max >= 5 and temp_max <= 35:
        acu_tempmin += temp_min                                                 #esta seccion verifica los dias que no se tuvo error en ninguna de las dos medidas
        con_diassinerrormin += 1                                                #acumula la temperatura y cuenta los dias para sacar el promerdio o media
    if temp_max >= 5 and temp_max <= 35 and temp_min >= 5 and temp_min <= 35:   #posteriormente sin tener en cuenta los dias que registro errores
        acu_tempmax += temp_max
        con_diassinerrormax += 1
    # Mostrar en consola la temperatura media mínima y máxima, sin tener en cuenta los días en que se reportaron errores.

def inicio():
    print('           ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('           ▒                                                                      ▒')
    print('           ▓     ░░▒▒▓▓██  INGENIERIA AMBIENTAL UNIVERSIDAD EL BOSQUE  ██▓▓▒▒░░   ▓')
    print('           █                                                                      █')
    print('           ▓                             ░░▒▒▓▓██   Powered By MINTIC  ██▓▓▒▒░░   ▓')
    print('           ▒                                                                      ▒')
    print('           ░░░░░░░░░▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓██████████████████▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒░░░░░░░░░')
    print('                                                                                   ')
    print('                                                                                   ')
    print('╔═════════════════════════════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                                                 ║')
    print('║   Bienvenido al programa de registro de temperaturas ambientales de la universidad El Bosque    ║')
    print('║   el cual le permitirá registrar los datos de las temperaturas tomadas durante una salida de    ║')
    print('║   campo, deberá ingresar las temperaturas tomadas por cada día (mínima y máxima) sin importar   ║')
    print('║   el orden, para terminar el proceso de ingreso de información digite el número cero (0) en     ║')
    print('║   ambas temperaturas para ver los resultados finales, gracias.                                  ║')
    print('║                                                                                                 ║')
    print('╚═════════════════════════════════════════════════════════════════════════════════════════════════╝')
    print('                                                                                                   ')
    print('                                                                                                   ')
    print('───────────────────────────────────────────────────────────────────────────────────────────────────')

def datos_reg():
    print('                                                                                                       ')
    print('                                        ░░▒▒▓▓██ ██▓▓▒▒░░                                              ')
    print('                         ░░▒▒▓▓██  DATOS REGISTRADOS CON EXITO  ██▓▓▒▒░░                               ')
    print('                                        ░░▒▒▓▓██ ██▓▓▒▒░░                                              ')
    print('═══════════════════════════════════════════════════════════════════════════════════════════════════    ')
    print('Recuerde que para finalizar el proceso de registro debe ingresar el número 0 en ambas temperaturas     ')
    print('═══════════════════════════════════════════════════════════════════════════════════════════════════    ')

def media_participacion(con_diastotales,con_diaserror,con_diassinerrormin,acu_tempmin,acu_tempmax,con_diassinerrormax):
    global participacion
    global mediamin
    global mediamax
    if con_diastotales != 0:
        participacion = float(con_diaserror / con_diastotales)        #hago una verificacion que los dias totales, los dias sin error en maxima
    if  con_diassinerrormin != 0 :                                    #y los dias sin error en minima que no sean numero cero (0) porque no se
        mediamin = float(acu_tempmin / con_diassinerrormin)           #puede dividir por (0), el programa da error y se sale con este condicional
    if  con_diassinerrormax != 0:                                     #se salta las divisiones y muestra el final.
        mediamax = float(acu_tempmax / con_diassinerrormax)

def final(con_diastotales,con_diaserror,con_diaserrormin,con_diaserrormax,con_diaserrorambas,mediamin,mediamax,participacion):
    print('\n\n')
    print('                                 ░ ░ ▒ ▒ ▓ ▓ █ █  █ █ ▓ ▓ ▒ ▒ ░ ░                    ')
    print('                    ░ ░ ▒ ▒ ▓ ▓ █ █   TOMA DE DATOS TERMINADA  █ █ ▓ ▓ ▒ ▒ ░ ░       ')
    print('                                 ░ ░ ▒ ▒ ▓ ▓ █ █  █ █ ▓ ▓ ▒ ▒ ░ ░ \n\n\n\n           ')
    print('   ╔══════════════════════════════════════════════════════════════╗       ')
    print('   ║        ░░▒▒▓▓██  RESUMEN FINAL DE LA MUESTRA  ██▓▓▒▒░░       ║       ')
    print('   ╠══════════════════════════════════════════════════════════════╣       ')
    print('   ║                                                              ║       ')
    print('   ║  Total días de la muestra               : {:<3}días            ║'.format(con_diastotales))
    print('   ║  Total días con error                   : {:<3}días            ║'.format(con_diaserror))
    print('   ║  Total días con errores menores a 5°    : {:<3}días            ║'.format(con_diaserrormin))
    print('   ║  Total días con errores mayores a 35°   : {:<3}días            ║'.format(con_diaserrormax))
    print('   ║  Total días con error en los dos rangos : {:<3}días            ║'.format(con_diaserrorambas))
    print('   ║                                                              ║       ')
    print('   ╠══════════════════════════════════════════════════════════════╣       ')
    print('   ║                                                              ║       ')
    print('   ║  Temperatura media Mínima   : {:<5}°                         ║'.format(round(mediamin,3)))
    print('   ║  Temperatura media Máxima   : {:<5}°                         ║'.format(round(mediamax,3)))
    print('   ║  Participación de errores   : {:<6}%                        ║'.format(round(participacion*100,3)))
    print('   ║                                                              ║       ')
    print('   ╚══════════════════════════════════════════════════════════════╝       ')
    print('                                               ')
    print('                                               ')
    print('                                               ')
    print(' Hecho por Alejandro Meneses Roldan ♠          ')
    print(' Proyecto MINTIC 2022 UNIVERSIDAD EL BOSQUE    ')

while True:
    inicio()
    temp_1 = float(input(print('\tPor favor digite la primera temperatura registrada el día ',con_diastotales,':   ')))
    temp_2 = float(input(print('\n\tPor favor digite la segunda temperatura registrada el día ',con_diastotales,': ')))
    print('───────────────────────────────────────────────────────────────────────────────────────────────────     ')
    '''
    temp_1 = float(input())       #ESTA ES LA PRESENTACION PARA EL BOT
    temp_2 = float(input())
    '''

    if temp_1 == 0 and temp_2 == 0:
        break

    con_diastotales +=1

    max_min(temp_1 ,temp_2)

    dias_error(temp_max,temp_min)

    error_varios(temp_max,temp_min)

    datos_media_participacion(temp_min,temp_max)

    #datos_reg()

con_diastotales -= 1

media_participacion(con_diastotales,con_diaserror,con_diassinerrormin,acu_tempmin,acu_tempmax,con_diassinerrormax)

final(con_diastotales,con_diaserror,con_diaserrormin,con_diaserrormax,con_diaserrorambas,mediamin,mediamax,participacion)
'''
print(con_diastotales) #Contador_Dias

print(con_diaserror) #Dias_Error

print(con_diaserrormin) #Contador_Min              #ESTA ES LA PRESENTACION PARA EL BOT

print(con_diaserrormax) #Contador_Max

print(con_diaserrorambas) #Contador_Ambos

print(mediamax) #Media_Max

print(mediamin) #Media_Min

print(participacion*100) #Porcentaje_Dias_Error
'''