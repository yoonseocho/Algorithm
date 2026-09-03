def solution(new_id):
    
    # 1단계
    new_id = new_id.lower()
    # print(f'1단계, {new_id}')
    
    # 2단계
    for ch in new_id:
        if not (ch.isalpha() or ch.isdigit() or ch == '-' or ch == '_' or ch == '.'):
            new_id = new_id.replace(ch, '')
    # print(f'2단계, {new_id}')
    
    # 3단계
    result = ''
    i = 0
    while i < len(new_id):
        if new_id[i] == '.':
            result += '.'
            j = i + 1
            while len(new_id) >= j+1 and new_id[j] == '.':
                j += 1
            i = j
        else:
            result += new_id[i]
            i += 1
    new_id = result
    # print(f'3단계, {new_id}')
    
    # 4단계
    if len(new_id) >= 1 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) >= 1 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # print(f'4단계, {new_id}')
    
    # 5단계
    if len(new_id) == 0:
        new_id += 'a'
    # print(f'5단계, {new_id}')
    
    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    # print(f'6단계, {new_id}')
    
    # 7단계
    if len(new_id) == 1:
        new_id += (new_id[-1]) * 2
    if len(new_id) == 2:
        new_id += new_id[-1]
    # print(f'7단계, {new_id}')
    
    return new_id
    