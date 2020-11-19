# https://www.hackerrank.com/challenges/s10-spearman-rank-correlation-coefficient/problem

def rank(data):
    ranked_data = {}
    sorted_data = sorted(data)
    for i in range (len(data)):
        for j in range (len(sorted_data)):
            if  data[i] == sorted_data[j]:
                ranked_data[data[i]] = j+1
    return ranked_data

def spearman_rank(x, y, rank_x, rank_y, n):
    rank_diff = 0
    for i in range(n):
        rank_diff = rank_diff + ((rank_x[x[i]]-rank_y[y[i]]) ** 2)
    result = 1 - (6*rank_diff)/(n*(n**2-1))
    return result

n = int(input())
x = list(map(float, input().split()))
y = list(map(float, input().split()))

rank_x = rank(x)
rank_y = rank(y)
print(round((spearman_rank(x,y,rank_x,rank_y,n)),3))