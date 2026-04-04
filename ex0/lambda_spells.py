from typing import Dict, List


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    if not artifacts or not isinstance(artifacts, list):
        return []
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    if not mages or not isinstance(mages, list):
        return []
    return list(filter(lambda mage: mage["power"] >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    if not spells or not isinstance(spells, list):
        return []
    return list(map(lambda spell: "* "+spell+" *", spells))


def mage_stats(mages: List[Dict]) -> Dict:
    if not mages or not isinstance(mages, list):
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    max_power = max(mages, key=lambda x: x["power"])["power"] if mages else 0
    min_power = min(mages, key=lambda x: x["power"])["power"] if mages else 0
    avg_power = float(sum(mage["power"] for mage in mages) / len(mages)
                      if mages else 0)
    return {"max_power": max_power,
            "min_power": min_power,
            "avg_power": round(avg_power, 2)}


def main() -> None:
    print("\nTesting artifact sorter...")
    artifacts = [
        {"name": "Fire Staff", "power": 80, "type": "Staff"},
        {"name": "Crystal Orb", "power": 60, "type": "Orb"}
    ]
    sorted_artifacts = artifact_sorter(artifacts)
    for artifact in sorted_artifacts:
        print(f"{artifact['name']} ({artifact['power']} power)", end="")
        if artifact != sorted_artifacts[-1]:
            print(" comes before ", end="")

    print("\n\nTesting spell transformer...")
    spells = ["fireball", "heal", "sheild"]
    transformed_spells = spell_transformer(spells)
    for spell in transformed_spells:
        print(spell, end="")
        if spell != transformed_spells[-1]:
            print(" ", end="")
    print()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
