class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] != newColor:
            self.dfs(sr,sc,image,newColor,image[sr][sc])
        
        return image
    
    def dfs(self,r,c,arr,col,val):
        rl = len(arr)
        cl = len(arr[0])
        
        if r<0 or r>=rl or c<0 or c>=cl or arr[r][c] != val:
            return
        
        arr[r][c] = col
        self.dfs(r+1,c,arr,col,val)
        self.dfs(r-1,c,arr,col,val)
        self.dfs(r,c+1,arr,col,val)
        self.dfs(r,c-1,arr,col,val)