string = input()
output = []

for s in string:
    if "A" <= s <= "Z":
        char_code = ord(s) - ord('A')
        rotated_code = (char_code + 13) % 26
        new_code = chr(rotated_code + ord('A'))
        output.append(new_code)
    elif "a" <= s <= "z":
        char_code = ord(s) - ord('a')
        rotated_code = (char_code + 13) % 26
        new_code = chr(rotated_code + ord('a'))
        output.append(new_code)
    else:
        output.append(s)
print(''.join(output))