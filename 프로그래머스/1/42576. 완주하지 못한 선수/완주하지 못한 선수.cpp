#include <string>
#include <vector>
#include <map>

using namespace std;

string solution(vector<string> participant, vector<string> completion) {
    map<string, int> seen;
    
    for (auto i = completion.begin(); i != completion.end(); i++) {
        if (seen.contains(*i)) {
            seen[*i]++;
        } else {
            seen[*i] = 1;
        }
    }
    
    for (auto i = participant.begin(); i != participant.end(); i++) {
        if (seen.contains(*i) && seen[*i] > 0) seen[*i]--;
        else return *i;
    }
    
    return "";
}