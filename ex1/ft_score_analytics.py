import sys


def parse_scores(args: list[str]) -> list[int]:
    scores: list[int] = []
    for parameter in args:
        try:
            scores.append(int(parameter))
        except ValueError:
            print(f"Invalid parameter: '{parameter}'")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    scores = parse_scores(sys.argv[1:])
    if len(scores) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    total_score = sum(scores)
    players = len(scores)

    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {total_score}")
    print(f"Average score: {total_score / players}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
