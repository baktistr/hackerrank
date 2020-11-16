# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

inputs = list(map(float, input().split()))
lambda_a = inputs[0]
lambda_b = inputs[1]

print(round(160+40*(lambda_a + lambda_a**2),3))
print(round(128+40*(lambda_b + lambda_b**2),3))