class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        if nums[start] > target:
            return 0
        elif nums[end] < target:
            return end + 1
        else:
            while(end-start>1):
                if nums[start] == target:
                    return start
                elif nums[end] == target:
                    return end
                else:
                    mid = (start + end)/2
                    print("mid: " + str(mid))
                    if nums[mid] == target:
                        return mid
                    elif nums[mid] > target:
                        end = mid - 1
                    elif nums[mid] < target:
                        start = mid + 1
            if nums[start] == target:
                return start
            elif nums[end] == target:
                return end
            elif nums[start] < target and nums[end] > target:
                return start+1
            elif nums[start] < target and nums[end] < target:
                return end+1
            elif nums[start]> target:
                return start