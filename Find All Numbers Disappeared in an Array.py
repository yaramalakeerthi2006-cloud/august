class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        j = 0
        n = len(nums)

        for i in range(1, n + 1):
            while j < n and nums[j] < i:
                j += 1

            if j == n or nums[j] != i:
                ans.append(i)

        return ans
