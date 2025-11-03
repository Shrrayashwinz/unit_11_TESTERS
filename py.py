"""
Lab11_pcarswel-1.py
Author: Shrrayash
Purpose: Normalize a rotation angle to within 0–359 degrees.
Date: November 3, 2025
"""

def normalize_rotation(degrees):
    """
    Normalize any degree input to a value between 0 and 359 inclusive.
    Handles negative and large positive inputs.
    
    Parameters:
        degrees (int or float): The angle to normalize.
    
    Returns:
        int or float: Normalized angle within 0–359.
    
    Raises:
        ValueError: if input is not a number.
    """
    if not isinstance(degrees, (int, float)):
        raise ValueError("Input must be a numeric value.")
    return degrees % 360

