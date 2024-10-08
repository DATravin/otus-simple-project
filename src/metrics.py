"""
module for functions

"""

from typing import List,Union

def calculate_mean(numbers: List[Union[int,float]])->float:
    """
    function for calculation mean

    Parametrs
    ---------
    numbers: List[Union[int,float]
        list of numbers

    Return
    ------
    float
        mean of numbers

    """
    return sum(numbers)/len(numbers)
