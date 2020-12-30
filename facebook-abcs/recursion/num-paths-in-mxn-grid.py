import os

def solution(m, n):
    if m==1 or n==1:
        return 1
    else:
        return solution(m, n-1) + solution(m-1, n)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    result = solution(m, n)

    fptr.write(str(result) + '\n')

    fptr.close()