#include <vector>
#include <map>

using namespace std;

int solution(vector<int> nums)
{
    map<int, int> monster;
    
    for (auto n = nums.begin(); n != nums.end(); n++) {
        if (monster.contains(*n)) monster[*n]++;
        else monster[*n] = 1;
    }
    
    if (monster.size() >= nums.size() / 2) return nums.size() / 2;
    
    return monster.size();
}