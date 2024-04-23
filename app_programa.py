list_viajeros = []
import os

def fnt_limpiar():
    os.system('cls')
    print('Autor: Michell Alejandra Mosquera Pacheco')
    print('Copyright(c) 2024')
    print('Universidad Catolica Luis Amigo')

def fnt_agente(op):
    fnt_limpiar()
    if op == '1':
        print('--- AGREGAR VIAJERO ---\n')
        viajero = ''
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        edad = input('Ingrese la edad: ')
        if (int(edad) > 0 and int(edad) <= 25):
            viajero = nombre + ' ' + apellido + ' ' + edad
            list_viajeros.append(viajero)
            print('Viajero agregado correctamente\n')
            enter = input('Presione <ENTER> para continuar...')
        else:
            print('No cuentas con la edad suficiente\n')
            enter = input('Presione <ENTER> para continuar...')
    elif op == '2':
        print('--- MOSTRAR VIAJEROS ---\n')
        if len(list_viajeros) == 0:
            print('\nNo hay viajeros registrados')
            input('Presione <ENTER> para continuar...')
        else:
            for i in list_viajeros:
                print(i)
            input('\nPresione >ENTER> para continuar...')

sw = True
while sw == True:
    fnt_limpiar()
    opcion = input(' ---- MENU PRINCIPAL ----\n1. Agregar\n2. Mostrar \n3. Salir\n4. -> ')
    fnt_agente(opcion)