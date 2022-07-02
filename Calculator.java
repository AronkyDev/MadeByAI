package TikTok;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int num1, num2, risultato;
        char operatore;
        boolean flag = true;
        while (flag) {
            System.out.println("Inserisci il primo numero: ");
            num1 = input.nextInt();
            System.out.println("Inserisci l'operatore: ");
            
            operatore = input.next().charAt(0);
            System.out.println("Inserisci il secondo numero: ");
            num2 = input.nextInt();
            switch (operatore) {
                case '+':
                    risultato = num1 + num2;
                    System.out.println("Il risultato è: " + risultato);
                    break;
                case '-':
                    risultato = num1 - num2;
                    System.out.println("Il risultato è: " + risultato);
                    break;
                case '*':
                    risultato = num1 * num2;
                    System.out.println("Il risultato è: " + risultato);
                    break;
                case '/':
                    risultato = num1 / num2;
                    System.out.println("Il risultato è: " + risultato);
                    break;
                default:
                    System.out.println("Operatore non valido");
                    break;
            }
            System.out.println("Vuoi continuare? (y/n)");
            if (input.next().charAt(0) == 'n') {
                flag = false;
            }
        }
    }
}

// Inserisci il primo numero: 5
// Inserisci l'operatore: +
// Inserisci il secondo numero: 6
// Il risultato è: 11
// Vuoi continuare? (y/n)y
// Inseris