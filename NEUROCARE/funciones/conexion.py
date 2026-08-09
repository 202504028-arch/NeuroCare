import mysql.connector

def conectarBd():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "NeuroCare2026!",
        database = "neuroocare"
    )
    
    return conexion
