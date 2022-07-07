
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int InputCount;
    cin >> InputCount;

    vector<char> UsedArray;
    using UsedArrayIter = vector<char>::iterator;
    int Counter = 0;

    for(int i = 0; i < InputCount; ++i)
    {
        string CurrentInput;
        cin >> CurrentInput;
        // UsedMap.clear();
        UsedArray.clear();
        char PreviousLetter = -1;
        for(string::iterator iter = CurrentInput.begin(); iter != CurrentInput.end();)
        {
            UsedArrayIter Finder = find(UsedArray.begin(), UsedArray.end(), *iter);
            if (Finder == UsedArray.end())
            {
                UsedArray.push_back(*iter);
                PreviousLetter = *iter;
            }
            else
            {
                if(PreviousLetter != *iter)
                {
                    break;
                }
            }
            if(++iter == CurrentInput.end())
            {
                Counter++;
            }
        }
    }
    cout << Counter;
}