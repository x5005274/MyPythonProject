def find_and_reverse_duplicates(strings):
    seen = {}  # Dictionary to keep track of seen strings
    duplicates = []  # List to store found duplicates

    # Traverse each string in the list
    for string in strings:
        if string in seen:
            if seen[string] == 1:  # First time encountering this string as duplicate
                duplicates.append(string)  # Add to duplicates list
            seen[string] += 1
        else:
            seen[string] = 1

    # Reverse the duplicate strings
    reversed_duplicates = [s[::-1] for s in duplicates]

    return reversed_duplicates

# Example usage:
if __name__ == "__main__":
    strings = ["apple", "banana", "apple", "orange", "banana", "pear"]

    reversed_duplicates = find_and_reverse_duplicates(strings)

    print("Original List of Strings:", strings)
    print("Found Duplicate Strings:", set(reversed_duplicates))
