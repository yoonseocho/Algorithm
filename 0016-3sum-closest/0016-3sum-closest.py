class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        answer = set()
        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            lo, hi = i+1, n-1
            while lo < hi:
                s = nums[i] + nums[lo] + nums[hi]
                answer.add(s)

                if s == target:
                    return s
                elif s > target:
                    hi -= 1
                    while lo < hi and nums[hi] == nums[hi+1]:
                        hi -= 1
                else:
                    lo += 1
                    while lo < hi and nums[lo] == nums[lo-1]:
                        lo += 1
   
        return min(answer, key=lambda x: abs(x-target))
