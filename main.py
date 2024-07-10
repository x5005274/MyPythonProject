def find_and_reverse_duplicates(strings):
  seen = {}  # Dictionary to keep track of seen strings
  duplicates = []  # List to store found duplicates
  all_letters = set()  # Set to store all unique letters from all strings

  # Traverse each string in the list
  for string in strings:
      if string in seen:
          if seen[string] == 1:  # First time encountering this string as duplicate
              duplicates.append(string)  # Add to duplicates list
      else:
          seen[string] = 1

      # Add all letters of the current string to all_letters set
      all_letters.update(string)

  # Reverse the duplicate strings
  reversed_duplicates = [s[::-1] for s in duplicates]

  return reversed_duplicates, sorted(all_letters)

# Example usage:
if __name__ == "__main__":
  strings = ["apple", "banana", "apple", "orange", "banana", "pear"]

  reversed_duplicates, all_letters = find_and_reverse_duplicates(strings)

  print("Original List of Strings:", strings)
  print("Found Duplicate Strings (Reversed):", set(reversed_duplicates))
  print("All Unique Letters in Input Strings:", all_letters)
