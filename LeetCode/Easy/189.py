
nums = [1,2,3,4,5,6,7]
# Output: [5,6,7,1,2,3,4]
k = 8
k = k % len(nums)
print(k)
def reverse(nums, start, end):
    while start < end:
        nums[start], nums[end] = nums[end], nums[start]
        start += 1
        end -= 1

reverse(nums, 0, len(nums) - 1)
reverse(nums, 0, k - 1)
reverse(nums, k, len(nums) - 1)
print(nums)