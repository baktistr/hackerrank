# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return factorial(n-1)*n


def poisson_distribution(l,k):
    e = 2.71828
    return (l**k * e**(-l)/factorial(k))


lambda_val = float(input())
k_val = float(input())

print(round(poisson_distribution(lambda_val,k_val),3))


