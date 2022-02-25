import psycopg2

def menu():
    print("Menu")
    print("1- Ingresar Numero")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Numero")
    numero = float(input())

    if numero %2 == 0:
        resultado = "Es Compuesto"
        print("El numero ",numero, "es compuesto")
    else:
        resultado="Es Primo"
        print("El numero ",numero,"Es primo")
    
    cursor.execute("INSERT INTO compuesto(numero,resultado) VALUES(%s,%s);",(numero,resultado))
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
                SQL = 'SELECT * FROM compuesto;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM compuesto;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()