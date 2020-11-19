# https://www.hackerrank.com/challenges/s10-least-square-regression-line/problem

def mean(data):
    return sum(data)/len(data)

def sum_xy(x,y):
    result = 0
    for i in range (len(x)):
        result += (x[i]*y[i])
    return result

def sum_quadratic(data):
    result = 0
    for i in range(len(data)):
        result += data[i]**2
    return result
 
n = 5
x = [95, 85, 80, 70, 60]
y = [85, 95, 70, 65, 70]

mean_x = mean(x)
mean_y = mean(y)

b = ((n * sum_xy(x,y))-(sum(x)*sum(y)))/(n*sum_quadratic(x)-sum(x)**2)
a = mean_y - b*mean_x
result = a + 80*b
print(round(result,3))