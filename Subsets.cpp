class Solution {
public:
    int n;
    vector<vector<int>>ans;
    vector<int>v;
    void F(int idx,vector<int>& nums)
    {
        if(idx==n)
        {
            ans.push_back(v);
            return;
        }
        v.push_back(nums[idx]);
        F(idx+1,nums);
        v.pop_back();

        F(idx+1,nums);

    }

    vector<vector<int>> subsets(vector<int>& nums) 
    {
        n =(int) nums.size();
        F(0,nums);
        return ans;
    }
};
