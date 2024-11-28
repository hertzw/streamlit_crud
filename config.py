from pathlib import Path
import mysql.connector
from decouple import config

class repositorio():
    mydb = mysql.connector.connect(
            host=config("host"),
            user=config("user"),
            password=config("password"),
            database=config("database"),
    )  # Conexão com dados do banco de dados e MySQL
    mysqlcursor = mydb.cursor()
    
