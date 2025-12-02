# Data Analysis Functions - Student Submission

**Author:** John Smith  
**Date:** November 15, 2025  
**Course:** CS 101 - Introduction to Programming

## Overview

This submission contains a collection of functions for performing basic data analysis and statistical calculations on lists of numbers.

## File Structure

- `math_functions.py` - Contains basic mathematical operations (average, max, min)
- `stats_functions.py` - Contains statistical analysis functions (median, range)

## Functions Implemented

### math_functions.py

1. **calculate_average(numbers)** - Calculates the arithmetic mean of a list of numbers
2. **find_max(numbers)** - Finds the maximum value in a list
3. **find_min(numbers)** - Finds the minimum value in a list

### stats_functions.py

1. **calculate_median(numbers)** - Calculates the median value of a list of numbers
2. **calculate_range(numbers)** - Calculates the range (difference between max and min)

## Usage Example

```python
from math_functions import calculate_average, find_max, find_min
from stats_functions import calculate_median, calculate_range

data = [10, 5, 8, 12, 3, 7]

print(f"Average: {calculate_average(data)}")
print(f"Max: {find_max(data)}")
print(f"Min: {find_min(data)}")
print(f"Median: {calculate_median(data)}")
print(f"Range: {calculate_range(data)}")
```

## Error Handling

All functions raise a `ValueError` if provided with an empty list.

## Testing

Functions have been tested with various input cases including:
- Normal lists of integers and floats
- Lists with negative numbers
- Single-element lists
- Empty lists (to verify error handling)

## Notes

I split the functions into two modules to organize them by category - basic math operations vs. statistical operations. This makes the code more maintainable and easier to navigate.
