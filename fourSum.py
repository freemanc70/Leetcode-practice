class solution(object):
    def threeSum(self,nums, target):
        nums, result, temp = sorted(nums), [], 0
        for i in range(0, len(nums)-2):
            temp = target - nums[i]
            if temp > 0 and nums[i] != nums[i+1]:
                j, k = i + 1, len(nums) - 1
                while j < k and nums[j] != nums[k]:
                    if nums[j] + nums[k] < temp:
                        j += 1
                    elif nums[j] + nums[k] > temp:
                        k -= 1
                    else:
                        result.append([nums[i],nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while nums[j] == nums[j-1]:
                            j += 1
                        while nums[k] == nums[k+1]:
                            k -= 1
        return result
    
    def fourSum(self, nums, target):
        nums, result, temp, temp2 = sorted(nums), [], 0, []
        for i in range(0, len(nums)-3):
            temp = target - nums[i]
            if temp > 0 and nums[i] != nums[i+1]:
                temp2 = self.threeSum(nums[i+1:], temp)
                temp2 = [ [nums[i]] + x for x in temp2]
                result += temp2
        return result
    
if __name__ == '__main__':
    result = solution().threeSum([-1, 0, 1, 1, 1, 1, 2, -1, -4, 7, 7, 10, -8, 12, 4, 8, 7, 3], 2)
    result1 = solution().fourSum([-1, 0, 1, 1, 1, 1, 2, -1, -4, 7, 7, 10, -8, 12, 4, 8, 7, 3], 2)
    print result, result1
