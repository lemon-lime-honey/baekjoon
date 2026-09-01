#include <vector>
#include <cmath>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> time;

    for (int i = progresses.size() - 1; i >= 0; i--) {
        time.emplace_back(ceil((100.0 - progresses[i]) / speeds[i]));
    }
    
    while (!time.empty()) {
        int cnt = 1;
        int last = time.back();
        
        time.pop_back();
        
        while (!time.empty() && time.back() <= last) {
            cnt++;
            time.pop_back();
        }
        
        answer.emplace_back(cnt);
    }
    
    return answer;
}