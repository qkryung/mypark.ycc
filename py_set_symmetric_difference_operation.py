#https://www.hackerrank.com/challenges/py_set_symmetric_difference_operation/problem



# Enter your code here. Read input from STDIN. Print output to STDOUT



a,s1=int(input()),set(map(int,input().split()))
b,s2=int(input()),set(map(int,input().split()))
print(len((s1.difference(s2)).union(s2.difference(s1))))
