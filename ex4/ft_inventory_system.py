import sys


def parse_inventory(args: list[str]) -> tuple[dict[str, int], list[str]]:
    inventory: dict[str, int] = {}
    order: list[str] = []

    for parameter in args:
        if parameter.count(":") != 1:
            print(f"Error - invalid parameter '{parameter}'")
            continue

        item, raw_quantity = parameter.split(":")
        if item in inventory:
            print(f"Redundant item '{item}' - discarding")
            continue

        try:
            quantity = int(raw_quantity)
        except ValueError as error:
            print(f"Quantity error for '{item}': {error}")
            continue

        inventory[item] = quantity
        order.append(item)

    return inventory, order


def find_most_abundant(inventory: dict[str, int], order: list[str]) -> str:
    best = order[0]
    for item in order[1:]:
        if inventory[item] > inventory[best]:
            best = item
    return best


def find_least_abundant(inventory: dict[str, int], order: list[str]) -> str:
    best = order[0]
    for item in order[1:]:
        if inventory[item] < inventory[best]:
            best = item
    return best


def main() -> None:
    print("=== Inventory System Analysis ===")

    inventory, order = parse_inventory(sys.argv[1:])
    print(f"Got inventory: {inventory}")
    print(f"Item list: {list(inventory.keys())}")

    total_quantity = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total_quantity}")

    if total_quantity > 0:
        for item, quantity in inventory.items():
            percent = round((quantity * 100) / total_quantity, 1)
            print(f"Item {item} represents {percent}%")

    if len(order) > 0:
        most_abundant = find_most_abundant(inventory, order)
        least_abundant = find_least_abundant(inventory, order)
        print("Item most abundant: "
              f"{most_abundant} with quantity {inventory[most_abundant]}")
        print("Item least abundant: "
              f"{least_abundant} with quantity {inventory[least_abundant]}")

    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    main()
