class Solution {
public:
    vector<vector<int>>ans;
    vector<int>v;
    void F(int sz,int last_element,int n,int k)
    {
        if(sz==k)
        {
            ans.push_back(v);
            return;
        }

        for(int i =last_element+1;i<=n;i++)
        {
            v.push_back(i);
            F(sz+1,i,n,k);
            v.pop_back();
        }

    }


    vector<vector<int>> combine(int n, int k) 
    {
        F(0,0,n,k);
        return ans;
    }
};
