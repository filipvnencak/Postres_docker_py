import psycopg2
import requests
import json


with open('demo_data.json') as f:
    req = json.loads(f.read())

connection = psycopg2.connect(  user="postgres",
                                password="docker",
                                host="127.0.0.1",
                                port="5432",
                                database="postgres")
#print(json.dumps(data, sort_keys=True, indent=4))

cur = connection.cursor()

cur.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")


connection.commit()
# closing database connection.
if connection:

    cur.close()
    connection.close()
    print("PostgreSQL connection is closed")
else:
    print("No connection")





