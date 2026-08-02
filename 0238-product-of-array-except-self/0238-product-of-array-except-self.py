class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        total_product = 1
        zero_cnt = 0
        for num in nums:
            if num == 0:
                zero_cnt += 1
                continue
            total_product *= num
        
        for i in range(n):
            if nums[i] == 0:
                if zero_cnt == 1:
                    answer[i] = total_product
                else:
                    answer[i] = 0

            else:
                if zero_cnt == 0:
                    answer[i] = total_product // nums[i]
                else:
                    answer[i] = 0
        
        return answer