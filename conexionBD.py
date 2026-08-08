import mysql.connector
from config import MYSQL_CONFIG

def obtener_conexion():
    return mysql.connector.connect(**MYSQL_CONFIG)