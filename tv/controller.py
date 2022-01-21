class Controller():
    def __init__(self, power = "OFF", channel = "BBC", channels = ["BBC", "MTV", "MY5", "Sevimli"], sound = 0):
        self.power = power
        self.channel = channel
        self.channels = channels
        self.sound = sound
    def tv_power(self):
        return f"{self.power}"

    def __str__(self):
        return f"Status: {self.power}\nCurrent channel: {self.channel}\nAll channels: {self.channels}\nSound: {self.sound}"
    
    def status(self):
        if(self.power == "OFF"):
            self.power = "ON"
        else:
            self.power = "OFF"

    def show_current_channel(self):
        print(f"You are on {self.channel} channel now!")

    def channels_list(self):
        l = self.channels
        print(f"All available channels: {self.channels}.")

    def sound_controll(self):
        print(f"Current sound status: {self.sound}")
        while 1:
            i = input("+ / - : ")
            if(i == "+"):
                if(self.sound < 10):
                    self.sound += 1
                print(f"Current sound status: {self.sound}")
            elif(i == "-"):
                if(self.sound > 0):
                    self.sound -= 1
                print(f"Current sound status: {self.sound}")
            else:
                break

    def change_current_channel(self):
        print(f"Current channel: {self.channel}")
        while 1:
            i = input("+ / - : ")
            if(i == "+"):
                if(self.channel == self.channels[-1]):
                    print(f"Current channel: {self.channel}")
                else:
                    t = self.channels.index(self.channel)
                    t += 1
                    self.channel = self.channels[t]
                    print(f"Current channel: {self.channel}")
            elif(i == "-"):
                if(self.channels[0] == self.channel):
                    print(f"Current channel: {self.channel}")
                else:
                    t = self.channels.index(self.channel)
                    t -= 1
                    self.channel = self.channels[t]
                    print(f"Current channel: {self.channel}")
            else:
                break

    def add_channel(self):
        new = input("Enter the name of the new channel: ")
        self.channels.append(new)
        print(f"All available channels: {self.channels}.")

    
    
        