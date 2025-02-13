# ZeroDivisionError in Python

This repository demonstrates a common error in Python: the `ZeroDivisionError`.  The provided code attempts to divide by zero, resulting in this exception. A solution is also provided to handle this scenario gracefully.

## Bug Description

The `my_function` attempts to perform division without checking for a zero denominator. When `b` is 0, this results in a `ZeroDivisionError`.

## Solution

The solution includes a check to prevent division by zero. This is done by adding a conditional statement that handles the case when the denominator is zero, either by returning a default value, raising a custom exception, or skipping the operation.