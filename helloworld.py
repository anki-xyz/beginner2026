print("Hi!")
x = 5
x = 10
y = 5

def random(a:int, b:float) -> float:
    """_summary_

    Args:
        a (int): The lower bound.
        b (float): The upper bound.

    Returns:
        float: A random float between a and b.
    """
    import random
    return random.uniform(a, b)