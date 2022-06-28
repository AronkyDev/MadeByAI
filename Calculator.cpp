#include <iostream>
#include <fstream>         // You have to import the libraries by yourself
#include <string>
using namespace std;

// Crea una calcolatrice con tutti i 4 tipi di operazioni [Translated: Make a calculator with all 4 types of operations]

int main(){               // You have to create the main function
    int a, b, c, d;
    char op;
    cout << "Inserisci l'operatore (+, -, *, /): ";  // And then the AI will create all from line 9 to line 37
    cin >> op;
    cout << "Inserisci il primo numero: ";
    cin >> a;
    cout << "Inserisci il secondo numero: ";
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
        cout << "Operatore non valido";
        break;
    }
    cout << "Il risultato e' " << c << endl;
    system("PAUSE");                     // A little problem, he will replace the system("PAUSE") with the Return 0, causing the script to terminate at the end of execution.
}