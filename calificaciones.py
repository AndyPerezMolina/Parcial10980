import psycopg2
from statistics import median,mean,mode,pstdev,pvariance

def menu():
    print("Menu")
    print("1- Ingresar Calificaciones ")
    print("2- Consultar base de datos")
    print("3- Borrar base de datos")
    print("4- Salir")
    return()

def operaciones():
    print("Ingresar 5 Calificaciones")
    list=[]
    for x in range(5):
        valor = float(input("Ingrese calificacion \n"))
        list.append(valor)
    print("Las calificaciones son: \n",list)
    
    print("La media es: ",mean(list))
    print("La mediana es: ",median(list))
    print("La moda es: ",mode(list))
    print("El rango es: ",max(list)-min(list))
    print("La Desviacion Estandar: ",pstdev(list))
    print("La Varianza: ",pvariance(list))

    cursor.execute("INSERT INTO estadistica(nota1,nota2,nota3,nota4,nota5,media,mediana,moda,rango,desviacion,varianza) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",(list[0],list[1],list[2],list[3],list[4],mean(list),median(list),mode(list),max(list)-min(list),pstdev(list),pvariance(list)))
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
                SQL = 'SELECT * FROM estadistica;'
                cursor.execute(SQL)
                valores = cursor.fetchall()
                print(valores)
            elif opcion==3:
                SQL = 'DELETE FROM estadistica;'
                cursor.execute(SQL)
                conexion.commit()
                print("Los registros han sido eliminados")  
            elif opcion == 4:
                break
    except :
        print("Debe ingresar una opcion valida")

cursor.close()
conexion.close()