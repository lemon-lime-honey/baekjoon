#include <vector>

using namespace std;

vector<int> solution(vector<int> arr) 
{
    vector<int> answer;
    
    for (auto i = arr.begin(); i != arr.end(); i++) {
        if (answer.empty() || answer.back() != *i) answer.emplace_back(*i);
    }

    return answer;
}