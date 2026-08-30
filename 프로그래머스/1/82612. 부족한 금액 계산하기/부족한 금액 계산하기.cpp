using namespace std;

long long solution(int price, int money, int count)
{
    long long cost = (long long)price * (count + 1) * count / 2;
    
    if (money >= cost) return 0;
    
    return cost - money;
}