def solution(phone_book):
    phone_book.sort()
    
    for left, right in zip(phone_book[:-1], phone_book[1:]):
        if right.startswith(left):
            return False
    return True