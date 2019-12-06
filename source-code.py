from time import sleep
class Cars:

    def __init__(self,name,speed,fuel):
        print("Getting Data! ")
        self.name = name
        self.speed = speed
        self.fuel = fuel

        if type(self.name) != str or self.name == "":
            print("You didn't write a name! ")
            str("Press any key to exit ")
            exit()
        else:
            pass

    
    def increment(self,count):
        print("Incrementing the speed... ")
        sleep(3)
        while self.speed < count:
            self.speed = self.speed + 5
            if self.speed == count:
                print("The speed is good according what you want!")
                print(self.speed)
                break #Stop the loop
            else:
                continue #Continue the loop :) until gets the correct value 

    
    def decrement(self,count):
        print("Decrementing the speed... ")
        sleep(3)
        while self.speed > count:
            self.speed = self.speed - 5
            if self.speed == count:
                print("The value of speed as you want!")
                print(self.speed)
                break
            else:
                continue


#Attributes
user_car = Cars("Dacia",210,1)
user_car.increment(270)