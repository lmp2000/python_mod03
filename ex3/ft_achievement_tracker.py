class Player:
    def __init__(self, name: str) -> None:
        self.name = name
        self.achievements = set()

    def add_achievements(self, *achievements: str) -> None:
        self.achievements.update(achievements)

def main() -> None:
    print("=== Achievement Tracker System ===\n")

    alice = Player("Alice")
    bob = Player("Bob")
    charlie = Player("Charlie")
    players = [alice, bob, charlie]

    alice.add_achievements('first_kill', 'level_10', 'treasure_hunter', 'speed_demon')
    bob.add_achievements('first_kill', 'level_10', 'boss_slayer', 'coletor')
    charlie.add_achievements('level_10', 'trasure_hunter', 'boss_slayer',
                             'speed_demon', 'perfectionist')

    for player in players:
        print(f"Player {player.name} achievements: {player.achievements}")

    a, b, c = [player.achievements for player in players]

    print("\n=== Achievement Analytics ===")
    print(f'All unique achievements: {a | b | c}')
    print(f'Total unique achievements: {len(a | b | c)}\n')

    print(f'Common to all players: {a & b & c}')
    print(f'Rare achievements (1 player): {a ^ b ^ c}\n')

    print(f'Alice vs Bob common: {a & b}')
    print(f'Alice unique: {a - b}')
    print(f'Bob unique: {b - a}')


if __name__ == "__main__":
    main()