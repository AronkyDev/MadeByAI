#include <iostream>
#include <fstream>         // You have to import the libraries by yourself
#include <string>
using namespace std;

// Prendi in input tre valori e fanne la media [Translated: Take in input three values and make the average]

int main(){               // You have to create the main function
    int a, b, c;
    cout << "Enter the three values: ";
    cin >> a >> b >> c;
    int media = (a + b + c) / 3;
    cout << "The average is: " << media << endl;
    system("PAUSE"); // A little problem, he will replace the system("PAUSE") with the Return 0, causing the script to terminate at the end of execution.
}
