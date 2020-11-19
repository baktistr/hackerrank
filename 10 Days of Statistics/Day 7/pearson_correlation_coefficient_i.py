# https://www.hackerrank.com/challenges/s10-pearson-correlation-coefficient/problem

import math

def mean(data):
    return sum(data)/len(data)

def std_def(data, size):
    sums = 0
    for x in range(size):
        sums = sums + (data[x] - mean(data))**2
    return math.sqrt(sums/size)

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

top_result = 0
for index in range(n):
    top_result += (x[index]-mean(x))*(y[index]-mean(y))

result = top_result /(n * std_def(x,n) * std_def(y,n))
print(round(result,3))