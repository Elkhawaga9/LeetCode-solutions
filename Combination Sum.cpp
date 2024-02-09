class Solution {
public:

    vector<int>v;
    vector<vector<int>>ans;
    int curr_sum=0;
    void F(int idx,vector<int>& candidates, int target)
    {
        if(curr_sum==target)
        {

            //sort(v.begin(),v.end());
            ans.push_back(v);
            return;
        }

        for(int i =0;i<(int)candidates.size();i++)
        {
            if(curr_sum<target)
            {
                v.push_back(candidates[i]);
                curr_sum+=candidates[i];
                F(idx+1,candidates,target);
                curr_sum-=candidates[i];
                v.pop_back();
            }
            else 
            { 
                break;
            }
        }


    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) 
    {
        sort(candidates.begin(),candidates.end());
        F(0,candidates,target);
        set<vector<int>>fin;
       for(auto &i:ans)
        {
           sort(i.begin(),i.end());
           fin.insert(i);
        }
        ans.clear();
        for(auto i:fin)
        {
            ans.push_back(i);
        }
        return ans;
    }
};
