# Explanation:

# There are only 4 cases to consider.

# Case 1: [1,10000,5,6,7,8,9,2] - It's optimal to grab both from the front.
# Case 2: [2,3,4,5,6,7,10000,1] - It's optimal to grab both from the back.
# Case 3: [2,3,10000,5,6,7,4,1] - It's optimal to grab the max from the front and min from back.
# Case 4: [2,3,1,5,6,7,4,10000] - It's optimal to grab the min from the front and max from back.

# Consider them all and take the minimum.

def minimumDeletions(nums):
        minFromFront = nums.index(min(nums))
        maxFromFront = nums.index(max(nums))
        
        minFromBack = len(nums) - minFromFront - 1
        maxFromBack = len(nums) - maxFromFront - 1 
        
        return min(max(minFromFront, maxFromFront) + 1,  # Case 1
                   max(minFromBack, maxFromBack) + 1,    # Case 2
                   minFromBack + maxFromFront + 2,       # Case 3 
                   minFromFront + maxFromBack + 2)       # Case 4


# print(minimumDeletions([2, 10, 7, 5, 4, 1, 8, 6]))