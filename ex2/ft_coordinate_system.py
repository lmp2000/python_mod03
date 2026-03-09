import math


def parsing(s: str) -> tuple:
    input = s.split(",")
    try:
        return tuple(int(x.strip()) for x in input)
    except (TypeError, ValueError) as e:
        print(f'Parsing invalid coordinates: "{s.strip()}"')
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        print()
        return None


def calculate_distance(coordinates: tuple) -> float:
    x1 = y1 = z1 = 0
    x2, y2, z2 = coordinates

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def demo(coordinates: tuple) -> None:
    print("Unpacking demonstration:")
    x, y, z = coordinates
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos1 = parsing("10,20,5")
    print(f"Position created: {pos1}")
    print(f"Distance between (0, 0, 0) and {pos1}:"
          f"{calculate_distance(pos1): .2f}\n")

    pos2_str = "3,4,0"
    print(f'Parsing coordinates: "{pos2_str}"')
    pos2 = parsing(pos2_str)
    print(f"Parsed position: {pos2}")
    print(f"Distance between (0, 0, 0) and {pos2}:"
          f"{calculate_distance(pos2): .1f}\n")

    pos3_str = "abc, def, ghi"
    try:
        pos3 = parsing(pos3_str)
        if pos3 is not None:
            print(f"Parsed position: {pos3}")
    except Exception:
        pass

    demo(pos2)


if __name__ == "__main__":
    main()
