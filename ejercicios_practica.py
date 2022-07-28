#!/usr/bin/env python
'''
SQL Introducción [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.1

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.1"

import sqlite3

# https://extendsclass.com/sqlite-browser.html


def create_schema():

    # Conectarnos a la base de datos
    # En caso de que no exista el archivo se genera
    # como una base de datos vacia
    conn = sqlite3.connect('secundaria.db')

    # Crear el cursor para poder ejecutar las querys
    c = conn.cursor()

    # Ejecutar una query
    c.execute("""
                DROP TABLE IF EXISTS estudiante;
            """)

    # Ejecutar una query
    c.execute("""
            CREATE TABLE estudiante(
                [id] INTEGER PRIMARY KEY AUTOINCREMENT,
                [name] TEXT NOT NULL,
                [age] INTEGER NOT NULL,
                [grade] INTEGER,
                [tutor] TEXT
            );
            """)

    # Para salvar los cambios realizados en la DB debemos
    # ejecutar el commit, NO olvidarse de este paso!
    conn.commit()

    # Cerrar la conexión con la base de datos
    conn.close()


def fill():
    print('Completemos esta tablita!')
    # Llenar la tabla de la secundaria con al menos 5 estudiantes
    # Cada estudiante tiene los posibles campos:
    # id --> este campo es auto incremental por lo que no deberá completarlo
    # name --> El nombre del estudiante (puede ser solo nombre sin apellido)
    # age --> cuantos años tiene el estudiante
    # grade --> en que año de la secundaria se encuentra (1-6)
    # tutor --> nombre de su tutor

    # Se debe utilizar la sentencia INSERT.
    # Observar que hay campos como "grade" y "tutor" que no son obligatorios
    # en el schema creado, puede obivar en algunos casos completar esos campos

    group = [('Pablo', 16, 5, 'Chicho'),
             ('Mariana', 15, 4, 'Chicho'),
             ('Pedro', 17, 6, 'Chacho'),
             ('Lisa', 16, 5, 'Chucho'),
             ('Luis', 16, 5, 'Chucho'),
             ('Nicola', 13, 2, 'Chocho'),
             ('Peter', 12, 1, 'Checho'),
             ('Juliana', 12, 1, 'Checho'),
             ]

    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.executemany("""
        INSERT INTO estudiante (name, age, grade, tutor)
        VALUES (?,?,?,?);""", group)
    conn.commit()
    conn.close()

def fetch():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # todas las filas con todas sus columnas
    # Utilizar fetchone para imprimir de una fila a la vez
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    for row in c.execute('SELECT * FROM estudiante'):
        print(row)

    conn.close()


def search_by_grade(grade):
    print('Operación búsqueda!')
    # Utilizar la sentencia SELECT para imprimir en pantalla
    # aquellos estudiantes que se encuentra en en año "grade"

    # De la lista de esos estudiantes el SELECT solo debe traer
    # las siguientes columnas por fila encontrada:
    # id / name / age
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()

    for row in c.execute("""SELECT id, name, age FROM estudiante WHERE grade=?""",(grade,)):
        print(row)

    conn.close()

def insert(new_student):
    print('Nuevos ingresos!')
    # Utilizar la sentencia INSERT para ingresar nuevos estudiantes
    # a la secundaria
    print("Nuevo registro:", new_student)
    fetch()
    
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    c.execute("""
        INSERT INTO estudiante (name, age)
        VALUES (?,?);""", new_student)
    conn.commit()
    conn.close()    
    fetch()
    

def modify(id, name):
    print('Modificando la tabla')
    # Utilizar la sentencia UPDATE para modificar aquella fila (estudiante)
    # cuyo id sea el "id" pasado como parámetro,
    # modificar su nombre por "name" pasado como parámetro
    fetch()
    conn = sqlite3.connect('secundaria.db')
    c = conn.cursor()
    rowcount = c.execute("UPDATE estudiante SET name =? WHERE id =?",(name, id)).rowcount

    print('Filas actualizadas:', rowcount)

    conn.commit()
    conn.close()    
    fetch()
    


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()   # create and reset database (DB)
    fill()
    fetch()

    grade = 5
    search_by_grade(grade)

    new_student = ['Yoli', 16]
    insert(new_student)

    name = '¿Inove?'
    id = 2
    modify(id, name)
