def player_creator(
        name: str, score: int, achievements: list, region: str, status: bool
        ) -> dict:
    player = {
        "name": name,
        "score": score,
        "achievements": achievements,
        "region": region,
        "status": status
    }
    return player


def main() -> None:
    players = [
        player_creator("alice", 4600, [
            'first kill', 'level 10', 'boss slayer', 'double kill'
            ], 'north', True),
        player_creator("bob", 3600, [
            'first kill', 'level 10', 'boss slayer', 'treasure found'
            ], 'east', True),
        player_creator("charlie", 4600, [
            'first kill', 'level 10', 'level 15', 'boss slayer', 'double kill'
            ], 'west', True),
        player_creator("diana", 4100, [
            'first kill', 'level 10', 'boss slayer', 'max score', 'jungler'
            ], 'south', True),
        player_creator("eva", 1500, [
            'first kill', 'boss slayer', 'double kill', 'demonized'
            ], 'north', True)
    ]

    print('=== Game Analytics Dashboard ===\n')
    print('=== List Comprehension Exampls ===')

    high_scores = [
        player["name"] for player in players if player["score"] > 2000
    ]
    scores_doubled = [
        player["score"] * 2 for player in players
    ]
    active_players = [
        player["name"] for player in players if player["status"]
    ]

    print(f'High scores (>2000): {high_scores}')
    print(f'Scores doubled: {scores_doubled}')
    print(f'Active players: {active_players}')

    print('\n=== Dict Comprehension Examples ===')

    player_scores = {
        player["name"]: player["score"] for player in players
    }
    scores_cats = {
        "high": len([player for player in players if player["score"] > 4000]),
        "medium": len([
            player for player in players if player["score"] > 3000
            ]),
        "low": len([player for player in players if player["score"] < 3000])
    }
    achiev_count = {
        player["name"]: len(player["achievements"]) for player in players
    }

    print(f'Player scores: {player_scores}')
    print(f'Score categories: {scores_cats}')
    print(f'Achievement counts: {achiev_count}')

    print('\n=== Set Comprehension Examples ===')

    unique_players = {
        player["name"] for player in players
    }
    unique_achievements = {
        achievement for player in players for achievement in player[
            "achievements"
            ]
    }
    active_regions = {
        player["region"] for player in players
    }

    print(f'Unique players: {unique_players}')
    print(f'Unique achievements: {unique_achievements}')
    print(f'Active regions: {active_regions}')

    print('\n=== Combined Analysis ===')
    print(f'Total players: {len(players)}')
    print(f'Total unique achievements: {len(unique_achievements)}')
    print('Average score: '
          f'{sum(player["score"] for player in players) / len(players):.1f}')
    top_player = max(player_scores, key=lambda name: player_scores[name])
    print(f'Top performer: {top_player} ({player_scores[top_player]} points)')


if __name__ == "__main__":
    main()
