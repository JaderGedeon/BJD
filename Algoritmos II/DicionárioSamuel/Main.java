/*
Entrega do Trabalho 3- Algoritmos e Programação II
Eu,

Jader Gedeon de Oliveira Rocha

declaro que

todas as respostas são fruto de meu próprio trabalho,
não copiei respostas de colegas externos,
não disponibilizarei minhas respostas para colegas externos e
não realizarei quaisquer outras atividades desonestas para me beneficiar ou 
prejudicar outros.
*/

import java.io.*;

public class Main {
    
    // Função para contar número de valores do array, para reduzir o número de acesso dos ponteiros
    public static int quantDeValores(String v[]) {

        int contador = 0;

        for (String valor: v) {
            if (valor != null) {
                contador++;
            }
        }

        return contador;
    }

    // Busca binária recursiva modificada pra ignorar nulls ao longo do array
    public static int buscaBinariaRecursiva(String palavra, String v[], int i, int f) {

        if (i > f) {
            return -1;
        }

        int indice = (i + f) / 2;

        if (v[indice] == null || palavra.compareTo(v[indice]) > 0) {
            return buscaBinariaRecursiva(palavra, v, i + 1, f);
        } else if (v[indice] == null || palavra.compareTo(v[indice]) < 0) {
            return buscaBinariaRecursiva(palavra, v, i, f - 1);
        } else {
            return 0;
        }
    }
    
    // Insertion Sort modificado para funcionar com a comparação de duas Strings
    public static void ordemPorInsercao(String palavra, String v[]) {
        for (int i = 1; i < quantDeValores(v); i++) {

            String temp = v[i];
            int j = i;

            while ((j > 0) && (v[j - 1].compareTo(temp) > 0)) {
                v[j] = v[j - 1];
                j -= 1;
            }
            v[j] = temp;

        }
    }

    public static void main(String[] args) throws IOException {

        // Leitura do arquivoDeEntrada.txt
        FileReader leitor = new FileReader("arquivoDeEntrada.txt");
        BufferedReader bufferLinha = new BufferedReader(leitor);

        String dicionario[] = new String[1000];

        //Verifica pra ver se a linha que leu era apenas um ".".
        for (String linha = bufferLinha.readLine(); !linha.equals("."); linha = bufferLinha.readLine()) {
            //Para cada palavra no vetor linha, transformada em lowercase e quebrada pelo split.
            for (String palavra: linha.toLowerCase().split(" ")) {
                //Se a busca binária recursiva, utilizando o otimizador de roda apenas o número de itens
                 //que há no vetor retornar -1.
                if (buscaBinariaRecursiva(palavra, dicionario, 0, quantDeValores(dicionario)) == -1) {
                    //Então adiciona no último índice do contador otimizado a palavra
                    dicionario[quantDeValores(dicionario)] = palavra;
                    //E então da o sort
                    ordemPorInsercao(palavra, dicionario);
                }
            }
        }

        bufferLinha.close();
        
        //Output       
        int contador = 0;

        for (String palavra: dicionario) {
            if (palavra != null) {
                System.out.println(palavra);
                contador++;
            }
        }
        System.out.println("total de palavras no dicionario="+contador);

    }
}