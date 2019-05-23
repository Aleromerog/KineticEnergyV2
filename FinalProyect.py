from src.Skeleton import Skeleton
from src.animation import *

array = []
fileName = 'data/sample_data.csv'

skeret = Skeleton(fileName)
animate(fileName, skeret.get_kinetic_energy(), skeret.get_calories())


