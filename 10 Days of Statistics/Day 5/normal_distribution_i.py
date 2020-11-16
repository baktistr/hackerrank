# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem

import math

def cumulative_normal_dist(mean, stdev, x):

    return 0.5 * (1 + math.erf((x-mean)/(stdev * (2**0.5))))

inputs = list(map(float,input().split()))
x_mean = inputs[0]
x_stdev = inputs[1]

x1 = float(input())

x2 = list(map(float, input().split()))
x2_a = x2[0]
x2_b = x2[1]

print(round(cumulative_normal_dist(x_mean,x_stdev,x1), 3))
print(round((cumulative_normal_dist(x_mean,x_stdev,x2_b)) - (cumulative_normal_dist(x_mean,x_stdev,x2_a)), 3))

