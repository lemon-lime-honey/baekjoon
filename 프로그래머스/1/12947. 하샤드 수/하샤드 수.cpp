using namespace std;

bool solution(int x) {
    int chk = x;
    int target = 0;
    
    while (chk != 0) {
        target += chk % 10;
        chk /= 10;
    }
    
    return x % target == 0;
}