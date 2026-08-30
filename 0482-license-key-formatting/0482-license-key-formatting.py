class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cleaned = s.replace('-', '').upper()
        n = len(cleaned)
        answer = []
        print(cleaned)
        if n % k == 0:
            # k개씩 쪼개기
            i = 0
            for _ in range(n//k):
                answer.append(cleaned[i:i+k])
                i += k
        else:
            res = n % k
            answer.append(cleaned[:res])

            # k개씩 쪼개기
            i = res
            for _ in range(n//k):
                answer.append(cleaned[i:i+k])
                i += k
        
        return '-'.join(answer)