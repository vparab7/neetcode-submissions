class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(heights)-1
        while left < right:
            if heights[left] < heights[right]:
                max_area = max(heights[left]*(right-left),max_area)
                left+=1
            else:
                max_area = max(heights[right]*(right-left),max_area)
                right-=1
            #print("left -> {} right -> {} max -> {}".format(left,right,max_area))
        return max_area