import sqlite3

database = sqlite3.connect("clients.db")
cursor = database.cursor()

def table():
	cursor.execute("CREATE TABLE IF NOT EXISTS reservations (Name TEXT, Last Name TEXT, Age NUMBER, Phone_Number TEXT)")
	database.commit()

def add():
	name = input("Enter your name: ")
	last_name = input("Enter your last name: ")
	age = input("Enter your age: ")
	phone_number = input("Enter your phone number: ")
	cursor.execute("INSERT INTO reservations VALUES (?,?,?,?)", (name, last_name, age, phone_number))
	print("RESERVED SUCCESSFULLY\nWe will call you back in the near future!")
	database.commit()

def show_all_clients():
	print("-----CLIENTS-----")
	cursor.execute("SELECT * FROM reservations")
	i = cursor.fetchall()
	print(*i, sep="\n")

def close():
	database.close()

table()