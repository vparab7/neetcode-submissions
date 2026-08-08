class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # -4, -1, -1, 0, 1, 2
        output = list()
        nums.sort()
        for i in range(len(nums)-2): 
            if nums[i] == nums[i-1] and i!=0:
                continue
            target = -nums[i] #1
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right] #1
                if sum < target: #1<4
                    left+=1
                elif sum > target:
                    right-=1
                else:
                    output.append([-target,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left-1] == nums[left] and left < right:
                        left+=1
                    while nums[right+1] == nums[right] and right < right:
                        right-=1
        return output