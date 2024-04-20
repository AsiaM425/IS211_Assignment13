# Part I - Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Part II - Euclid’s GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Part III - String Comparison
def compareTo(s1, s2):
    if s1 == '' and s2 == '':
        return 0
    elif s1 == '':
        return -1
    elif s2 == '':
        return 1
    elif s1[0] < s2[0]:
        return -1
    elif s1[0] > s2[0]:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])

# Testing the functions
if __name__ == "__main__":
    # Part I - Fibonacci Sequence
    print("Fibonacci sequence:")
    for i in range(10):
        print(fibonacci(i), end=" ")
    print("\n")

    # Part II - Euclid’s GCD Algorithm
    print("GCD of 48 and 18:", gcd(48, 18))
    print("GCD of 60 and 96:", gcd(60, 96))
    print("GCD of 17 and 13:", gcd(17, 13))
    print()

    # Part III - String Comparison
    print("String Comparison:")
    print(compareTo("apple", "banana"))  # Expected: -1
    print(compareTo("banana", "apple"))  # Expected: 1
    print(compareTo("apple", "apple"))   # Expected: 0
