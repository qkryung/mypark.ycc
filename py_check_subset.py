#https://www.hackerrank.com/challenges/py_check_subset/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(input())):
    a1 = input()
    a2 = set(map(int, input().split()))
    b1 = input()
    b2 = set(map(int, input().split()))
    if a2.intersection(b2) == a2:
        print("True")
    else:
        print("False")
