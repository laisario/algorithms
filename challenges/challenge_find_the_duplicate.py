def find_duplicate(nums):
    if not nums or isinstance(nums, int) or len(nums) < 2:
        return False
    n = len(nums)
    ordered_nums = sorted(nums)
    for number in range(0, n - 1):
        if isinstance(ordered_nums[number], str) or ordered_nums[number] < 1:
            return False
        if ordered_nums[number] == ordered_nums[number + 1]:
            return ordered_nums[number]
    return False
