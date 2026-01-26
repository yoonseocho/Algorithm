def solution(s):
    words = list(s.split(' '))
    new_words = []
    
    for word in words:
        if word:
            new_words.append(word[0].upper() + word[1:].lower())
        else:
            new_words.append('')
    
    return ' '.join(new_words)