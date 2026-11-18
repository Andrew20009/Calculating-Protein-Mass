MONOISOTOPIC_MASS = { # Monoisotopic mass of each amino acid residue
    "A": 71.03711,  "C": 103.00919, "D": 115.02694, "E": 129.04259,
    "F": 147.06841, "G": 57.02146,  "H": 137.05891, "I": 113.08406,
    "K": 128.09496, "L": 113.08406, "M": 131.04049, "N": 114.04293,
    "P": 97.05276,  "Q": 128.05858, "R": 156.10111, "S": 87.03203,
    "T": 101.04768, "V": 99.06841,  "W": 186.07931, "Y": 163.06333,
}


def read_protein_from_txt(file_path: str) -> str: # Reads the protein string from the file
    with open(file_path) as f: # Open the file for reading
        return "".join(line.strip() for line in f).upper() # Join all lines, drop whitespace, uppercase


def protein_mass(protein: str) -> float: # Sums the mass of every amino acid in the protein
    total = 0.0 # Start the running total at zero
    for amino_acid in protein: # Go through each letter in the protein string
        if amino_acid not in MONOISOTOPIC_MASS: # Catch letters that are not amino acids
            raise ValueError(f"Unknown amino acid: {amino_acid!r}")
        total += MONOISOTOPIC_MASS[amino_acid] # Add this amino acid's mass to the total
    return total # Return the total weight of the protein


def main() -> None:
    protein = read_protein_from_txt("rosalind_prtm.txt") # Read the protein string
    print(f"{protein_mass(protein):.3f}") # Print the total mass to the thousandths place


if __name__ == "__main__": # # Only run main() when this file is executed directly
    main()
