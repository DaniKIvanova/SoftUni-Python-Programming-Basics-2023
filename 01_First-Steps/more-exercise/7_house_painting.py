height_of_the_house = float(input())
sidewall_length = float(input())
wall_of_the_roof_height = float(input())

window = 2.25
door = 2.40
green_paint = 3.4
red_paint = 4.3

side_wall = height_of_the_house * sidewall_length
side_wall_total = (side_wall * 2) - (window * 2)
back_wall = ((height_of_the_house * height_of_the_house) * 2) - door
total_area_walls = side_wall_total + back_wall
green_paint_needed = total_area_walls / green_paint

two_rectangle_roof = 2 * (height_of_the_house * sidewall_length)
two_triangle_roof = 2 * (height_of_the_house * wall_of_the_roof_height)
total_area_roof = two_rectangle_roof + two_triangle_roof
red_paint_needed = total_area_roof / red_paint

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")