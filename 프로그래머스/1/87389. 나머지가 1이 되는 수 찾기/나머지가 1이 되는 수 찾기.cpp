using namespace std;

int solution(int n) {
    int chk = 1;
    
    while (n % chk != 1) {
        chk++;
    }
    
    return chk;
}