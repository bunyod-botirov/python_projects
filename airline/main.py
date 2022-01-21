import admin
import client

while 1:
	try:
		print("-----MAIN PAGE-----")
		choice = input("0. Quit\n1. Admin\n2. Client\nPlease choose one from the above: ")
		if(choice == "0"):
			break
		elif(choice == "1"):
			admin_name = "admin"
			admin_password = "root"
			breaker = False
			while 1:
				if breaker:
					break
				print("Enter 0 in the username field to exit!")
				user_name = input("Enter the Username: ")
				user_password = input("Enter the Password: ")
				if(user_name == "0"):
					break
				elif(admin_name != user_name and admin_password == user_password):
					print("Username incorrect!")
				elif(admin_name == user_name and admin_password != user_password):
					print("Password incorrect!")
				elif(admin_name != user_name and admin_password != user_password):
					print("Username and Password incorrect!")
				else:
					while 1:
						print("-----ADMIN-----")
						print("""1. Add a flight
2. Flight cancellation
3. All flights
4. Show all clients
0. Exit""")
						choice = input("Please choose one from the above: ")
						if(choice == "0"):
							breaker = True
							break
						elif(choice == "1"):
							admin.add()
						elif(choice == "2"):
							admin.delete()
						elif(choice == "3"):
							admin.read()
						elif(choice == "4"):
							client.show_all_clients()
						else:
							print("Please choose the correct number!")
		elif(choice == "2"):
			while 1:
				print("-----CLIENT-----")
				print("0. Exit\n1. All Flights\n2. Make a reservation")
				choice = input("Please choose one from the above: ")
				if(choice == "0"):
					break
				elif(choice == "1"):
					admin.read()
				elif(choice == "2"):
					client.add()
		else:
			print("Please choose correctly!\n")

	except:
		print("Something went wrong!")

admin.close()
client.close()