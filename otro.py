@@ -1,11 +1,11 @@
import mysql.connector

def conectarBd():
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "19841987",
        database = "NeuroCare"
        password = "NeuroCare2026!",
        database = "neuroocare"
    )

    return conexion