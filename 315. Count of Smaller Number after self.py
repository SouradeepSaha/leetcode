#include <iostream>
using namespace std;

class Solution {
private:
    vector<int> counts;
public:
    
    vector<int> mergeSort(vector<int>& nums, int left, int right) {
        vector<int> result;
        if (left == right) result.push_back(left);
        else {
            int mid = int((left+right)/2);
            vector<int> leftVec = mergeSort(nums, left, mid);
            vector<int> rightVec = mergeSort(nums, mid+1, right);
            
            int i=0, j=0, k=0;
            
            while (i < leftVec.size() and j < rightVec.size()) {
            
                if (nums[leftVec[i]] <= nums[rightVec[j]]){
                    counts[leftVec[i]] += j;
                    result.push_back(leftVec[i++]);
                } 
                else result.push_back(rightVec[j++]);
                k++;
            }

            while(i < leftVec.size()) {
                counts[leftVec[i]] += j;
                result.push_back(leftVec[i++]);
            }
            while(j < rightVec.size()) result.push_back(rightVec[j++]);
            
        }
        return result;
        
    }
    
    vector<int> countSmaller(vector<int>& nums) {
        counts.assign(nums.size(), 0);
        mergeSort(nums, 0, nums.size()-1);
        return counts;
    }
    
};
