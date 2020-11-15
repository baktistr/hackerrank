# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return factorial(n-1)*n

def binomial_dist(x,n,p):
    
    return (factorial(n)/(factorial(x)*factorial(n-x))) * (p**x) * ((1.0-p)**(n-x))

inputs = list(map(float, input().split()))
p = inputs[0] / (inputs[0]+inputs[1])
n = 6

result = binomial_dist(3,n,p) + binomial_dist(4,n,p) + binomial_dist(5,n,p) + binomial_dist(6,n,p)
print(round(result,3))
