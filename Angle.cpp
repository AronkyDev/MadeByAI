#include <iostream>
#include <fstream>         // You have to import the libraries by yourself
#include <string>
using namespace std;

// Prendi in input un valore di angolo e determina quale tipo di angolo sia [Translated: take in input an angle and determine which type of angle is it]
int main(){               // You have to create the main function
    int angolo;
    cout << "Insert angle value: ";
    cin >> angolo;
    if (angolo >= 0 && angolo <= 90){
        cout << "Angle of type 0";  // He will say "Angle of type X" and not for example "right angle"
    }
    else if (angolo > 90 && angolo <= 180){
        cout << "Angle of type 1";
    }
    else if (angolo > 180 && angolo <= 270){
        cout << "Angle of type 2";
    }
    else if (angolo > 270 && angolo <= 360){
        cout << "Angle of type 3";
    }
    else{
        cout << "Angle not valid";
    }
    system("PAUSE");         // A little problem, he will replace the system("PAUSE") with the Return 0, causing the script to terminate at the end of execution.
}