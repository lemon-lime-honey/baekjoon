#include <string>
#include <vector>

using namespace std;

string solution(vector<int> food) {
    string answer = "";

    for (int i = 1; i < food.size(); i++) {
        if (food[i] == 0 || food[i] == 1) continue;
        for (int j = 0; j < food[i] / 2; j++) {
            answer += i + '0';
        }
    }
    
    answer += '0';
    answer += string(answer.rbegin() + 1, answer.rend());
    
    return answer;
}