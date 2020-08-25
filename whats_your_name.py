#https://www.hackerrank.com/challenges/whats_your_name/problem

def print_full_name(a, b):
    string = f"Hello {a} {b}! You just delved into python."
    return print(string)



if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
