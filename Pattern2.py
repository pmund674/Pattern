def print_inverted_pattern(rows):
  """Prints an inverted pyramid pattern of asterisks.

  Args:
    rows: The number of rows in the pattern.
  """

  for i in range(rows, 0, -1):
    # Print spaces before the asterisks
    for j in range(rows - i):
      print(" ", end="")

    # Print asterisks
    for k in range(2 * i - 1):
      print("*", end="")

    # Move to the next line
    print()

# Get the number of rows from the user
rows = int(input("Enter the number of rows: "))

# Print the inverted pattern
print_inverted_pattern(rows)
