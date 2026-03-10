import sys


def main() -> None:
    print("=== Command Quest ===")

    argc = len(sys.argv)

    if argc <= 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
    elif argc > 1:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {argc - 1}")
        for i, string in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {string}")

    print(f"Total arguments: {argc}")


if __name__ == "__main__":
    main()
