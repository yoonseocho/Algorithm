def solution(new_id):
    # 1단계
    new_id_1 = new_id.lower()
    
    # 2단계
    new_id_2 = ""
    for char in new_id_1:
        if char.isdigit() or char.isalpha() or char in ['-', '_', '.']:
            new_id_2 += char
    
    # 3단계
    new_id_3 = ""
    i = 0
    while i < len(new_id_2):
        if new_id_2[i] == '.':
            cnt = 0
            while i+1 < len(new_id_2) and new_id_2[i+1] == '.':
                i += 1
            new_id_3 += "."
        else:
            new_id_3 += new_id_2[i]
        
        i += 1
    
    # 4단계
    new_id_4 = ""
    
    for i in range(len(new_id_3)):
        if i == 0 or i == len(new_id_3)-1:
            if new_id_3[i] == '.':
                continue
        new_id_4 += new_id_3[i]
    
    # 5단계
    new_id_5 = new_id_4
    
    if new_id_4 == "":
        new_id_5 += 'a'
    
    # 6단계
    new_id_6 = new_id_5
    
    if len(new_id_5) >= 16:
        new_id_6 = new_id_5[:15]
    
    if new_id_6[-1] == ".":
        new_id_6 = new_id_6[:-1]
    
    # 7단계
    new_id_7 = new_id_6
    if len(new_id_6) <= 2:
        while len(new_id_7) < 3:
            new_id_7 += new_id_6[-1]
    
    return new_id_7
            
    