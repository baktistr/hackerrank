# https://www.hackerrank.com/challenges/s10-the-central-limit-theorem-1/problem

import math

def cumulative_normal_dist(mean, stdev, x):

    return 0.5 * (1 + math.erf((x-mean)/(stdev * (2**0.5))))

max_weight = float(input())
n = float(input())
mean = float(input())
stdev = float(input())

new_mean = n * mean
new_stdev = math.sqrt(n) * stdev

print(round(cumulative_normal_dist(new_mean,new_stdev,max_weight),4))