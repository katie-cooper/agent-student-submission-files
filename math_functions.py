"""
Student Submission: Math Functions Module
Author: John Smith
Date: November 15, 2025
This module contains mathematical utility functions.
"""

def calculate_average(numbers):
    """Calculate the average of a list of numbers.
    
    Args:
        numbers: A list of numeric values
        
    Returns:
        float: The arithmetic mean of the input numbers
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")
    
    return sum(numbers) / len(numbers)


def find_max(numbers):
    """Find the maximum value in a list.
    
    Args:
        numbers: A list of comparable values
        
    Returns:
        The maximum value from the list
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find max of empty list")
    
    return max(numbers)


def find_min(numbers):
    """Find the minimum value in a list.
    
    Args:
        numbers: A list of comparable values
        
    Returns:
        The minimum value from the list
        
    Raises:
        ValueError: If the list is empty
    """
    if not numbers:
        raise ValueError("Cannot find min of empty list")
    
    return min(numbers)
