#https://www.hackerrank.com/challenges/polar_coordinates/problem
#Enter your code here. Read input from STDIN. Print output to STDOUT

import cmath
a = input()

print(abs(complex(a)))
print(cmath.phase(complex(a)))
