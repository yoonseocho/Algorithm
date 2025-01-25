sentence = input()
result = []
split_by_tag = sentence.split("<")

for word in split_by_tag:
    if ">" in word:
        tag, rest = word.split(">")
        result.append(f'<{tag}>')
        reversed_rest = ' '.join(m[::-1] for m in rest.split())
        result.append(reversed_rest)
    else:
        just_word = ' '.join(i[::-1] for i in word.split())
        result.append(just_word)

print(''.join(result))