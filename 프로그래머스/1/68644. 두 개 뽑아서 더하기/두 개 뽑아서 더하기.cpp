#include <vector>
#include <set>
#include <algorithm>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    set<int> seen;
    
    for (int i = 0; i < numbers.size() - 1; i++) {
        for (int j = i + 1; j < numbers.size(); j++) {
            int target = numbers[i] + numbers[j];
            if (!seen.contains(target)) {
                answer.emplace_back(target);
                seen.insert(target);
            }
        }
    }
    
    sort(answer.begin(), answer.end());

    return answer;
}