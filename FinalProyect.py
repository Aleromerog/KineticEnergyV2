from src.Skeleton import Skeleton
from src.animation import *

array = []
fileName = 'data/sample_data.csv'
animate(array)

skeret = Skeleton(fileName)


print(skeret.get_calories())
