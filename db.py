#pip install mysql-connector-python
#pip freeze

import mysql.connector

#conect
connection = mysql.connector.connect(

    host = "localhost",
    user="root",
    passwd="ubermensch",
    #nota mental so escreva a proxima linha se o banco ja estiver criado
    database='db_cars'

)

cursor= connection.cursor()

#executes into database
cursor.execute("create database IF NOT EXISTS db_cars")
cursor.execute("USE db_cars;")
cursor.execute("""
    CREATE TABLE IF NOT EXISTS tbl_cars (
        id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
        marca VARCHAR(100) NOT NULL,
        modelo VARCHAR(100) NOT NULL,
        fabricacao DATE NOT NULL,
        UNIQUE INDEX (id)
    );
""")
cursor.execute("""
    INSERT INTO tbl_cars (marca, modelo, fabricacao)
    VALUES ('fusca', 'Volkswagen', '2000-05-20');
""")


#commit the changes
connection.commit()


# Recuperar os resultados da consulta
results = cursor.fetchall()
for row in results:
    print(row)


cursor.close()
connection.close()
