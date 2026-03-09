def inventory_master() -> None:
    print("=== Inventory System Analysis ===\n")
    inventory = {
        "potion": {"name": "potion", "type": "moderate",
                   "quantity": 5, "value": 5},
        "armor": {"name": "armor", "type": "scarce",
                  "quantity": 3, "value": 3},
        "shield": {"name": "shield", "type": "scarce",
                   "quantity": 2, "value": 2},
        "sword": {"name": "sword", "type": "scarce",
                  "quantity": 1, "value": 1},
        "helmet": {"name": "helmet", "type": "scarce",
                   "quantity": 1, "value": 1}
    }

    total = sum(item["quantity"] for item in inventory.values())
    print(f'Total items in inventory: {total}')
    print(f'Unique items types: {len(inventory)}')

    print('\n=== Current Inventory ===')
    for item in inventory.values():
        if item["quantity"] > 1:
            print(f'{item["name"]}: {item["quantity"]} '
                  f'units ({item["quantity"]/total:.1%})')
        else:
            print(f'{item["name"]}: {item["quantity"]} '
                  f'unit ({item["quantity"]/total:.1%})')

    print('\n=== Inventory Statistics ===')
    abundant = max(inventory.values(), key=lambda item: item["quantity"])
    least = min(inventory.values(), key=lambda item: item["quantity"])
    print(f'Most abundant: {abundant["name"]} ({abundant["quantity"]} units)')
    print(f'Least abundant: {least["name"]} ({least["quantity"]} unit)')

    print('\n=== Item Categories ===')
    categories: dict[str, dict[str, int]] = {}
    for key, item in inventory.items():
        cat = item["type"]
        categories.setdefault(cat, {})[key] = item["quantity"]
    print(f"Moderate: {categories.get('moderate')}")
    print(f"Scarce: {categories.get('scarce')}")

    print('\n=== Management Suggestions ===')
    low_stock = ', '.join(
        item["name"] for item in inventory.values() if item["quantity"] <= 1
        )
    print(f'Restock needed: {low_stock}')

    print('\n=== Dictionary Properties Demo ===')
    items = inventory.keys()
    keys_text = ", ".join(items)
    values_text = ", ".join(str(inventory[k]["value"]) for k in inventory)
    print(f'Dictionary keys: {keys_text}')
    print(f'Dictionary values: {values_text}')
    print(f"Sample lookup - 'sword' in inventory: {'sword' in inventory}")


if __name__ == "__main__":
    inventory_master()
