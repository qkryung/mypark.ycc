#https://www.hackerrank.com/challenges/py_introduction_to_sets/problem

def average(array):
    # your code goes here

    a= set(array)
    avr = sum(a) / len(a)
    return avr



if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

