def solution(phone_book):
    answer = True
    phone_book.sort()
    
    now = phone_book[0]

    for i in range(1, len(phone_book)):
        if now == phone_book[i][:len(now)]:
            return False
        now = phone_book[i]
    
    return answer
