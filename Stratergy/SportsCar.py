from vehicle import vehicle
from DriveStratergy.Sports_Drive_Stratergy import Sports_Drive_Stratergy_func

class SportsCar(vehicle):

    def __init__(self):
        super().__init__(Sports_Drive_Stratergy_func)