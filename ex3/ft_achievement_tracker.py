import random


ACHIEVEMENTS = [
    "First Steps",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "World Savior",
    "Crafting Genius",
    "Strategist",
    "Sharp Mind",
    "Unstoppable",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    wanted = random.randint(5, 9)
    picked: set[str] = set()
    while len(picked) < wanted:
        picked.add(random.choice(ACHIEVEMENTS))
    return picked


def main() -> None:
    print("=== Achievement Tracker System ===")

    players = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, data in players.items():
        print(f"Player {name}: {data}")

    player_sets = list(players.values())
    all_distinct = set.union(*player_sets)
    common = set.intersection(*player_sets)

    print(f"All distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")

    for name, data in players.items():
        others_union = set()
        for other_name, other_data in players.items():
            if other_name != name:
                others_union = others_union.union(other_data)
        print(f"Only {name} has: {data.difference(others_union)}")

    for name, data in players.items():
        print(f"{name} is missing: {set(ACHIEVEMENTS).difference(data)}")


if __name__ == "__main__":
    main()
