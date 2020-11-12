# https://www.hackerrank.com/challenges/s10-interquartile-range/problem

def median(size, data):
    if (size % 2 == 0):
        return float((data[int(size/2)-1]+data[int(size/2)])/2)
    else:
        return float(data[int(size/2)])

size = int(input())
numbers = list(map(int,input().split()))
freqs = list(map(int,input().split()))

new_list = []
for x in range(len(numbers)):
    for y in range(freqs[x]):
        new_list.append(numbers[x])

new_list = sorted(new_list)

if (len(new_list) % 2 == 0):
    data_low = new_list[0:int(len(new_list)/2)]
    data_high = new_list[int(len(new_list)/2):]
else:
    data_low = new_list[0:int(len(new_list)/2)]
    data_high = new_list[int(len(new_list)/2)+1:]

q1 = median(len(data_low), data_low)
q3 = median(len(data_high), data_high)

print(q3-q1)