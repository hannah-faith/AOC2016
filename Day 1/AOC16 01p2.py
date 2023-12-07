file_path = "Day 1/input.txt"

with open(file_path, 'r') as file:
    lines_array = [line.strip() for line in file.readlines()]

moves = lines_array[0].split(", ")
cardinal = 0
# 0 = north
# 1 = east
# 2 = south
# 3 = west

coordinates = (0,0)
locations = []
flag = True

for each in moves:
    if flag:
        if each[0] == "R":
            cardinal += 1
        elif each[0] == "L":
            cardinal -= 1

        if cardinal == 4:
            cardinal = 0
        if cardinal == -1:
            cardinal = 3

        r = int(each[1:])
        if cardinal == 0:
            for step in range(1,r+1):
                temp_coordinates = (coordinates[0], coordinates[1] + step)

                if (temp_coordinates[0], temp_coordinates[1]) in locations:
                    print(f"First location visited twice: {(temp_coordinates[0], temp_coordinates[1])}")
                    print(f"Distance: {abs(temp_coordinates[0]) + abs(temp_coordinates[1])}")
                    flag = False
                    break
                else:
                    locations.append((temp_coordinates[0], temp_coordinates[1]))

            coordinates = temp_coordinates

        elif cardinal == 1:
            for step in range(1,r+1):
                temp_coordinates = (coordinates[0] + step, coordinates[1])

                if (temp_coordinates[0], temp_coordinates[1]) in locations:
                    print(f"First location visited twice: {(temp_coordinates[0], temp_coordinates[1])}")
                    print(f"Distance: {abs(temp_coordinates[0]) + abs(temp_coordinates[1])}")
                    flag = False
                    break
                else:
                    locations.append((temp_coordinates[0], temp_coordinates[1]))

            coordinates = temp_coordinates


        elif cardinal == 2:
            for step in range(1,r+1):
                temp_coordinates = (coordinates[0], coordinates[1] - step)

                if (temp_coordinates[0], temp_coordinates[1]) in locations:
                    print(f"First location visited twice: {(temp_coordinates[0], temp_coordinates[1])}")
                    print(f"Distance: {abs(temp_coordinates[0]) + abs(temp_coordinates[1])}")
                    flag = False
                    break
                else:
                    locations.append((temp_coordinates[0], temp_coordinates[1]))

            coordinates = temp_coordinates


        elif cardinal == 3:
            for step in range(1,r+1):
                temp_coordinates = (coordinates[0] - step, coordinates[1])

                if (temp_coordinates[0], temp_coordinates[1]) in locations:
                    print(f"First location visited twice: {(temp_coordinates[0], temp_coordinates[1])}")
                    print(f"Distance: {abs(temp_coordinates[0]) + abs(temp_coordinates[1])}")
                    flag = False
                    break
                else:
                    locations.append((temp_coordinates[0], temp_coordinates[1]))

            coordinates = temp_coordinates

        else:
            print("Error")