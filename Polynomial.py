"""
This module provides functions to evaluate a polynomial function given an array of coefficients 
and a value of x. It includes functions to calculate the power of a number, evaluate a polynomial, 
and execute the main function that demonstrates polynomial evaluation.

Functions:
    power(x, p): Computes the p'th power of a real number.
    evaluate(A, x): Evaluates a polynomial given its coefficients and a value of x.
    main(): Runs an example polynomial evaluation and prints the result.
"""

def power(x, p):
    """Calculates the p'th power of a real number.

    Args:
        x (float): The base number to be exponentiated.
        p (int): The exponent (should be a non-negative integer).

    Returns:
        float: The result of x raised to the power of p.
    
    Raises:
        ValueError: If p is negative, as only non-negative exponents are supported.
    """
    if p < 0:
        raise ValueError("Exponent must be a non-negative integer")
    
    result = 1  # Initialize result to 1
    for _ in range(p):
        result *= x  # Multiply x by itself p times
    return result

def evaluate(A, x):
    """Evaluates a polynomial given its coefficients and a function-evaluated integer.

    The polynomial is evaluated as:
        f(x) = A[0] + A[1]x + A[2]x^2 + ... + A[n]x^n
    
    Args:
        A (list of float): List of polynomial coefficients, where A[i] represents the coefficient 
            for the x^i term.
        x (float): The value at which the polynomial is evaluated.

    Returns:
        float: The computed value of the polynomial at x.
    """
    result = 0  # Initialize the result to 0
    for i in range(len(A)):
        result += A[i] * power(x, i)  # Multiply the coefficient by x^i and accumulate
    return result

def main():
    """Evaluates the polynomial f(x) = 12.3 + 40.7x - 9.1x^2 + 7.7x^3 + 6.4x^4 + 8.9x^6 at x = 5.4.
    
    The function initializes an array of coefficients corresponding to the polynomial terms,
    evaluates the polynomial at x = 5.4, and prints the final computed result.
    """
    polyArray = [12.3, 40.7, -9.1, 7.7, 6.4, 0, 8.9]  # Coefficients of the polynomial
    xNum = 5.4  # Value of x at which to evaluate the polynomial
    result = evaluate(polyArray, xNum)  # Compute the polynomial value
    print("Final result:", result)  # Display result

if __name__ == "__main__":
    main()

#The total number of multiplications for a polynomial of degree n is: n*(n+1)/2
#The Big-O notation for this program is 0(n^2) because the number opf multiplications corresponds to the square of the degree of the polynomial 
