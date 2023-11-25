class Solution:
    def product_except_self(self, nums):
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        result = [1] * len(nums)

        # calculate left products 
        left_product = 1
        for i in range(1, len(nums)):
            left_product *= nums[i - 1]
            left_products[i] = left_product

        # calculate right products 
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            right_products[i] = right_product

        # combine two products 
        for i in range(0, len(nums)):
            result[i] = left_products[i] * right_products[i]

        return result
    
    def product_except_self_2(self, nums):
        result = [1] * len(nums)

        # calculate left products 
        left_product = 1
        for i in range(1, len(nums)):
            left_product *= nums[i - 1]
            result[i] *= left_product

        # calculate right products 
        right_product = 1
        for i in range(len(nums) - 2, -1, -1):
            right_product *= nums[i + 1]
            result[i] *= right_product

        return result

s = Solution();
print(s.product_except_self([1, 2, 3, 4]))
