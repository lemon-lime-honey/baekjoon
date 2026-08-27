#include <iostream>
#include <string>

using namespace std;
int solution(int n)
{
    int answer = 0;
    std::string str = std::to_string(n);
    
    for (int i = 0; i < str.length(); i++) {
        answer += str[i] - '0';
    }

    return answer;
}