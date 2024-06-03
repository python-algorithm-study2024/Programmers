def solution(n):
    if n == 0 or n == 1: return n

    answer = 1 + n
    for i in range(2, n):
        if n % i == 0: answer += i
    
    return answer