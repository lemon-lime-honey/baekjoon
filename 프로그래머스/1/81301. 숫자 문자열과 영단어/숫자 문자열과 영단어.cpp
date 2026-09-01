#include <string>
#include <cctype>
#include <vector>

using namespace std;

int solution(string s) {
    vector<string> nums = {"zero", "one", "two", "three", "four",
                           "five", "six", "seven", "eight", "nine"};

    int answer = 0;
    int idx = 0;

    while (idx < s.length()) {
        if (isdigit(s[idx])) {
            answer = answer * 10 + s[idx] - '0';
            idx++;
        } else {
            for (int i = 3; i < 6; i++) {
                string chk = s.substr(idx, i);
                bool flag = false;
                for (int j = 0; j < 10; j++) {
                    if (chk == nums[j]) {
                        flag = true;
                        answer = answer * 10 + j;
                        idx += i;
                        break;
                    }
                }
                if (flag) break;
            }
        }
    }
    
    return answer;
}