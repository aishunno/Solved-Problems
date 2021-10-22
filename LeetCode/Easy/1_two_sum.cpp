#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

// Brute-force solution
// vector<int> twoSum(vector<int>& nums, int target) {
//     for (int i = 0; i < nums.size(); i++)
//     {
//         for (int j = i + 1; j < nums.size(); j++)
//         {
//             if (nums[i] + nums[j] == target)
//             {
//                 return {i, j};
//             }
            
//         }
//     }

//     return {};
// }

class Solution {
public:
    static vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> visited;
        for (int i = 0; i < nums.size(); i ++) {
            int required_number = target - nums[i];

            if (visited.count(required_number) > 0) {
                return {visited.at(required_number), i};
            } else {
                visited[nums[i]] = i;
            }
        }
        return {};
    }
};

int main(void) {
    vector <int> nums = {3, 3};
    int target = 6;
    vector<int> result = Solution::twoSum(nums, target);
    for (auto it: result) {
        cout << it << " ";
    }
    return 0;
}