#include <string>
#include <cctype>

using namespace std;

string solution(string s, int n) {
    for (int i = 0; i < s.length(); i++) {
        if (!isalpha(s[i])) continue;
        
        if (isupper(s[i]) && (s[i] - 'A' + n >= 26) ||
            islower(s[i]) && (s[i] - 'a' + n >= 26)) {
            s[i] += n - 26;
        } else {
            s[i] += n;
        }
    }
    
    return s;
}