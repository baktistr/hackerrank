# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-3/problem

import math

n = float(input())
mean = float(input())
stdev = float(input())
confidence_interval_percentage = float(input())
confidence_interval_value = float(input())

print(round(mean - (confidence_interval_value * (stdev/math.sqrt(n))),2))
print(round(mean + (confidence_interval_value * (stdev/math.sqrt(n))),2))