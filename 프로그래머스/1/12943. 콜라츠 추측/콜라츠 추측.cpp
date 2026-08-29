using namespace std;

int solution(int num) {
    if (num == 1) return 0;
    
    long long n = num;
    int answer = 0;
    
    while (true) {
        answer++;
        
        if (n % 2 == 0) {
            n /= 2;
        } else {
            n = n * 3 + 1;
        }
        
        if (n == 1) break;
        
        if (answer == 500) return -1;
    }

    return answer;
}