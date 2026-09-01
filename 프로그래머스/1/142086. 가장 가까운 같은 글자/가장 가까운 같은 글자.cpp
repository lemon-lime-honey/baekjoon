#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    
    answer.emplace_back(-1);
    
    for (int i = 1; i < s.length(); i++) {
        for (int j = i - 1; j >= 0; j--) {
            if (s[i] == s[j]) {
                answer.emplace_back(i - j);
                break;
            }
        }
        
        if (answer.size() != i + 1) answer.emplace_back(-1);
    }
    
    return answer;
}