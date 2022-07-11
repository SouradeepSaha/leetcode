#include <iostream>

using namespace std;

class NumArray {
private:
    vector<int> ft;
    int LSB(int x){
        return (x & (-x));
    }
    
    int prefixSum(int i) {
        int sum = 0;
        while (i > 0) {
            sum += ft[i];
            i -= LSB(i);
        }
        return sum;
    }

public:
    NumArray(vector<int>& nums) {
        ft.push_back(0);
        for (int num : nums) ft.push_back(num);
        for (int i = 1; i <= nums.size(); i++) {
            int j = i + LSB(i);
            if (j < ft.size()) {
                ft[j] += ft[i];
            }
        }
    }
    
    void update(int index, int val) {
        int diff = val-sumRange(index, index);
        index = index+1;
        while (index < ft.size()) {
            ft[index] += diff;
            index += LSB(index);
        }
    }
    
    int sumRange(int left, int right) {
        return prefixSum(right+1)-prefixSum(left);
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * obj->update(index,val);
 * int param_2 = obj->sumRange(left,right);
 */
