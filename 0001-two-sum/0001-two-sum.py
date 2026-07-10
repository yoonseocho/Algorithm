class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = []
        indent = "   "
        def dfs(cur_sum, idx):
            # print(f"{indent * idx}>>>dfs({cur_sum}, {idx})")
            if len(answer) == 2:
                if cur_sum == target:
                    return True
                return False
 
            for i in range(idx, len(nums)):
                answer.append(i)
                if dfs(cur_sum + nums[i], i+1):
                    return True
                # print(f"{indent * (i+1)}dfs함수 끝!")
                answer.pop()

        dfs(0, 0)
        return answer
            