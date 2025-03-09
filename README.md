# Power Evaluation

## Overview
This repository contains a Python module designed for evaluating polynomial functions using an array of coefficients and a given value of x. It includes functions to:
- Compute the power of a number.
- Evaluate a polynomial efficiently.
- Execute a main function that demonstrates polynomial evaluation with a sample dataset.

## Features
- **Power Calculation**: Computes the p'th power of a given number.
- **Polynomial Evaluation**: Evaluates a polynomial function based on provided coefficients and a variable x.
- **Structured Execution**: Demonstrates the evaluation of a predefined polynomial example.

```

## Usage
Run the main script to evaluate the polynomial example:
```sh
Polynomial.py
```

## Code Structure
### `power(x, p)`
Computes the p'th power of a real number.
```python
def power(x, p):
    """Calculates the p'th power of a real number."""
```
**Parameters:**
- `x` (float): The base number.
- `p` (int): The exponent (should be a non-negative integer).

**Returns:**
- `float`: The result of x raised to the power of p.

### `evaluate(A, x)`
Evaluates a polynomial given its coefficients and a function-evaluated integer.
```python
def evaluate(A, x):
    """Evaluates a polynomial given its coefficients."""
```
**Parameters:**
- `A` (list of float): List of polynomial coefficients, where A[i] represents the coefficient for the x^i term.
- `x` (float): The value at which the polynomial is evaluated.

**Returns:**
- `float`: The computed value of the polynomial at x.

### `main()`
Executes the polynomial evaluation example:
```python
def main():
    """Evaluates a polynomial and prints the result."""
```
This function evaluates the polynomial:
```
f(x) = 12.3 + 40.7x - 9.1x^2 + 7.7x^3 + 6.4x^4 + 8.9x^6
```
at `x = 5.4` and prints the computed result.

## Example Output
```sh
Final result: 12587.346
```

## Contributing
Contributions are welcome! To contribute:
1. Fork this repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a Pull Request.

## License
This project is licensed under the MIT License.

## Author
Developed by Ike Iloegbu.
