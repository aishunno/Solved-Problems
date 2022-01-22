/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const visited = new Map();

    for(let i = 0; i < nums.length; i++) {
        const req_num = target - nums[i];
        
        if (visited.has(req_num)) {
            return [i, visited.get(req_num)];
        }

        visited.set(nums[i], i);
    }

    return [];
};

// console.log(twoSum([2, 7, 11, 15], 18));
