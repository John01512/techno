import numpy as np


def chinese_remainder_theorem(residues, moduli):
    # Check if the lengths of residues and moduli are the same
    if len(residues) != len(moduli):
        raise ValueError("Number of residues must equal number of moduli")

    n = len(residues)

    # Compute the product of all moduli
    N = np.prod(moduli)

    # Compute the array of Ni values
    Ni = [int(N // moduli[i]) for i in range(n)]  # Convert to regular Python integers

    # Compute the array of Mi values (inverse of Ni modulo moduli[i])
    Mi = [pow(Ni[i], -1, moduli[i]) for i in range(n)]

    # Compute the solution using the Chinese Remainder Theorem formula
    solution = sum(residues[i] * Ni[i] * Mi[i] for i in range(n)) % N

    return solution

# Example usage
residues = [2, 3, 2]
moduli = [3, 5, 7]

solution = chinese_remainder_theorem(residues, moduli)
print("Solution:", solution)