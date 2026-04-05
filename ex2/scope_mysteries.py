from typing import Callable, Dict


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_value: int) -> Callable:
    total = initial_value

    def accumulator(value: int) -> int:
        nonlocal total
        total += value
        return total

    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchant(item: str):
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> Dict[str, Callable]:
    memory = {}

    def store(key: str, value: str) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        return memory.get(key, "Memory not found")

    return {"store": store,
            "recall": recall}


def main() -> None:
    print("\nTesting mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()

    print(f"counter_a call 1: {counter_a()}")
    print(f"counter_a call 2: {counter_a()}")
    print(f"counter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    add1 = 20
    add2 = 30
    accumulator_a = spell_accumulator(base)

    print(f"Base {base}, add {add1}: {accumulator_a(add1)}")
    print(f"Base {base}, add {add2}: {accumulator_a(add2)}")

    print("\nTesting enchantment factory...")
    fire_enchant = enchantment_factory("Flaming")
    ice_enchant = enchantment_factory("Frozen")

    print(fire_enchant('Sword'))
    print(ice_enchant('Shield'))

    print("\nTesting memory vault...")
    vault = memory_vault()

    vault["store"]("secret", 42)
    print("Store 'secret' = 42")
    print("Recall 'secret':", vault["recall"]("secret"))
    print("Recall 'unknown':", vault["recall"]("unknown"))


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
