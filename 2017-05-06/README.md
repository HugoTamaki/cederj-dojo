
# Problemas

## Encontre o telefone

Em alguns lugares é comum lembrar um número do telefone associando seus dígitos a letras. Dessa maneira a expressão MY LOVE significa 69 5683. Claro que existem alguns problemas, uma vez que alguns números de telefone não formam uma palavra ou uma frase e os dígitos 1 e 0 não estão associados a nenhuma letra.
Sua tarefa é ler uma expressão e encontrar o número de telefone correspondente baseado na tabela abaixo. Uma expressão é composta por letras maiúsculas (A-Z), hifens (-) e os números 1 e 0.
Letras  ->  Número<br/>
ABC    ->  2<br/>
DEF    ->  3<br/>
GHI    ->  4<br/>
JKL    ->  5<br/>
MNO    ->  6<br/>
PQRS    ->  7<br/>
TUV    ->  8<br/>
WXYZ   ->  9<br/>

Entrada
A entrada consiste de um conjunto de expressões. Cada expressão está sozinha em uma linha e possui C caracteres, onde 1 ≤ C ≤ 30. A entrada é terminada por fim de arquivo (EOF).
Saída
Para cada expressão você deve imprimir o número de telefone correspondente.
Exemplo de entrada:
1-HOME-SWEET-HOME  MY-MISERABLE-JOB
Saída correspondente:
1-4663-79338-4663  69-647372253-562
Curiosidades
A frase "The quick brown fox jumps over the lazy dog" é um pangrama (frase com sentido em que são usadas todas as letras do alfabeto de determinada língua) da língua inglesa.


## Caixa Eletrônico

Desenvolva um programa que simule a entrega de notas quando um cliente efetuar um saque em um caixa eletrônico. Os requisitos básicos são os seguintes:
* Entregar o menor número de notas;
* É possível sacar o valor solicitado com as notas disponíveis;
* Saldo do cliente infinito;
* Quantidade de notas infinito (pode-se colocar um valor finito de cédulas para aumentar a dificuldade do problema);
* Notas disponíveis de R$ 100,00; R$ 50,00; R$ 20,00 e R$ 10,00
Exemplos:
* Valor do Saque: R$ 30,00 – Resultado Esperado: Entregar 1 nota de R$20,00 e 1 nota de R$ 10,00.
* Valor do Saque: R$ 80,00 – Resultado Esperado: Entregar 1 nota de R$50,00 1 nota de R$ 20,00 e 1 nota de R$ 10,00.
