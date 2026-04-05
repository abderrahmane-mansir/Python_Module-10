from typing import List, Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combined(target: str, power: int) -> tuple:
        return (
            spell1(target, power),
            spell2(target, power)
        )
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified_spell(target: str, power: int):
        return base_spell(target, power * multiplier)

    return amplified_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def conditional(target: str, power: int) -> str:
        if condition(target, power):
            return spell(target, power)
        return "Spell fizzled"
    return conditional


def spell_sequence(spells: List[Callable]) -> Callable:
    def sequence(target: str, power: int) -> List[str]:
        return [spell(target, power) for spell in spells]
    return sequence


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heals restores {target} for {power} HP"


def main() -> None:
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    combined_result = combined("Dragon", 10)
    print(
        f"Combined spell result: {combined_result[0]}, {combined_result[1]}"
    )

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    original_result = fireball("Dragon", 10)
    amplified_result = mega_fireball("Dragon", 10)
    print(f"Original: {original_result}, Amplified: {amplified_result}")

    print("\nTesting conditional caster...")
    sep = conditional_caster(lambda t, p: p > 15, fireball)
    print(f"Conditional cast: {sep('Goblin', 5)}")
    print(f"Conditional cast: {sep('Goblin', 20)}")

    seq = spell_sequence([fireball, heal])
    for target in ["Knight", "Wizard"]:
        print(f"\nSpell sequence on {target}:")
        results = seq(target, 12)
        for res in results:
            print(res)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
