import random
from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "dylan"]
ACTIONS = [
    "run", "eat", "sleep", "grab", "move",
    "climb", "swim", "release", "use",
]


def gen_event() -> Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
    events: list[tuple[str, str]],
) -> Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        index = random.randint(0, len(events) - 1)
        yield events.pop(index)


def main() -> None:
    print("=== Game Data Stream Processor ===")

    event_stream = gen_event()
    for index in range(1000):
        player, action = next(event_stream)
        print(f"Event {index}: Player {player} did action {action}")

    ten_events = [next(gen_event()) for _ in range(10)]
    print(f"Built list of 10 events: {ten_events}")

    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")


if __name__ == "__main__":
    main()
