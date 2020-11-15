# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem

inputs = list(map(int, input().split()))
p = (inputs[0] / inputs[1])
q = 1-p
n = int(input())

result = q**(n-1)*p
print(round(result,3))
