#include <vector>

using namespace std;

vector<long long> solution(int x, int n) {
    vector<long long> answer;
    int target = x;
    
    while (answer.size() != n) {
        answer.emplace_back(target);
        target += x;
    }

    return answer;
}