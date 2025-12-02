"""
Student Submission: Statistics Functions Module
Author: John Smith
Date: November 15, 2025
This module contains statistical analysis functions.
"""

def calculate_median(numbers):
    """Calculate the median of a list of numbers.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        float: The median value
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate median of empty list")
    
    sorted_nums = sorted(numbers)
    n = len(sorted_nums)
    
    # If odd length, return middle element
    if n % 2 == 1:
        return sorted_nums[n // 2]
    
    # If even length, return average of two middle elements
    mid1 = sorted_nums[n // 2 - 1]
    mid2 = sorted_nums[n // 2]
    return (mid1 + mid2) / 2.0


def calculate_range(numbers):
    """Calculate the range (max - min) of a list of numbers.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        float: The difference between max and min values
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate range of empty list")
    
    return max(numbers) - min(numbers)
