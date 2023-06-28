import math

length = float(input())
width = float(input())

CORRIDOR = 100
L_DESK = 120
W_DESK = 70
OTHER_SPACE = 3

width = math.floor(((width * 100) - CORRIDOR) / W_DESK)
length = math.floor(((length * 100) / L_DESK))
total_space = length * width - OTHER_SPACE

print(total_space)