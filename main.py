import psycopg2
import json_parse


data=json_parse.list

connection = psycopg2.connect(  user="postgres",
                                password="docker",
                                host="0.0.0.0",
                                port="5432",
                                database="postgres")

cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS data (type TEXT, name TEXT, policy TEXT);")


for d in data:
    cur.execute("""INSERT INTO data (type, name, policy)  VALUES (%(type)s, %(name)s, %(policy-map-rule)s)""", d)

if connection:
    connection.commit()
    cur.close()
    connection.close()
    print("PostgreSQL connection is closed")






