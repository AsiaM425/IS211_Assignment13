def fibonacci(n):
    """
    Returns the nth element of the Fibonacci sequence using recursion.

    Parameters:
    n (int): The index of the desired element of the Fibonacci sequence.

    Returns:
    int: The nth element of the Fibonacci sequence.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
      print(fibonacci(0))  # 0
print(fibonacci(1))  # 1
print(fibonacci(10)) # 55




def gcd(a, b):
    """
    Returns the greatest common divisor of two integers using recursion.

    Parameters:
    a (int): An integer.
    b (int): Another integer.

    Returns:
    int: The greatest common divisor of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
      print(gcd(12, 18)) # 6
print(gcd(9, 28))  # 1



def compareTo(s1, s2):
    """
    Recursively compares two strings and returns a negative number if s1 < s2,
    0 if s1 == s2, and a positive number if s1 > s2.

    Parameters:
    s1 (str): A string.
    s2 (str): Another string.

    Returns:
    int: A negative number if s1 < s2, 0 if s1 == s2, and a positive number
         if s1 > s2.
    """
    if s1 == "" and s2 == "":
        return 0
    elif s1 == "":
        return -1
    elif s2 == "":
        return 1
    else:
        if s1[0] < s2[0]:
            return -1
        elif s1[0] > s2[0]:
            return 1
        else:
            return compareTo(s1[1:], s2[1:])
          print(compareTo("apple", "banana"))    # -1
print(compareTo("banana", "apple"))    # 1
print(compareTo("apple", "apple"))     # 0




