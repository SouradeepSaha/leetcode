typedef long long ll;

class FenwickTree {

private:
    vector<int> ft;
    int LSB(int x) {return (x & (-x));}
    
public:
    FenwickTree(int n) {
        ft.assign(n+1, 0);
    }
    
    void update(int index, int del) {
        //cout << index << endl;
        while (index < ft.size()) {
            ft[index] += del;
            index += LSB(index);
        }
    }
    
    int prefixSum(int index) {
        int sum = 0;
        while (index > 0) {
            sum += ft[index];
            index -= LSB(index);
        }
        //cout << index << " " << sum << endl;
        return sum;
    }
    
};

class Solution {

public:
    int countRangeSum(vector<int>& nums, int lower, int upper) {
        vector<ll> sum(nums.size()+1, 0);
        for (int i = 0; i < nums.size(); i++) sum[i+1] = sum[i]+nums[i];
        vector<ll> sortedSum(sum.begin(), sum.end());
        sort(sortedSum.begin(), sortedSum.end());
        
        FenwickTree ft(sum.size());
        
        int result = 0, curIndex, lowerIndex, upperIndex;
        ll curElem;
        for (int i = 0; i < sum.size(); i++) {
            
            curElem = sum[i];
            curIndex = upper_bound(sortedSum.begin(), sortedSum.end(), curElem)-sortedSum.begin();
            
            lowerIndex = ft.prefixSum(lower_bound(sortedSum.begin(), sortedSum.end(), curElem-upper) - sortedSum.begin());
            upperIndex = ft.prefixSum(upper_bound(sortedSum.begin(), sortedSum.end(), curElem-lower) - sortedSum.begin());
            result += upperIndex-lowerIndex;
            //cout << "here " << endl;
            ft.update(curIndex, 1);
        }
        return result;
        
    }
};
