# https://www.hackerrank.com/challenges/py_set_intersection_operation/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT


s = int(input())
s1 = set(map(int,input().split()))
s2 = int(input())
s2 = set(map(int,input().split()))
print (len(s1.intersection(s2)))
