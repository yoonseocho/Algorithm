class Solution:
    def reformatNumber(self, number: str) -> str:
        cleaned = number.replace('-', '').replace(' ', '')
        
        n = len(cleaned)
        i = 0
        answer = []

        while (n - i) > 4:
            answer.append(cleaned[i:i+3])
            i += 3
        
        if len(cleaned[i:]) == 4:
            answer.append(cleaned[i:i+2])
            i += 2
        answer.append(cleaned[i:])

        return '-'.join(answer)