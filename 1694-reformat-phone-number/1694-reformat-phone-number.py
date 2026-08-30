class Solution:
    def reformatNumber(self, number: str) -> str:
        dash_removed = ''.join(number.split('-'))
        space_dash_removed = ''.join(dash_removed.split())
        
        n = len(space_dash_removed)

        b = n // 3
        if (n - 3*b) % 2 != 0:
            b -= 1
        a = (n - 3*b) // 2

        answer = []
        last = 0
        for i in range(0, 3*b, 3):
            answer.append(space_dash_removed[i:i+3])
            last = i+3

        
        for i in range(last, last + 2*a, 2):
            answer.append(space_dash_removed[i:i+2])
        
        return '-'.join(answer)