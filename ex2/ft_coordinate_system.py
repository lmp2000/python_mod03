import math


Coordinate = tuple[float, float, float]


def get_player_pos() -> Coordinate:
    while True:
        raw = input("Enter new coordinates as floats in format 'x,y,z': ")
        parts = raw.split(",")
        if len(parts) != 3:
            print("Invalid syntax")
            continue

        values: list[float] = []
        invalid = False
        for part in parts:
            clean = part.strip()
            try:
                values.append(float(clean))
            except ValueError as error:
                print(f"Error on parameter '{clean}': {error}")
                invalid = True
                break

        if invalid:
            continue
        return (values[0], values[1], values[2])


def distance_to_center(pos: Coordinate) -> float:
    return math.sqrt(pos[0] ** 2 + pos[1] ** 2 + pos[2] ** 2)


def distance_between(pos1: Coordinate, pos2: Coordinate) -> float:
    return math.sqrt((pos2[0] - pos1[0]) ** 2 +
                     (pos2[1] - pos1[1]) ** 2 +
                     (pos2[2] - pos1[2]) ** 2)


def main() -> None:
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    first = get_player_pos()

    print(f"Got a first tuple: {first}")
    print(f"It includes: X={first[0]}, Y={first[1]}, Z={first[2]}")
    print(f"Distance to center: {round(distance_to_center(first), 4)}")

    print("Get a second set of coordinates")
    second = get_player_pos()
    print("Distance between the 2 sets of coordinates: "
          f"{round(distance_between(first, second), 4)}")


if __name__ == "__main__":
    main()
