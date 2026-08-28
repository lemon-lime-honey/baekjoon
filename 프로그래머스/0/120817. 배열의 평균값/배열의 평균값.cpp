#include <vector>

using namespace std;

double solution(vector<int> numbers) {
    double answer = 0;
    
    for (auto i = numbers.begin(); i != numbers.end(); i++) {
        answer += *i;
    }
    
    answer /= numbers.size();
    
    return answer;
}