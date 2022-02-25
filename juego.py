from random import randint
import psycopg2

def menu():
    print("Menu")
    print("1- Lanzar Dados")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    print("Valor del Dado 1 es:",dado1)
    print("Valor del Dado 2 es:",dado2)

    suma = dado1+dado2
    if suma == 8 :
        resultado = "Gano"
        print("Usted Gano")
        cursor.execute("INSERT INTO juego(dado1,dado2,suma,resultado) VALUES(%s,%s,%s,%s);",(dado1,dado2,suma,resultado))
        conexion.commit()
    elif suma == 7 :
        resultado = "Perdio"
        print("Usted Perdio")
        cursor.execute("INSERT INTO juego(dado1,dado2,suma,resultado) VALUES(%s,%s,%s,%s);",(dado1,dado2,suma,resultado))
        conexion.commit()
    elif suma != 7 or suma!=8 :
        resultado = "Seguir Lanzando"
        print("Debe Seguir Lanzando")
        cursor.execute("INSERT INTO juego(dado1,dado2,suma,resultado) VALUES(%s,%s,%s,%s);",(dado1,dado2,suma,resultado))
        conexion.commit()
    return()




conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    user = "postgres",
    password = "1234",
    dbname = "tareap1"
)

cursor = conexion.cursor()
while True:
    menu()
       
    try :
            opcion = int(input())
            if opcion == 1:
                operaciones()
            elif opcion==2:
                SQL = 'SELECT * FROM juego;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM juego;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()