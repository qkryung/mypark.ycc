#https://www.hackerrank.com/challenges/py_set_difference_operation/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT


s1 = int(input())
set_1 = set(map(int,input().split()))
s2 = int(input())
set_2 = set(map(int,input().split()))
print(len(set_1 - set_2))
