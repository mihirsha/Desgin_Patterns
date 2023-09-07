from vehicle import vehicle
from DriveStratergy.Off_road_Drive_Stratergy import Off_road_Drive_Stratergy_func

class offroadcar(vehicle):

    def __init__(self):
        super().__init__(Off_road_Drive_Stratergy_func)