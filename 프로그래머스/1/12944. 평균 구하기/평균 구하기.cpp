#include <vector>

using namespace std;

double solution(vector<int> arr) {
    double answer = 0;
    
    for (auto i = arr.begin(); i != arr.end(); i++) {
        answer += *i;
    }
    
    answer /= arr.size();
    
    return answer;
}