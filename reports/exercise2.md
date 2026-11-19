# Bug reports for exercise2.py

Line: 3
Problem: is_passing returns False for a grade of exactly 5, but the docstring says "5 or more".
Example: is_passing(5) returns False, expected True.
Fix: return grade >= 5

Line: 8
Problem: is_valid_password returns False for passwords that are exactly 8 characters long, but the docstring says "At least 8 characters".
Example: is_valid_password("12345678") returns False, expected True.
Fix: return len(password) >= 8 and any(c.isdigit() for c in password)

Line: 13
Problem: clamp does not correctly limit x to the range from low to high, as it uses 'low' instead of 'high' in the min function.
Example: clamp(10, 5, 8) returns 5, expected 8.
Fix: return max(low, min(x, high))
