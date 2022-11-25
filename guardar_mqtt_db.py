import mysql.connector
from decouple import config


def conectarDB():
    mydb = mysql.connector.connect(
        host='localhost',
        user=config('USER_DB'),
        password=config('PASSWORD_DB'),
        database=config('NAME_DB')
    )

    return mydb


def guardarDB(mydb, valores):
    cur = mydb.cursor()
    cur.execute('INSERT INTO datos_tiempo_real (t,num, voltaje, con) VALUES ({t},"{num}", {voltaje},{con})'.format(
        t=valores['t'],num=valores['y'], voltaje=valores['v'],con=valores['c']))
    cur.close()


def cargarDB(valores):
    mydb = conectarDB()
    guardarDB(mydb, valores)
