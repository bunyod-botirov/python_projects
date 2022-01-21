import sqlite3

database = sqlite3.connect("flights.db")
cursor = database.cursor()

def table():
	cursor.execute("CREATE TABLE IF NOT EXISTS reys (From_x TEXT, To_x TEXT, Cost INTEGER, Flight_Time TEXT,  Landing_Time TEXT, Flight_Duration INTEGER)")
	database.commit()

def add():
	fr = input("From: ")
	to = input("To: ")
	cost = int(input("Cost in $: "))
	flight_time = input("Flight Time: ")
	landing_time = input("Landing Time: ")
	duration = int(input("Duration per hour: "))
	cursor.execute("INSERT INTO reys VALUES (?,?,?,?,?,?)", (fr, to, cost, flight_time, landing_time, duration))
	print("ADDED SUCCESSFULLY")
	database.commit()

def delete():
	name1 = input("Enter the value of FROM: ")
	name2 = input("Enter the value of TO: ")
	name3 = input("Enter the value of COST: ")
	cursor.execute("DELETE FROM reys WHERE From_x = ? AND To_x = ? AND Cost = ?", (name1, name2, name3))
	print("DELETED SUCCESSFULLY")
	database.commit()

def read():
	print("-----ALL FLIGHTS-----")
	print("| from | to | cost | flight | landing | duration |")
	cursor.execute("SELECT * FROM reys")
	i = cursor.fetchall()
	print(*i, sep="\n")

def close():
	database.close()

table()