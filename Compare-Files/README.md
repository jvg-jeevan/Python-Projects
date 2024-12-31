# File Comparison Using SHA-1 Hashing

This program compares two files to determine if they are identical by computing their SHA-1 hash values. It reads the files in chunks to handle large files efficiently and compares the hash values for equality.

## Algorithm

The algorithm follows these steps to compare two files:

1. **Initialize SHA-1 Hashers**:  
   Create two SHA-1 hash objects (`h1` and `h2`).

2. **Compute Hash for the First File**:  
   - Open the first file (`fileName1`) in binary read mode.
   - Read the file in chunks of 1024 bytes.
   - Update the hash object `h1` with each chunk until the entire file is processed.

3. **Compute Hash for the Second File**:  
   - Open the second file (`fileName2`) in binary read mode.
   - Read the file in chunks of 1024 bytes.
   - Update the hash object `h2` with each chunk until the entire file is processed.

4. **Compare Hashes**:  
   - If the hash values (`h1.hexdigest()` and `h2.hexdigest()`) of the two files are not equal, print "These files are not identical".
   - Otherwise, print "These files are identical".

## Pseudocode

```plaintext
Function CompareFiles(fileName1, fileName2):
    Initialize h1 as SHA-1 hash object
    Initialize h2 as SHA-1 hash object

    Open fileName1 in binary read mode:
        While file has remaining data:
            Read a 1024-byte chunk from file
            Update h1 with the chunk

    Open fileName2 in binary read mode:
        While file has remaining data:
            Read a 1024-byte chunk from file
            Update h2 with the chunk

    If h1.hexdigest() is not equal to h2.hexdigest():
        Print "These files are not identical"
    Else:
        Print "These files are identical"
```

## How It Works
1. The program uses Python's `hashlib` library to compute the SHA-1 hash of both files.
2. The files are read in chunks of 1024 bytes to avoid memory overload, especially for large files.
3. The program then compares the hash values of both files. If they match, the files are identical; if not, they are different.

## Requirements
- Python 3.x
- No additional libraries are required aside from the built-in `hashlib`.

## Usage

1. Ensure that the two files you wish to compare are available.
2. Modify the file paths in the program (in the `hash_file` function).
3. Run the program.

```bash
python compare_files.py
```

### Example Output:

If the files are identical:
```bash
These files are identical
```

If the files are not identical:
```bash
These files are not identical
```

## Complexity Analysis

| **Operation**  | **Best Case** | **Average Case** | **Worst Case** |
|----------------|---------------|------------------|----------------|
| **Time Complexity**  | O(n)  | O(n)             | O(n)           |
| **Space Complexity** | O(1)  | O(1)             | O(1)           |

Where `n` is the size of the file being read. The time complexity is proportional to the size of the file, as it reads the file in chunks. The space complexity is constant, as the program only stores the hashes in memory.



### Explanation of Sections:

- **Algorithm**: A clear breakdown of the program’s logic in bullet points, followed by pseudocode to describe the steps in a high-level format.
- **How It Works**: A concise explanation of the core steps and libraries used in the program.
- **Complexity Analysis**: A table summarizing the time and space complexities of the algorithm.
- **Example Output**: Shows typical outputs for matching and non-matching files.

This README is designed to help users understand both how the program works and how to use it efficiently. It also includes information about the algorithm, ensuring that it can be easily followed by developers or users who wish to modify or extend the program.
