#include <iostream>

using namespace std;

int main()
{
    int Input;
    cin >> Input;
    int Sum = 0;
    int Counter = 0;
    while(Sum < Input)
    {
        Counter++;
        Sum += Counter;
    }
    int x, y, MoveCount;
    MoveCount = Input - (Sum - Counter + 1);
    x = Counter % 2 == 0 ? 1 + MoveCount : Counter - MoveCount;
    y = Counter % 2 == 0 ? Counter - MoveCount : 1 + MoveCount;

    cout << x << "/" << y << endl;
}
/*
1/1
1/2
2/1
3/1
2/2
1/3
1/4 
2/3 
3/2
*/
/*
0,0
1,0
0,1
0,2
1,1
2,0
3,0

*/