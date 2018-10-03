class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        self.buildHeap(nums)
        for i in range(k):
            ans = nums.pop(0)
            self.buildHeap(nums)
        return ans
    
    def buildHeap(self,arr):
        l = len(arr)
        for i in range((l/2)-1,-1,-1):
            self.maxheapify(arr,i,l)
    
    def maxheapify(self,arr,i,l):
        left = 2*(i)+1
        right = 2*(i)+2
        largest = i
        if left<l and arr[left]>arr[largest]:
            largest = left
        else:
            largest = i
        if right<l and arr[right]>arr[largest]:
            largest = right
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.maxheapify(arr,largest,l)