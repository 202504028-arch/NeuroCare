import mysql.connector

def conectarBD():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "19841987",
        database = "sistema_usuarios"
    )

    return conexion

