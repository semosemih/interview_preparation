# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false
# Constraints:

# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9

# 1. Brute Force
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(num)):
                if nums[i]==nums[j]:
                    return True
        return False

#aslinda burda imleclerden biri her adimda saga kayiyor bu bir for icin digeri de alttaki for bitince bir saga kayan imlec o da ikinci for

#2. Sorting
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        #nums 3 elemanli array ise range(1,3) oluyo yani 1 ve 2 yi sayar yani array in ilk elemanini atlar son eleman da dahil olmak uzere son elemana kadar check eder
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False

# 3. Hash Set
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num) #yani aslinda biz burda her seferinde ayni olmayan elemanlari bu hashlist e ekliyoruz (unique bir list) sonra ayni elemandan birden cok var ise bunu anlamis oluyoruz
        return False

#4. Hash Set Length
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)