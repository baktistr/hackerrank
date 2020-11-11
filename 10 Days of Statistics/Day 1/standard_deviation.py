# https://www.hackerrank.com/challenges/s10-standard-deviation/problem
import math

def mean(data):
    return sum(data)/len(data)

def sttdev(data, size):
    sums = 0
    for x in range(size):
        sums = sums + (data[x] - mean(data))**2
    return math.sqrt(sums/size)


size = int(input())
numbers = list(map(int, input().split()))

print(round(sttdev(numbers,size),1))