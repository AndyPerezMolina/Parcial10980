import psycopg2

def menu():
    print("Menu")
    print("1- Calcular IVA ")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar Precio del producto")
    precio = float(input())

    preciosiniva = precio / 1.12
    print("El precio del producto sin IVA es:","{:.2f}".format(preciosiniva))
    iva = preciosiniva*0.12
    print("El mont de IVA es: ", "{:.2f}".format(iva))
    
    cursor.execute("INSERT INTO iva(precio,costo,iva) VALUES(%s,%s,%s);",(precio,preciosiniva,iva))
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
                SQL = 'SELECT * FROM iva;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM iva;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()