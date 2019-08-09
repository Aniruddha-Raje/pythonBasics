import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE pythonDb")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)

mycursor.execute("use pythonDb")

mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Aniruddha", "Pune 411038")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
print("Inserted record's ID:", mycursor.lastrowid)

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652') 
]
mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)


mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
	print(x)

mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

sql = "DELETE FROM customers WHERE name = %s"
name = ("Yellow Garden 2",)
mycursor.execute(sql, name)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
