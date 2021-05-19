import mysql.connector
from flask import Flask, jsonify

app = Flask(__name__)

#connect to the mysql server running as a statefulset deployment
mydb = mysql.connector.connect(
  host="mysql-set-0.mysql-headless.default.svc.cluster.local",
  user="root",
  password="password"
)

#add data in the database table
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS books")

mycursor.execute("USE books")

mycursor.execute("CREATE TABLE IF NOT EXISTS authors (id INT, name VARCHAR(20), email VARCHAR(255));")

mycursor.execute("""INSERT IGNORE INTO authors (id,name,email) VALUES(1,"Vivek","vivek@example.com");""")

mycursor.execute("""INSERT IGNORE INTO authors (id,name,email) VALUES(1,"Priya","priya@example.com");""")

mycursor.execute("""INSERT IGNORE INTO authors (id,name,email) VALUES(1,"Shashank","shashank@example.com");""")

mycursor.execute("SELECT * FROM authors")

result = mycursor.fetchall()

@app.route('/')
def main():
  output = []

  for x in result:
    output.append(x)

  return jsonify(output)
