def solution(phone_book):
    phone_set = set(phone_book)
    
    for p in phone_book:
        temp = ""
        for num in p:
            temp += num
            if temp in phone_set and temp != p:
                return False
    return True