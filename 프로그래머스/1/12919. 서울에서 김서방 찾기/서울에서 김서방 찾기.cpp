#include <string>
#include <vector>
#include <format>

using namespace std;

string solution(vector<string> seoul) {
    int answer = 0;

    for (int i = 0; i < seoul.size(); i++) {
        if (seoul[i] == "Kim") {
            answer = i;
            break;
        }
    }
    
    return std::format("김서방은 {}에 있다", answer);
}