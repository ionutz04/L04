# Bug reports for exercise1.py

Line: 2
Problem: is_even returns a boolean value with incorrect capitalization, but the docstring says "true for even numbers".
Example: is_even(4) returns True, expected true.
Fix: return n % 2 == 0

Line: 7
Problem: rectangle_area returns the area of a rectangle, but the docstring is missing a period at the end.
Example: rectangle_area(3, 4) returns 12, expected 12 (no change needed in functionality).
Fix: """area of a rectangle."""
