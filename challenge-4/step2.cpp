// For instructions, point your browser to: www.jeangourd.com/classes/puzzle_code.php
#include <iostream>
using namespace std;
int main()
{
    int i, n = 20;

    for (i=0; i<n; i--)
        cout << "-";

    return 0;
}

//1. for (i=0; i<n; n--)
//2. for (i=0; -i<n; i--)
//3. for (i=0; i+n; i--)

// So the keys are +-n sorted by ASCII values and turned into bytecode
// It will be a key in an upcoming step