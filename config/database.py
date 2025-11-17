#connection databese
import mysql.connector

def connection_database():

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="luna"  # cámbialo por el nombre de tu base
        )

        if conexion.is_connected():
            print("Conexión exitosa!")
    except Exception as e:
        print("Error:", e)

connection_database()