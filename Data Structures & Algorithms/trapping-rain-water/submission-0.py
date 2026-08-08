class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0
        left_max = 0
        right_max = 0
        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if left_max < right_max:
                area += (left_max - height[left])
                #print("left is less. left -> {}, right -> {}, left_max-> {}, right_max -> {}, area -> {}".format(left,right,left_max, right_max, area))
                left+=1
            else:
                area += (right_max-height[right])
                #print("right is less. left -> {}, right -> {}, left_max-> {}, right_max -> {}, area -> {}".format(left,right,left_max, right_max, area))
                right-=1
        return area