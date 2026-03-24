import random


def main() -> None:
    print("=== Game Data Alchemist ===")

    players = [
        "Alice", "bob", "Charlie", "dylan", "Emma",
        "Gregory", "john", "kevin", "Liam",
    ]

    all_capitalized = [name.capitalize() for name in players]
    initially_capitalized = [name for name in players if name[0].isupper()]

    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capitalized}")
    print(f"New list of capitalized names only: {initially_capitalized}")

    scores = {name: random.randint(0, 1000) for name in all_capitalized}
    average = round(sum(scores.values()) / len(scores), 2)
    high_scores = {
        name: score for name, score in scores.items() if score > average
    }

    print(f"Score dict: {scores}")
    print(f"Score average is {average}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
