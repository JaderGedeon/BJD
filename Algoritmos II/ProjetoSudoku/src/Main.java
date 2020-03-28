/*
Entrega de trabalho
Eu,

Jader Gedeon de Oliveira Rocha

declaro que

todas as respostas são fruto de meu próprio trabalho,
não copiei respostas de colegas externos,
não disponibilizarei minhas respostas para colegas externos e
não realizarei quaisquer outras atividades desonestas para me beneficiar ou prejudicar
outros.
*/

import java.util.Scanner;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        game();

    }

    public static void game() throws IOException {

        Scanner leitor = new Scanner(System.in);

        char tab_primordial[][] = initialize();
        char[][] tabuleiro = new char[9][9];

        for (int i = 0; i < tab_primordial.length; i++)
            for (int j = 0; j < tab_primordial[i].length; j++)
                tabuleiro[i][j] = tab_primordial[i][j];

        boolean operante = false;

        // game loop
        while (!operante) {

            print(tabuleiro, tab_primordial);

            switch (step(tabuleiro, tab_primordial)) {
                case -1:
                    System.out.println("\n\n\n===============[Valores inseridos inválidos, Tente novamente]===============\n");
                    break;
                case 0:
                    System.out.println("\n\n\n==[O número digitado já existe na Linha/Coluna/Quadrante, Tente novamente]==\n");
                    break;
                case 1:
                    System.out.println("\n\n\n==============================[Próxima Jogada]==============================\n");
                    break;
            }

            operante = status(tabuleiro);
        }

    }

    public static char[][] initialize() throws FileNotFoundException, IOException {

        char grade[][] = new char[9][9];

        FileReader leitorChar = new FileReader("boards/easy_1.txt"); // Lê caracter por caracter em ascii de uma linha
        BufferedReader bufferLinha = new BufferedReader(leitorChar); //Bufferiza os caracteres de uma linha, normal, não ascii

        for (int i = 0; i < 9; i++) {
            String linhaGrade[] = (bufferLinha.readLine()).split(" "); //Separa a linha bufferizada e armazena numa array
            for (int j = 0; j < 9; j++) {
                grade[i][j] = linhaGrade[j].charAt(0);
            }
        }

        bufferLinha.close();

        return grade;
    }

    public static void print(char grade[][], char primordial[][]) {

        String Azul = "\u001B[34m";
        String Verde = "\u001B[32m";
        String Ciano = "\u001B[36m";
        String Vermelho = "\u001B[31m";

        String Reset = "\u001B[0m";

        String linha = "               C O L U N A" + Reset + "\n";

        linha += "" + Vermelho + "         1│2│3  4│5│6  7│8│9" + Reset + "\n";
        linha += "       " + Verde + "═════" + Reset + "  " + Ciano + "════" + Reset + "  " + Verde + "═════" + Reset + "\n";

        for (int i = 0; i < 9; i++) {
            switch (i - 2) {
                case 1:
                    linha += "L\nI  ";
                    break;
                case 2:
                    linha += "N  ";
                    break;
                case 3:
                    linha += "H  ";
                    break;
                case 4:
                    linha += "A\n   ";
                    break;
                default:
                    linha += "   ";
                    break;
            }

            linha += "" + Vermelho + (i + 1) + Reset + "  ";
            if (i < 3 || i > 5) {
                linha += "" + Verde + "║" + Reset;
            } else {
                linha += "" + Ciano + "║" + Reset;
            }

            for (int j = 0; j < 9; j++) {
                if (j > 0 && j % 3 == 0) {
                    linha += " ";
                }

                if (j % 3 == 0) {
                    linha += " ";
                } else {
                    linha += "│";
                }

                if (grade[i][j] != '_' && grade[i][j] == primordial[i][j]) {
                    linha += "" + Azul + grade[i][j] + Reset;


                } else {
                    linha += "" + grade[i][j];
                }

            }

            if (i < 3 || i > 5) {
                linha += "" + Verde + " ║\n" + Reset;
            } else {
                linha += "" + Ciano + " ║\n" + Reset;
            }

        }
        linha += "       " + Verde + "═════" + Reset + "  " + Ciano + "════" + Reset + "  " + Verde + "═════" + Reset + "\n";
        System.out.printf(linha);

    }

    public static int step(char grade[][], char primordial[][]) {

        Scanner leitor = new Scanner(System.in);

        try {

            System.out.println("\nDigite a coordenada linha<espaço>coluna de sua jogada: ");
            int lin = (leitor.nextInt() - 1);
            int col = (leitor.nextInt() - 1);

            System.out.println("\nDigite o número que deseja colocar: ");
            String numJogado = leitor.next();

            if (numJogado.charAt(0) != '_' && (Integer.parseInt(numJogado) > 9 || Integer.parseInt(numJogado) < 1) || primordial[lin][col] != '_') {
                return -1;
            }



            if (numJogado.charAt(0) != '_') {
                for (int i = 0; i < 9; i++) {
                    if (grade[lin][i] == numJogado.charAt(0) || grade[i][col] == numJogado.charAt(0)) {
                        return 0;
                    }
                }

                for (int i = (lin / 3) * 3; i < (lin / 3) * 3 + 3; i++) {
                    for (int j = (col / 3) * 3; j < (col / 3) * 3 + 3; j++) {
                        if (grade[i][j] == numJogado.charAt(0)) {
                            return 0;
                        }
                    }
                }
            }

            grade[lin][col] = numJogado.charAt(0);

        } catch (Exception e) {
            System.out.println(e);
            return -1;
        }

        return 1;
    }

    public static boolean status(char grade[][]) {

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (grade[i][j] == '_')
                    return false;
            }
        }
        return true;
    }
}