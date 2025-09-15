def sort(width: int, height: int, length: int, mass: int) -> str:
    """
    Classify a package into the correct stack based on its dimensions and mass.

    Args:
        width (int): Width of the package in cm
        height (int): Height of the package in cm
        length (int): Length of the package in cm
        mass (int): Mass of the package in kg

    Returns:
        str: One of "STANDARD", "SPECIAL", or "REJECTED"
    """
    volume = width * height * length
    bulky = volume >= 1_000_000 or (width >= 150 or height >= 150 or length >= 150)
    heavy = mass >= 20

    if bulky and heavy:
        return "REJECTED"
    return "SPECIAL" if bulky or heavy else "STANDARD"


if __name__ == "__main__":
    # Quick demo run like sample test cases
    demo_cases = [
        (100, 100, 100, 10),
        (200, 50, 30, 10),
        (50, 50, 50, 25),
        (200, 200, 200, 25),
        (149, 149, 149, 19),
        (150, 149, 149, 19),
        (100, 100, 100, 20),
    ]

    for w, h, l, m in demo_cases:
        print(f"sort({w}, {h}, {l}, {m}) -> {sort(w, h, l, m)}")
