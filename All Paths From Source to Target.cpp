class Solution {

public:
    int n;
    vector<int>each_path;
    vector<vector<int>>ans;
    void F(int ele,vector<vector<int>>& graph)
    {
        if(ele==n-1)
        {
            each_path.push_back(n - 1);
            ans.push_back(each_path);
            each_path.pop_back();
            return;
        }
        for(int j=0;j<(int)graph[ele].size();j++)
        {
            each_path.push_back(ele);
            F(graph[ele][j],graph);
            each_path.pop_back();
        }
    }

    vector<vector<int>> allPathsSourceTarget(vector<vector<int>>& graph) {
        n = graph.size();
        F(0,graph);
        return ans;
    }
};
