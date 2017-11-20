class Solution(object):
    def rotate(self, nums, k):
        l = len(nums)
        val = (l-k)%l
        self.reverse(nums,0,val-1)
        self.reverse(nums,val,l-1)
        self.reverse(nums,0,l-1)
        
    def reverse(self,a,s,e):
        i = s
        j = e
        while i<j:
            a[i],a[j] = a[j],a[i]
            i += 1
            j -= 1
  	return a