class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string,vector<string>>mp;

        for(int i=0;i<strs.size();i++){
            vector<int>hash(26,0);
            for(int j=0;j<strs[i].size();j++){
                hash[strs[i][j]-'a']++;
            }
            string s;
            for(auto it:hash)s.push_back(it);
            mp[s].push_back(strs[i]);
        }
        vector<vector<string>>ans;
        for(auto [x,y]:mp){
            ans.push_back(y);
        }
        return ans;

    }
};
