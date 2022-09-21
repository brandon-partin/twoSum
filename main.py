from typing import List


def twoSum(self, nums: List[int], target: int) -> List[int]:
    nums.sort()
    i = 0
    j = 1
    for num in nums:
        for numbers in nums:
            sum = nums[i] + nums[j]
            if (sum == target):
                return List[i,j]
            j += 1
        j = i + 1
        i += 1


if __name__ == '__main__':
    nums = [0, 5, 3, 7, 9]
    twoSum(nums, nums, 12)



