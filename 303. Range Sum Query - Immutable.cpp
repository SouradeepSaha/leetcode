class NumArray {
private:
    vector<int> prefixSum;    
public:
    NumArray(vector<int>& nums) {
        prefixSum.push_back(0);
        int cumFreq = 0;
        for (int num : nums){
            cumFreq += num;
            prefixSum.push_back(cumFreq);
        }
    }
    
    int sumRange(int left, int right) {
        return prefixSum[right+1]-prefixSum[left];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(left,right);
 */
