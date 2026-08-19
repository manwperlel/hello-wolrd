"""
======================================================================
Python Fundamentals & Syntax Reference Guide
======================================================================

1. BUILT-IN FUNCTIONS
----------------------------------------------------------------------
print()   -> Outputs data to the standard console.
input()   -> Prompts the user for text input (returns a string).
type()    -> Identifies the data type of a value or variable.
len()     -> Calculates the length/count of items in a string or collection.
int()     -> Converts a compatible value to an integer (whole number).
float()   -> Converts a value to a floating-point number (decimal).
str()     -> Converts a value to its string representation.

2. ARITHMETIC OPERATORS
----------------------------------------------------------------------
+   -> Addition (also concatenates strings)
-   -> Subtraction
*   -> Multiplication (also repeats strings)
/   -> Division (always returns a float)
//  -> Floor division (truncates decimals, rounds down)
%   -> Modulo (returns the remainder of division)
**  -> Exponentiation (raises to the power of)

3. COMPARISON OPERATORS (Evaluate to True or False)
----------------------------------------------------------------------
>   -> Greater than
<   -> Less than
>=  -> Greater than or equal to
<=  -> Less than or equal to
==  -> Equal to
!=  -> Not equal to (different)

4. LOGICAL OPERATORS
----------------------------------------------------------------------
and  -> Returns True if both conditions evaluate to True.
or   -> Returns True if at least one condition evaluates to True.
not  -> Inverts the boolean result (True becomes False, and vice versa).

5. CONTROL FLOW (Conditional Statements)
----------------------------------------------------------------------
if    -> Executes a block of code if its condition is True.
elif  -> (Else If) Evaluates an alternative condition if preceding ones were False.
else  -> Fallback block; executes if none of the above conditions were met.

6. LOOPS & ACCUMULATORS
----------------------------------------------------------------------
while -> Repeats a code block as long as a condition remains True.
+=    -> In-place addition operator (e.g., x += 1 increments x by 1).

7. DATA TYPES & LITERAL EXAMPLES
----------------------------------------------------------------------
"""

# Type checking examples:
print(type("I am a string"))          # Type 'str'
print(type(42))                        # Type 'int'
print(type(3.14159))                   # Type 'float'
print(type(3 + 4j))                    # Type 'complex'
print(type(True))                      # Type 'bool'
print(type(print("Hello, world!")))    # Type 'NoneType'