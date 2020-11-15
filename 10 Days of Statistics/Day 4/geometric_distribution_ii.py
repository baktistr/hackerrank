# https://www.hackerrank.com/challenges/s10-geometric-distribution-2/problem

inputs = list(map(int, input().split()))
p = (inputs[0] / inputs[1])
q = 1-p
n = int(input())

result = 0
for i in range(1,n+1):
    result +=  q**(i-1)*p

print(round(result,3))
