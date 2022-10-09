class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap = {}
        for i,val in enumerate(nums):
            if (target - val) in hashMap:
                return [hashMap[target-val], i]
            else:
                hashMap[val] = i
                