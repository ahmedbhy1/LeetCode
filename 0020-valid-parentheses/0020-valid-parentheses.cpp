class Solution {
public:
    bool isValid(string s) {
        vector<int> stack ;
        map<char, char> mp;
        mp[')']='(';
        mp['}']='{';
        mp[']']='[';
        set<char> open = {'(','{','['};
        set<char> close {')','}',']'};

        for (auto i : s){
            if (open.count(i))stack.push_back(i);
            if (close.count(i)){
                if ((stack.size() == 0)||(mp[i] != stack.back())) return false ;
                stack.pop_back();
            }
        }
        if (stack.size())return false;
        return true;
    }
};