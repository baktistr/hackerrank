# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    else:
        return factorial(n-1)*n

def binomial_dist(x,n,p):
    
    return (factorial(n)/(factorial(x)*factorial(n-x))) * (p**x) * ((1.0-p)**(n-x))


inputs = list(map(int, input().split()))
p = (inputs[0] / 100)
n = int(inputs[1])

# no more than 2 rejects
result1 = 0
for i in range(n):
    if i < 3 :
        result1 += binomial_dist(i,n,p)

print(round(result1,3))


# at least 2 rejects
result2 = 0
for i in range(n):
    if i > 1 :
        result2 += binomial_dist(i,n,p)

print(round(result2,3))
