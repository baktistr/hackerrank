# https://www.hackerrank.com/challenges/s10-weighted-mean/problem

size = int(input())
numbers = list(map(int, input().split()))
weights = list(map(int, input().split()))

sums = 0

for x in range(size):
    sums += (numbers[x] * weights[x])

print(round(sums/sum(weights),1))