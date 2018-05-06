class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums == [] or nums == None:
            return -1

        n = len(nums)
        if nums[0] < nums[n - 1]:
            return self.bsearch(nums, 0, n - 1, target)

        pivot = -1
        for i in range(0, n - 1):
            if nums[i] > nums[i + 1]:
                pivot = i
                break

        if pivot == -1:  # The array is sorted
            return self.bsearch(nums, 0, n - 1, target)

        if nums[0] <= target <= nums[pivot]:
            return self.bsearch(nums, 0, pivot, target)
        else:
            return self.bsearch(nums, pivot + 1, n - 1, target)

    def bsearch(self, arr, low, high, target):
        if low <= high:
            mid = (low + high) // 2

            if target == arr[mid]:
                return mid
            if target < arr[mid]:
                return self.bsearch(arr, low, mid-1, target)
            elif target > arr[mid]:
                return self.bsearch(arr, mid +1 ,high, target)


sol = Solution()
print(sol.search([4,5,6,7,0,1,2],0))