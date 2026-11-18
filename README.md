# Calculating Protein Mass

## OVERVIEW
This program calculates the total weight of a protein string by adding up the monoisotopic mass of every amino acid in it.
It is a solution to the **"Calculating Protein Mass"** Rosalind problem **(ID: PRTM)**. The tool is simple, efficient, and ideal for practicing dictionaries, loops, file handling, and number formatting in Python.

---

## FEATURES
- Reads a protein string from a file (`rosalind_prtm.txt`), joining it into one string even if it is split across several lines
- Looks up each amino acid in a dictionary built from the monoisotopic mass table
- Adds every amino acid's mass into a total mass
- Raises a clear error if the string contains a letter that is not one of the 20 amino acids
- Prints the total mass rounded to the thousandths place (3 decimal places)
- Clean, well-commented code with proper functions and type hints

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input file with name rosalind_prtm.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_prtm.txt):
```
SKADYEK
```
**Output:**
```
821.392
```

---

## HOW IT WORKS
1. The program reads the protein string from the file, removing whitespace and line breaks
2. It goes through the string one letter at a time
3. Each letter is looked up in the monoisotopic mass dictionary
4. The mass of each amino acid is added to a running total
5. Finally, it prints the total mass rounded to the thousandths place

---

## TECHNOLOGIES USED
- **Python**
- **TXT File**
