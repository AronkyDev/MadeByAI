#include <iostream>
#include <fstream>         // You have to import the libraries by yourself
#include <string>
using namespace std;

// Crea una calcolatrice con tutti i 4 tipi di operazioni [Translated: Make a calculator with all 4 types of operations]

int main(){               // You have to create the main function
    int a, b, c, d;
    char op;
    cout << "Insert the operator (+, -, *, /): ";  // And then the AI will create all from line 9 to line 37
    cin >> op;
    cout << "Enter the first number: ";
    cin >> a;
    cout << "Enter the second number: ";
    cin >> b;

    switch (op)
    {
    case '+':
        c = a + b;
        break;
    case '-':
        c = a - b;
        break;
    case '*':
        c = a * b;
        break;
    case '/':
        c = a / b;
        break;
    default:
        cout << "Operator not valid";
        break;
    }
    cout << "The Result is: " << c << endl;
    system("PAUSE");                     // A little problem, he will replace the system("PAUSE") with the Return 0, causing the script to terminate at the end of execution.
}
