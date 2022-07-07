#include <iostream>

using namespace std;

int main()
{
    int Input;
    cin >> Input;

    int Result = 1;
    int Temp = 1;
    while(Temp < Input)
    {
        Temp += 6 * Result++;
    }
    cout << Result;
}

// int main()
// {
//     int Input;
//     cin >> Input;
//     int Result = 0;
//     if(Input == 1)
//     {
//         Result = 1;
//     }
//     else
//     {
//         for (int i = 1 ; i < 50000; ++i)
//         {
//             int MinNumber = 2 + (6 * (i - 1) * i / 2);
//             int MaxNumber = 1 + (6 * i * (i + 1) / 2);
//             if(Input <= MaxNumber && Input >= MinNumber)
//             {
//                 Result = i;
//                 break;
//             }
//         }
//         Result++;
//     }
//     cout << Result;
// }
// 1            1          ~   1 + 6*0      0
// 2 ~ 7        2          ~   1 + 6*1      1
// 8 ~ 19       2 + 6*1    ~   1 + 6*3      2
// 20 ~ 37      2 + 6*3    ~   1 + 6*6      3
// 38 ~ 61      2 + 6*6    ~   1 + 6*10     4
// 62 ~         2 + 6*10   ~   1 + 6*15     5

// 13 3
// 35 4

// 36  -> 6 / 6 0 

// 0 1 3 6