/*
Entrega de trabalho
Nós,

Jader Gedeon de Oliveira Rocha

declaramos que

todas as respostas são fruto de nosso próprio trabalho,
não copiamos respostas de colegas externos à equipe,
não disponibilizamos nossas respostas para colegas externos à equipe e
não realizamos quaisquer outras atividades desonestas para nos beneficiar ou prejudicar
outros.
*/

import java.util.Scanner;
import java.io.*;

public class Main {

    public static void main(String[] args) throws IOException {

        game();
        /*
        Game: Tudo
        Initialize: Escolher diferentes arquivos
        Print: Tudo
        Step: Tudo
        Status: Tudo       
        */

        /* CÓDIGO PRA EXIBIR COMO ESTÁ O TABULEIRO
        String linha = "";
        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                linha += " "+tabuleiro[i][j];
            }
            linha += "\n";
        }
        System.out.println(linha);
        
        */

    }
    /*
   função que irá executar a lógica deste jogo e chamar todos as funções 
   descritas a seguir dentro de um gameloop. 
   */
    public static void game() throws IOException {

        Scanner ler = new Scanner(System.in);

        char tabuleiro[][] = initialize();
        
        boolean operante = true;

        // game loop
        while (operante) {

            
            
            
            
            
            
            
            operante = status(tabuleiro);
        }
        
    }

    /*
    A função initialize() deverá fazer a leitura da grade armazenada em um arquivo texto e devolver
    uma matriz 9x9 já com os valores iniciais. Para que o jogo fique desafiador tente criar arquivos com
    configurações com grau de dificuldade diferentes. Abaixo segue um exemplo de arquivo de entrada as
    posições estão separadas por espaço em branco e a posição vazia é definida usando o caractere ‘_’ underline.
    Exemplo de arquivo de entrada:
    
    5 3 _ _ 7 _ _ _ _
    6 _ _ 1 9 5 _ _ _
    _ 9 8 _ _ _ _ 6 _
    8 _ _ _ 6 _ _ _ 3
    4 _ _ 8 _ 3 _ _ 1
    7 _ _ _ 2 _ _ _ 6
    _ 6 _ _ _ _ 2 8 _
    _ _ _ 4 1 9 _ _ 5
    _ _ _ _ 8 _ _ 7 9
    */

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
    
    /*
    A função status() verifica se o jogador já solucionou o quebra-cabeça, ou seja, não existe posições
    vazias na matriz. Caso o jogador tenha cumprido o objetivo do jogo a função retorna true, ou false caso
    contrário
    */
    
    public static boolean status(char grade[][]){
        return false;
    }
}