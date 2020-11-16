# https://www.hackerrank.com/challenges/s10-normal-distribution-2/problem

import math

def cumulative_normal_dist(mean, stdev, x):

    return 0.5 * (1 + math.erf((x-mean)/(stdev * (2**0.5))))

inputs = list(map(float,input().split()))
x_mean = inputs[0]
x_stdev = inputs[1]

x_80 = float(input())
x_60 = float(input())

print(round(100 - (cumulative_normal_dist(x_mean, x_stdev,x_80)) * 100,2))
print(round(100 - (cumulative_normal_dist(x_mean, x_stdev, x_60)) * 100,2))
print(round(cumulative_normal_dist(x_mean, x_stdev, x_60) * 100,2))
