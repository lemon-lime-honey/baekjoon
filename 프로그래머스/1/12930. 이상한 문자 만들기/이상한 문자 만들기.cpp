#include <string>
#include <cctype>

using namespace std;

string solution(string s) {
    int idx = 0;
    
    for (int i = 0; i < s.length(); i++) {
        if (isblank(s[i])) {
            idx = 0;
        } else {
            if (idx % 2 == 1) {
                s[i] = tolower(s[i]);
            } else {
                s[i] = toupper(s[i]);
            }
            idx++;
        }
    }
    
    return s;
}