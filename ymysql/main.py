from conexion import conectarBD

conexion = conectarBD()

if conexion.is_connected():
    print("conexion exitosa")
    
    conexion.close