from functools import lru_cache, reduce, partial, singledispatch
import operator
from typing import Any, Callable, Dict, List


def spell_reducer(spells: List[int], operation: str) -> int:
    if not spells:
        return 0

    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in ops:
        raise ValueError("Unknown operation")

    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> Dict[str, Callable]:
    return {
        "fire": partial(base_enchantment, 50, "Fire"),
        "ice": partial(base_enchantment, 50, "Ice"),
        "lightning": partial(base_enchantment, 50, "Lightning")
    }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> Callable[[Any], str]:

    @singledispatch
    def dispatch(spell):
        return "Unknown spell type"

    @dispatch.register
    def _(spell: int):
        return f"Damage spell: {spell} damage"

    @dispatch.register
    def _(spell: str):
        return f"Enchantment: {spell}"

    @dispatch.register
    def _(spell: list):
        return f"Multi-cast: {len(spell)} spells"

    return dispatch


def main() -> None:
    print("\nTesting spell reducer...")
    spell_powers = [10, 20, 30, 40]
    result = spell_reducer(spell_powers, "add")
    print(f"Sum: {result}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")
    print(f"Min: {spell_reducer(spell_powers, 'min')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fibonacci(10): {memoized_fibonacci(0)}")
    print(f"Fibonacci(10): {memoized_fibonacci(1)}")
    print(f"Fibonacci(10): {memoized_fibonacci(10)}")
    print(f"Fibonacci(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(f"{dispatcher(42)}")
    print(f"{dispatcher('fireball')}")
    print(f"{dispatcher(['Fireball', 'Ice Storm', 'Lightning Bolt'])}")
    print(f"{dispatcher({'type': 'unknown'})}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
