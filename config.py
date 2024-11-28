from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()  # Carrega variáveis do .env

class repositorio:
    mydb = mysql.connector.connect(
        host=os.getenv("host"),
        user=os.getenv("user"),
        password=os.getenv("password"),
        database=os.getenv("database")
    )
    mysqlcursor = mydb.cursor()

    
