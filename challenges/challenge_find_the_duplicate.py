def find_duplicate(nums):
    if not nums or isinstance(nums, str) or isinstance(nums, int):
        return False
    for number in nums:
        if number < 0:
            return False