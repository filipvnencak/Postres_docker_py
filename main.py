import psycopg2
import requests
import json

#conn = psycopg2.connect(user='docker', password='docker', host='127.0.0.1', port='5432')
conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='docker' port='5432'")

with open('demo_data.json') as f:
    req = json.loads(f.read())



#print(json.dumps(data, sort_keys=True, indent=4))

cur = conn.cursor()
cur.execute( "CREATE TABLE  demo ("
             "data json); ")


for item in req:
    data = {field: item[field] for field in req}
    cur.execute("INSERT INTO my_demo VALUES (%s)", (json.dumps(data),))



