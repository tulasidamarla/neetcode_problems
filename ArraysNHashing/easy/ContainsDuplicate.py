from typing import List


# This approach takes O(N) time complexity and O(N) space complexity
# Sorting approach takes nlogn time complexity hence not taken that route.
# Brute force takes n^2 time complexity

def containsDuplicate(nums: List[int]) -> bool:
    hashset = set()
    for num in nums:
        if num in hashset:
            return True
        hashset.add(num)
    return False


def main():
    nums = [1, 2, 3, 1]
    print("Input ", nums)
    print("Contains duplicate: ", containsDuplicate(nums))
    nums = [1, 2, 3, 4]
    print("Input ", nums)
    print("Contains duplicate: ", containsDuplicate(nums))
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print("Input ", nums)
    print("Contains duplicate: ", containsDuplicate(nums))


main()
