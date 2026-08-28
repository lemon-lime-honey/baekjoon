#include <vector>
#include <set>
#include <iostream>

using namespace std;

int solution(vector<int> numbers) {
    set<int> seen{0, 1, 2, 3, 4, 5, 6, 7, 8, 9};
    int answer = 0;
    
    for (auto i = numbers.begin(); i != numbers.end(); i++) {
        seen.erase(*i);
    }
    
    for (auto i = seen.begin(); i != seen.end(); i++) {
        answer += *i;
    }
    
    return answer;
}