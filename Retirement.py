import random

goFor = 40
money = 0
minRange = .9
maxRange = 1.15
addAmount = 5000

for i in range (goFor):
	money += addAmount
	money *= random.random() * (maxRange - minRange) + minRange
	print(money)

