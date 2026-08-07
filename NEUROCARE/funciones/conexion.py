import mysql.connector

def conectarBd():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "19841987",
        database = "NeuroCare"
    )
    
    return conexion
