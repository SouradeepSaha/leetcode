#include <stack>

class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        
        stack<int> monStack;
        vector<int> result;
        
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while (monStack.size() and monStack.top() > nums[i] and monStack.size()-1+n-i >= k) monStack.pop();
            if (monStack.size() < k) monStack.push(nums[i]);
            
        }

        while(monStack.size()) {
            result.push_back(monStack.top());
            monStack.pop();
        }
        reverse(result.begin(), result.end());
        return result;
    }
};
