class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_list = sorted(enumerate(nums), key=lambda x: x[1])
        n = len(nums)
        for i in range(n-1):
            for j in range(n-1, i, -1):
                two_sum = nums_list[i][1] + nums_list[j][1]
                if two_sum == target:
                    return [nums_list[i][0], nums_list[j][0]]
                elif two_sum < target:
                    break
            