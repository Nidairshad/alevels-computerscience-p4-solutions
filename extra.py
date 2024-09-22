class vehcile:
    #PRIVATE ID :STRING
    #PRIVATE MaxSpeed :INTEGER
    #PRIVATE IncreaseAmount :INTEGER
    #PRIVATE HorizontalPosition:INTEGER
    #PRIVATE CurrentSpeed :INTEGER
    def __init__(self,IDp,MaxSpeedp,IncreaseAmountp):
        self.__ID = IDp
        self.__MaxSpeed = MaxSpeedp
        self.__CurrentSpeed = 0
        self.__IncreaseAmount = IncreaseAmountp
        self.__Horizontalpositon = 0
    def GetCurrentspeed(self):
        return self.__CurrentSpeed
    def GetIncreaseAmount(self):
        return self.__IncreaseAmount
    def GetHorizontalPosition(self):
        return self.__Horizontalpositon
    def GetMaxSpeed(self):
        return self.__MaxSpeed
    def SetCurrentSpeed(self,currentspeed):
        self.__CurrentSpeed= currentspeed
    def SetHorizontalPosition(self,Horizontalposition):
        self.__Horizontalpositon = Horizontalposition
    def IncreaseSpeed(self):
        self.__Horizontalpositon=self.__CurrentSpeed \
                                 + self.__IncreaseAmount
        if self.__CurrentSpeed>self.__MaxSpeed:
            self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
class Helicopter(vehcile):
    def __init__(self,verticalchangep
                ,maxheightp,IDp,MaxSpeedp,IncreaseAmountp):
        super().__init__(IDp,MaxSpeedp,IncreaseAmountp)  # Corrected calling parent constructor
        self.__verticalposition = 0
        self.__verticalchange = verticalchangep
        self.__maxheight = maxheightp
    def increasespeed(self):
        self.__verticalposition += self.__verticalchange  # Corrected calculation
        if self.__verticalposition > self.__maxheight:  # Corrected spelling and capitalization
             self.__verticalposition = self.__maxheight
        self.SetCurrentSpeed(self.GetCurrentSpeed() + self.GetIncreaseAmount())  # Corrected calling methods
        if self.GetCurrentSpeed() > self.GetMaxSpeed():  # Corrected calling methods
            self.SetCurrentSpeed(self.GetMaxSpeed())
        self.SetHorizontalPosition(self.GetHorizontalPosition() + self.GetCurrentSpeed())  # Corrected calling methods
def displayspeed(vehicle):
    print("horizontal position:", vehicle.GetHorizontalPosition())  # Corrected method call
    print("current speed:", vehicle.GetCurrentSpeed())
    if isinstance(vehicle, Helicopter):  # Check if the vehicle is a Helicopter
        print("vertical position:", vehicle._Helicopter__verticalposition)  # Accessing private attribute directly
        print("current position:", vehicle.GetHorizontalPosition())


car = vehcile("tiger",100,20)
newhelicopter = Helicopter(3,100,"lion",350,40)
car.IncreaseSpeed()
car.IncreaseSpeed()
print(displayspeed(car))
newhelicopter.increasespeed()
newhelicopter.increasespeed()
print(displayspeed(newhelicopter))























































