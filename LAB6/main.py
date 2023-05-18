import math
import decimal
import time
import matplotlib.pyplot as plt
import mpmath as mp

def machin(n):
    # Set the precision to include the desired digit plus a few extra digits
    mp.dps = n + 10

    # Calculate pi using Machin's formula
    pi = 4 * (4 * mp.atan(1/5) - mp.atan(1/239))

    # Multiply pi by 10^n and convert to integer
    multiplied_pi = pi * mp.power(10, n)

    # Extract the n-th digit from the multiplied pi
    digit = int(multiplied_pi) % 10

    return digit

def gauss_legendre(n):
    decimal.getcontext().prec = n + 2  # Set precision to n+2 (to include n decimal places)
    decimal.getcontext().Emax = 9999999999  # Set maximum exponent value
    
    a = decimal.Decimal(1)
    b = decimal.Decimal(1) / decimal.Decimal(2).sqrt()
    t = decimal.Decimal(0.25)
    p = decimal.Decimal(1)

    for _ in range(n):
        a_next = (a + b) / 2
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2

    pi = (a + b) ** 2 / (4 * t)
    return str(pi)[:-1]

def ramanujan(n):
    num_terms = math.ceil((n + 1) / 14)  # Number of terms needed for n digits

    decimal.getcontext().prec = n + 10

    pi = decimal.Decimal(0)
    for k in range(num_terms):
        term = (decimal.Decimal(math.factorial(4 * k)) * (decimal.Decimal(1103) + decimal.Decimal(26390) * k)) / \
               ((decimal.Decimal(math.factorial(k)) ** 4) * (decimal.Decimal(396) ** (4 * k)))
        pi += term

    pi *= ((decimal.Decimal(2) * decimal.Decimal(math.sqrt(2))) / decimal.Decimal(9801))

    # Multiply pi by 10^n, round to the nearest integer, and extract the n-th digit
    digit = int((pi * decimal.Decimal(10) ** n).quantize(decimal.Decimal('1'))) % 10
    return digit



def time_taken(n):
    #Time for machin's formula
    start_time = time.time()
    pi_machin = machin(n)
    end_time = time.time()
    time_taken_machin = end_time - start_time

#Time for gauss-legendre formula
    start_time = time.time()
    pi_gauss_legendre = gauss_legendre(n)
    end_time = time.time()
    time_taken_gauss_legendre = end_time - start_time

#Time for ramanujan formula
    start_time = time.time()
    pi_ramanujan = ramanujan(n)
    end_time = time.time()
    time_taken_ramanujan = end_time - start_time

    return time_taken_machin, time_taken_gauss_legendre, time_taken_ramanujan

def plot_time(n):
    #Calculate time taken for the algorithms
    time_taken_machin, time_taken_gauss_legendre, time_taken_ramanujan = time_taken(n)

    algorithms = ['Machin', 'Gauss-Legendre', 'Ramanujan']

    times = [time_taken_machin, time_taken_gauss_legendre, time_taken_ramanujan]

    plt.bar(algorithms, times)
    plt.ylabel('Time taken (s)')
    plt.xlabel('Algorithm')
    plt.title(f'Time taken to calculate pi for n={n}')
    plt.show() 



# Example usage
n = 5
plot_time(n)
result = machin(n)
result1 = gauss_legendre(n)
result2 = ramanujan(n)
print(f"The {n}-th digit of pi is: {result}")
print(f"The {n}-th digit of pi is: {result1}")
print(f"The {n}-th digit of pi is: {result2}")

