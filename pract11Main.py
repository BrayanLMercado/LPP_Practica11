'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 11: Diccionarios
Archivo Principal
Fecha: 3 De Noviembre De 2022
'''

from pract11Func import*

menu()
try:
    opc=int(input("Selecciona Una Opción: "))
    while opc<0 or opc>3:
       opc=int(input("Selecciona Una Opción (1 a 3): ")) 
    if opc==1:
        biblioteca()
    elif opc==2:
        casaDeCambio()
    else:
        print("Gracias Por Usar El Programa")
except Exception:
    print("Error En La Captura De Datos")