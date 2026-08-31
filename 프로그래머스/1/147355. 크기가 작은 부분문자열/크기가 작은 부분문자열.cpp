#include <string>

using namespace std;

int solution(string t, string p) {
    int answer = 0;
    long long target = stoll(p);

    for (int i = 0; i < t.length() - p.length() + 1; i++) {
        if (stoll(t.substr(i, p.length())) <= target) answer++;
    }
    
    return answer;
}