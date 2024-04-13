class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int> char_map;
        
        if(s.length()!=t.length()){//cant be anagram if unequal length
            return false;
        }
        for(char ch : s ){
            char_map[ch]++;
        }
        for(char ch : t ){
            char_map[ch]--;
        }

        for(const auto& pair : char_map){
            if(pair.second>0){
                return false;
            }
        }
    

        return true;
    }
};