from itertools import product

def solution(word):
    # 사전 만들기..
    dictionary = []
    vowel = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        ps = product(vowel, repeat = i)
        for p in ps:
            dictionary.append(''.join(p))
    dictionary.sort()
    
    # print(dictionary)
    
    dict = {}
    for i, wrd in enumerate(dictionary, start=1):
        dict[wrd] = i
    
    # print(dict)
    
    if word in dict:
        return dict[word]
    