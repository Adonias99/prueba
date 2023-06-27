import msvcrt
import os
import time
import numpy

lista_ruts = []
lista_nombres_d = []
lista_nombres_m = []
lista_habitaciones = []


def mostrar_menu():
    
        print("""MENÚ
        1. Grabar
        2. Buscar
        3. Retirarse
        4. Salir""")

    



def validar_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion in(1,2,3,4):
                return opcion
            else:
                print("ERROR! OPCIÓN INCORRECTA!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")


def validar_rut():
    while True:
        try:
            rut = int(input("Ingrese rut(sin puntos ni dígito verificador): "))
            if len(str(rut)) >= 7 and len(str(rut)) <= 8:
                return rut    
            else:
                print("ERROR! EL RUT DEBE TENER ENTRE 7 Y 8 DÍGITOS!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")    
             


def validar_nombre():
    while True:
        nombre = input("Ingrese nombre: ")
        if len(nombre.strip()) >= 3 and nombre.isalpha():
            return nombre
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")

def validar_nombre_mascota():
    while True:
        nombre_m = input("Ingrese nombre de su mascota: ")
        if len(nombre_m.strip()) >= 3 and nombre_m.isalpha():
            return nombre_m
        else:
            print("ERROR! EL NOMBRE DEBE TENER AL MENOS 3 LETRAS!")




def validar_cantidad():
    while True:
        try:
            cantidad = int(input("Ingrese cantidad de días que permanecera su mascota en la guarderia: "))
            if cantidad >= 1:
                return cantidad
            else:
                print("ERROR! LA CANTIDAD DEBE SER MINIMO 1!")
        except:
            print("ERROR! DEBE INGRESAR UN NÚMERO ENTERO!")




def habitacion_m():
    while True:
        try:
            habitacion = int(input("Eliga habitación (1 - 10): "))
            if habitacion >= 1 and habitacion <= 10:
                return habitacion
        
            else:
                print("ERROR! debe ingresar una habitacion valida!")
        except:
            print("ERROR! debe ingresar un número entero!")        

def buscar_m():
    validar_rut()


        
    
def retirarse_3():
    validar_rut()

def grabar_1():
    validar_rut()
    validar_nombre()
    validar_nombre_mascota()
    validar_cantidad() 
    habitacion_m()


