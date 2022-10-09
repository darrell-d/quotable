from datetime import datetime

import psycopg2
import os

dt = datetime.now()

connection = psycopg2.connect(
    user = os.environ['DB_USER'],
    password = os.environ['DB_PASSWORD'],
    host = os.environ['DB_HOST'],
    port = "5432",
    database=os.environ['DB_NAME'])

cursor = connection.cursor()

file = "{}/import/quotes.csv".format(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
quotes = open(file, "r")
lines = quotes.readlines()

for line in lines:
    line = line.split("|")
    print("Quote: {}".format(line[0]))
    print("Quote Source: {}".format(line[1]))
    quote_body = "" if line[2] in [None, "\n"] else line[2]
    print(quote_body)

    cursor.execute("INSERT INTO quote_quote (quote, body, source, date_added) VALUES (%s, %s, %s, now())", (line[0], quote_body, line[1]))
    connection.commit()


cursor.close()
