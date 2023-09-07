from typing import List
from SportsCar import SportsCar
from off_road_car import offroadcar
from vehicle import vehicle

orc = offroadcar()
orc2 = SportsCar()

list: List[vehicle] = [orc, orc2]

for car in list:
    print(car.drive())
