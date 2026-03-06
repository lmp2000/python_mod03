from sys import argv

class ScoreError(Exception):
    pass


def main() -> None:
    print("=== Player Score Analytics ===")
    if len(argv) < 2:
        raise ScoreError("No scores provided: Usage: "
                        "python3 ft_score_analytics.py <score1> <score2> ...")
    scores = get_scores(argv)
    players = len(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / players}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")



def get_scores(input: list) -> list:
    scores = []
    for score in input[1:]:
        try:
            scores.append(int(score))
        except ValueError as e:
            pass
    return scores


if __name__ == "__main__":
    try:
        main()
    except ScoreError as e:
        print(e)