from mpmath import mp

def calculate_pi_digit(n):
    # Set the precision to include the desired digit plus a few extra digits
    mp.dps = n + 10

    # Calculate pi using Machin's formula
    pi = 4 * (4 * mp.atan(1/5) - mp.atan(1/239))

    # Extract the n-th digit from the calculated pi
    digit = int(str(pi)[n+2])

    return digit

# Example usage
n = 5  # Calculate the 1000th digit of pi
digit = calculate_pi_digit(n)
print(f"The {n}th digit of pi is: {digit}")
