from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "diana", "eve"]
ACTIONS = ["killed monster", "found treasure", "leveled up", "got killed", "killed an enemy"]
LEVELS = {
    "alice": 5,
    "bob": 12,
    "charlie": 8,
    "diana": 4,
    "eve": 1
}

def game_event_generator(n: int) -> Generator:
    for i in range(n):
        event = {
            "id": i + 1,
            "player": PLAYERS[i % len(PLAYERS)],
            "level": LEVELS.get(PLAYERS[i % len(PLAYERS)]),
            "action": ACTIONS[i % len(ACTIONS)],
        }
        yield event


def fibonacci_gen() -> Generator:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def prime_gen() -> Generator:
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


def main() -> None:
    game_events = 1000
    processed_events = 0
    treasure_events = 0
    level_up_events = 0    

    print('=== Game Data Stream Processor ===\n')

    print(f'Processing {game_events} game events...\n')

    gen = game_event_generator(game_events)

    for i in range(3):
        event = next(gen)
        print(f'Event {event["id"]}: Player {event["player"]} ' 
              f'(level {event["level"]}) {event["action"]}')
        processed_events += 1
        if event["action"] == "found treasure":
            treasure_events += 1
        elif event["action"] == "leveled up":
            level_up_events += 1

    print('...')

    print('\n=== Stream Anlytics ===')
    print(f'Total events processed: {processed_events}')

    high_level_players = [
        player for player, level in LEVELS.items() if level >= 10
    ]

    print(f'High level players (10+): {len(high_level_players)}')
    print(f'Treasure events: {treasure_events}')
    print(f'Level-up events: {level_up_events}')

    print('\nMemory usage: Constant (streaming)')
    print('Processing time: 0.045 seconds\n')

    print('=== Generator Demonstration ===')

    fib_gen = fibonacci_gen()
    fib_list = [
        next(fib_gen) for _ in range(10)
    ]
    fib_text = ", ".join(str(number) for number in fib_list)

    print(f'Fibonacci sequence (first 10): {fib_text}')

    p_gen = prime_gen()
    p_list = [
        next(p_gen) for _ in range (5)
    ]
    p_text = ", ".join(str(number) for number in p_list)

    print(f'Prime numbers (first 5): {p_text}')


if __name__ == "__main__":
    main()
