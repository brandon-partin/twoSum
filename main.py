from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # val : index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return


if __name__ == '__main__':
    p = Solution()
    nums = [0, 5, 3, 7, 9]
    print(p.twoSum(nums, 12))



