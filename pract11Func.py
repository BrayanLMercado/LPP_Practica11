'''
Materia: Lenguaje De Programación Python
Nombre: López Mercado Brayan
Matrícula: 1280838
Grupo: 531
Practica 11: Diccionarios
Archivo De Funciones
Fecha: 3 De Noviembre De 2022
'''

def biblioteca():
    libros={
        'El Viejo Y El Mar':230,
        'Luna De Plutón':200,
        'Harry Potter Y La Piedra Filosofal':270,
        'La Brujula Dorada':245,
        'La Biblia':100,
        'Lo Que El Viento Se Llevo':245,
        'El Arte De La Guerra':260,
        'Tom Sayer':245,
        'El Principito':100,
        'Mitología Griega':260,
        'Gente Rara':165
    }
    bookName=input("Captura El Nombre Del Libro: ")
    if bookName.title().strip() in libros:
        try:
            vendidos=int(input("¿Cuantos Libros Se Vendieron? "))
            while vendidos<0:
                vendidos=int(input("¿Cuantos Libros Se Vendieron? (Unicamente Valores Positivos)"))
            precio=vendidos*libros[bookName.title().strip()]
            print("El Precio Del Libro",bookName.title(),"Es",libros[bookName.title()])
            print("El Precio Total De Los Libros Vendidos Es:",precio)
        except Exception:
            print("El Tipo De Dato Capturado No Es Válido")
    else:
        print("El Libro No Se Encuentra En El Inventario")

def casaDeCambio():
    divisas={
        'Dolares':19.40,
        'Yenes':0.13,
        'Euros':19.73,
        'Yuan':2.71,
        'Won':0.014,
        'Libras Esterlinas':23
    }
    try:
        pesos=int(input("Captura La Cantidad De Pesos: "))
        while pesos<0:
            pesos=int(input("Captura La Cantidad De Pesos (Valores Positivos): "))
    except Exception:
        print("Tipo De Dato No Válido")

    for divisa in divisas:
        print(pesos,"Pesos Es",round(pesos/divisas[divisa],3),divisa)

def menu():
    print("      Menu")
    print("1) Biblioteca")
    print("2) Casa De Cambio")
    print("3) Salir")
