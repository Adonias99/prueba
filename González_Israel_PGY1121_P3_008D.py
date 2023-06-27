import funcionesp3 as fn
import os
import time
import numpy
import msvcrt

lista_ruts = []
lista_nombres_d = []
lista_nombres_m = []
lista_habitaciones = []



hotel_mascota = numpy.zeros((2,5))
os.system('cls')
print("   HABITACIONES")

print(hotel_mascota)
time.sleep(3)
while True:

    fn.mostrar_menu()

        
    if fn.validar_opcion() == 1:
        rut = fn.validar_rut()
        nombre = fn.validar_nombre()
        nombre_m = fn.validar_nombre_mascota()
        cantidad = fn.validar_cantidad()
        habitacion = fn.habitacion_m()
        lista_ruts.append(rut)

        time.sleep(3)

    elif fn.validar_opcion() == 2: 
          fn.buscar_m()
          if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                  if len(lista_ruts) == x:
                      posicion = x
            print("Su mascota se encuentra en la habitación", habitacion)
                          
                          
          else:
            print("ERROR! su rut no se encuentra en la lista!")            


    elif fn.validar_opcion() == 3:   
        fn.retirarse_3()
        if rut in lista_ruts:
            for x in range(len(lista_ruts)):
                  if len(lista_ruts) == x:
                      posicion = x

            print("SU TOTAL A PAGAR ES:",  cantidad * 15000)


    else:
        print("Gracias, adios")
        break

        
            
    

        
