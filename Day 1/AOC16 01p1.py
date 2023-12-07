file_path = "Day 1/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

moves = lines_array[0].split(", ")

print(moves)
cardinal = 0
# 0 = north
# 1 = east
# 2 = south
# 3 = west
north = 0
south = 0
east = 0
west = 0

for each in moves:
    if each[0] == "R":
        cardinal += 1
    elif each[0] == "L":
        cardinal -= 1

    if cardinal == 4:
        cardinal = 0
    if cardinal == -1:
        cardinal = 3

    if cardinal == 0:
        north += int(each[1:])
    elif cardinal == 1:
        east += int(each[1:])
    elif cardinal == 2:
        south += int(each[1:])
    elif cardinal == 3:
        west += int(each[1:])
    else:
        print("Error")

print(f"North: {north}    South: {south}    East: {east}    West: {west}")
print(f"Total: {abs(north - south) + abs(east - west)}")