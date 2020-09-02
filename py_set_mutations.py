# https://www.hackerrank.com/challenges/py_set_mutations/problem

# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    a = int(input())
    A = set(map(int, input().split()))
    N = int(input())
    for i in range(N):
        command = input().split()[0]
        b = set(map(int, input().split()))
        if command == "intersection_update":
            A.intersection_update(b)
            #A = A.intersection(b)
        elif command == "update":
            A.update(b)
        elif command == "symmetric_difference_update":
            A.symmetric_difference_update(b)
        elif command == "difference_update":
            A.difference_update(b)
    print(sum(A))


