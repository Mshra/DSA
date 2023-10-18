import time

def pow(a, n):
    """
    Compute the power of a number 'a' raised to the exponent 'n' using a recursive algorithm. Running time of the algorithm is O(log n), where n is the exponent.

    Parameters:
    - a: The base number.
    - n: The exponent to which 'a' is raised.

    Returns:
    The result of 'a' raised to the power of 'n'.

    Note:
    This function calculates the result of 'a' raised to the power of 'n' using a recursive approach. It exploits the property that 'a^(2n) = (a^n)^2' to reduce the number of multiplications needed.

    Example:
    result = pow(2, 5)
    # Result: 32 (2^5)
    """
    if n == 0:
        return 1
    x = pow(a, n // 2)
    if n % 2 == 0:
        return x * x
    else:
        return a * x * x

if __name__ == '__main__':
    a, n = 34, 40
    t = []

    for n in range(50):
        start = time.time()
        pow(a, n)
        end = time.time()
        t.append(round((end - start)*(1000000), 3))

    print('average running time is', sum(t)/len(t), 'microseconds')