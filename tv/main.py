from controller import *
controller = Controller()

while 1:
    choice = input("To switch ON the TV press 1\nTo put remote control press 0: ")
    if(choice == "1"):
        controller.status()
        while 1:
            print("----------")
            choice = input("1 -> Switch OFF\n2 -> Info\n3 -> Current channel\n4 -> All channels\n5 -> Change current channel\n6 -> Sound controll\n7 -> Add a new channel\nPlease select one from above: ")
            if(choice == "1"):
                controller.status()
                break
            elif(choice == "2"):
                print("-----INFO-----")
                print(controller)
            elif(choice == "3"):
                controller.show_current_channel()
            elif(choice == "4"):
                controller.channels_list()
            elif(choice == "5"):
                controller.change_current_channel()
            elif(choice == "6"):
                controller.sound_controll()
            elif(choice == "7"):
                controller.add_channel()
            else:
                print("Please select one from above!")
    elif(choice == "0"):
        break
    else:
        print("Please Switch on the TV!")