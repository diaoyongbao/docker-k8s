class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums)-1):
            for j in nums[i+1:]:
                if nums[i] == j:
                    nums.remove(nums[i])
                else:
                    break
        return len(nums)
if __name__ == "__main__":
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    a = Solution()
    b = a.removeDuplicates(nums)
    print(b)



