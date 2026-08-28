#include <vector>

using namespace std;

vector<int> solution(vector<int> num_list) {
    vector<int> answer;
    
    while (!num_list.empty()) {
        int idx = num_list.size() - 1;
        answer.emplace_back(num_list.at(idx));
        num_list.pop_back();
    }
    
    return answer;
}