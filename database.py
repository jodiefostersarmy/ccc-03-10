import psycopg2
import os

connection = psycopg2.connect(
    database="library_api",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    host="13.236.68.16",
    port="5432"
)

cursor = connection.cursor()

cursor.execute("create table if not exists books (id serial PRIMARY KEY, title varchar);")
connection.commit()