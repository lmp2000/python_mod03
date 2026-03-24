import sys


def main() -> None:
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")

    arguments = sys.argv[1:]
    if len(arguments) == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {len(arguments)}")
        for index, value in enumerate(arguments, start=1):
            print(f"Argument {index}: {value}")

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
