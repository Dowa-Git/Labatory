#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    int result = 0 ;
    if (!(c - b == 0))
    {
        result = a / (c - b) + 1;
    }
    result = result > 0 ? result : -1;
    cout << result; 
}
//A 설비 B 한대생산비용 C 가격
//1000 70 170
//11
//3 2 1
//-1
//2100000000 9 10
//2100000001

// x = 