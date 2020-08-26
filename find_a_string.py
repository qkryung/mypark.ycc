#https://www.hackerrank.com/challenges/find_a_string/problem



def count_substring(string, sub_string):
    l = len(sub_string)
    cou = 0
    for i in range(len(string) - len(sub_string) + 1):
        if(string[i:i + len(sub_string)] == sub_string ):      
            cou += 1
    return cou

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

