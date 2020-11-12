# https://www.hackerrank.com/challenges/s10-quartiles/problem

def median(size, data):
    if (size % 2 == 0):
        return int((data[int(size/2)-1]+data[int(size/2)])/2)
    else:
        return int(data[int(size/2)])

size = int(input())
numbers = sorted(list(map(int, input().split())))

if (size % 2 == 0):
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2):]
else:
    data_low = numbers[0:int(size/2)]
    data_high = numbers[int(size/2)+1:]

print(median(len(data_low), data_low))
print(median(size, numbers))
print(median(len(data_high), data_high))

