class Solution {
public:

    vector<int>v;
    bool mark[20] = {0};
    vector<vector<int>> ans;
    int n;
    void F(int sz,vector<int>& nums)
    {
        if(sz==n)
        {
            ans.push_back(v);
            return;
        }
        for(int i=0;i<n;i++)
        {
            if(mark[i])continue;

            v.push_back(nums[i]);
            mark[i]=1;
            F(sz+1,nums);
            v.pop_back();
            mark[i]=0;
        }
    }

    vector<vector<int>> permute(vector<int>& nums)
    {
        n = nums.size();
        F(0,nums);
        return ans;
    }
};
