length_centimeters = int(input())
width_centimeters = int(input())
height_centimeters = int(input())
percent = float(input()) / 100

volume_of_the_aquarium = length_centimeters * width_centimeters * height_centimeters / 1000
volume_of_the_aquarium = volume_of_the_aquarium - volume_of_the_aquarium * percent

print(volume_of_the_aquarium)