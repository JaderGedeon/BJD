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

import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {



        game(0);

    }

    //Função que irá executar a lógica do jogo.
    public static void game(int reiniciado) throws IOException {

        Scanner leitor = new Scanner(System.in);

        //Exibir o manual apenas 1 vez no inicio
        if (reiniciado == 0)
            //Manual
            System.out.println("==================================[Sudoku]==================================\n" +
                "\n" +
                "O objetivo do jogo é a colocação de números de 1 a 9 em cada uma das células vazias\n" +
                "numa grade de 9x9, constituída por 3x3 subgrades chamadas regiões.\n" +
                "\n" +
                "O tabuleiro contém algumas pistas iniciais, que são números inseridos em algumas células,\n" +
                "de maneira a permitir uma indução ou dedução dos números em células que estejam vazias.\n" +
                "\n" +
                "Cada coluna, linha e região só pode ter um número de cada um dos 1 a 9.\n" +
                "\n" +
                "Para importar novos tabuleiros, entre na pasta 'boards/' e clone o Modelo.txt\n" +
                "como base, substituindo os '_' por dígitos no novo arquivo, e também renomeando-o.");

        //Definição do tabuleiro e cópia dele, sendo o primordial a matriz-origem.
        char tab_primordial[][] = initialize();
        char[][] tabuleiro = new char[9][9];

        for (int i = 0; i < tab_primordial.length; i++)
            System.arraycopy(tab_primordial[i], 0, tabuleiro[i], 0, tab_primordial[i].length);

        boolean operante = false;


        // game loop
        while (!operante) {

            print(tabuleiro, tab_primordial);

            //Cada return do Step notifica um diferente mensagem dependendo do return.
            switch (step(tabuleiro, tab_primordial)) {
                case -1:
                    System.out.println("\n\n\n===============[Valores inseridos inválidos, Tente novamente]===============\n");
                    break;
                case 0:
                    System.out.println("\n\n\n==[O número digitado já existe na Linha/Coluna/Quadrante, Tente novamente]==\n");
                    break;
                case 1:
                    operante = status(tabuleiro);
                    if (!operante)
                        System.out.println("\n\n\n==============================[Próxima Jogada]==============================\n");

                    break;
            }

        }

        //Fim de jogo
        System.out.println("\n\n\n================================[Parabéns!!]================================\n");
        print(tabuleiro, tab_primordial);
        System.out.println("\n======================[Deseja jogar novamente? (S/N) ]======================\n");

        String resp = leitor.next();

        //Reiniciar o jogo
        if ("S".equals(resp) || "s".equals(resp))
            game(1);

    }

    //Função que inicializara o tabuleiro do jogo
    public static char[][] initialize() throws FileNotFoundException, IOException {

        char grade[][] = new char[9][9];

        int tabEscolhido = 0;

        //Coloca dentro de uma lista todos os arquivos.txt dentro da paste boards/.

        File diretorio = new File("boards");
        ArrayList < String > tabuleiros = new ArrayList();

        for (File arquivos: diretorio.listFiles()) {
            if (arquivos.getName().endsWith(".txt") && !"Modelo.txt".equals(arquivos.getName()))
                tabuleiros.add(arquivos.getName());
        }

        boolean valorCorreto = false;


        //Testa pra ver se o jogador inseriu o numero de um tabuleiro valido.
        while (!valorCorreto) {
            try {

                Scanner leitor = new Scanner(System.in);

                System.out.println("\n================================[Tabuleiros]================================\n");

                for (int i = 0; i < tabuleiros.size(); i++) {
                    System.out.println("(" + (i + 1) + ") > " + tabuleiros.get(i).substring(0, tabuleiros.get(i).length() - 4));
                }

                System.out.println("\nDigite o número do tabuleiro que deseje jogar: ");
                tabEscolhido = leitor.nextInt();

                if (tabEscolhido > 0 && tabEscolhido <= tabuleiros.size())
                    valorCorreto = true;

            } catch (Exception e) {

            }
            if (!valorCorreto)
                System.out.println("\n===============[Valores inseridos inválidos, Tente novamente]===============");
        }

        System.out.println("\n\n");

        //Faz a leitura do arquivo
        FileReader leitorChar = new FileReader("boards/" + tabuleiros.get(tabEscolhido - 1));
        BufferedReader bufferLinha = new BufferedReader(leitorChar);

        for (int i = 0; i < 9; i++) {
            String linhaGrade[] = (bufferLinha.readLine()).split(" ");
            for (int j = 0; j < 9; j++) {
                grade[i][j] = linhaGrade[j].charAt(0);
            }
        }

        bufferLinha.close();

        return grade;
    }

    //Funcao que ira mostrar o tabuleiro na tela a cada jogada
    public static void print(char grade[][], char primordial[][]) {

        //Corezinhas :3
        String Azul = "\u001B[34m";
        String Verde = "\u001B[32m";
        String Ciano = "\u001B[36m";
        String Vermelho = "\u001B[31m";

        String Reset = "\u001B[0m";

        //Tudo a seguir, realiza a montagem de uma string para aparecer o tabuleiro na tela
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

    //Funcao que realizara cada jogada
    public static int step(char grade[][], char primordial[][]) {

        Scanner leitor = new Scanner(System.in);

        //Testa para ver se o jogador numeros validos
        try {

            System.out.println("\nDigite a coordenada linha<espaço>coluna de sua jogada: Ex:'1 1'");
            int lin = (leitor.nextInt() - 1);
            int col = (leitor.nextInt() - 1);

            System.out.println("\nDigite o número que deseja colocar: ");
            String numJogado = leitor.next();


            //Teste de numeros validos
            if ((numJogado.charAt(0) != '_' && (Integer.parseInt(numJogado) > 9 || Integer.parseInt(numJogado) < 1)) || primordial[lin][col] != '_')
                return -1;


            if (numJogado.charAt(0) != '_' && grade[lin][col] != '_')
                return -1;


            //Teste para ver se não deu erro de Sudoku (Dois numeros na mesma linha/coluna/regiao
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

            //Numero inserido com sucesso
            grade[lin][col] = numJogado.charAt(0);

        } catch (Exception e) {
            return -1;
        }

        return 1;
    }

    //Funcao que ira verificar a vitoria do jogador
    public static boolean status(char grade[][]) {

        //Verifica se o tabuleiro esta sem nenhum '_'
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (grade[i][j] == '_')
                    return false;
            }
        }
        return true;
    }
}