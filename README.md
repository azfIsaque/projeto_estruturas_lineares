# projeto_estruturas_lineares
Projeto de estruturas lineares da aula de Programação de Computadores da faculdade de Ciência da Computação
# 💻 Desafios de Lógica e Estruturas de Dados em Python
Este repositório contém três scripts em Python que resolvem problemas clássicos de programação, abordando desde lógica condicional básica até a implementação prática de estruturas de dados fundamentais (Pilhas e Filas).

---

## 📂 Visão Geral dos Projetos

### 1. Sistema de Votação (`desafio_01_votacao.py`)
* **Qual problema o programa resolve:** Simula um sistema de urna eletrônica simples. Ele permite que o usuário registre votos contínuos para três candidatos predefinidos (Ana, Bruno, Carlos) até que o comando de encerramento ("Fim") seja acionado. Ao final, contabiliza os votos e declara o vencedor (ou empate).
* **Quais estruturas foram utilizadas:** O programa utiliza **variáveis primitivas (inteiros)** como acumuladores/contadores e estruturas de controle de fluxo (`while` para o loop contínuo e `if/elif/else` para validação e lógica de vitória).
* **Exemplo simples de entrada e saída:**
    * *Entrada:* `Ana` -> `Bruno` -> `Ana` -> `Fim`
    * *Saída:*
        ```text
        Resultado da votação:
        Ana: 2 votos
        Bruno 1 votos
        Carlos 0 votos
        O vencedor é: Ana.
        ```

### 2. Editor de Texto com Pilha (`desafio_02_editor_pilha.py`)
* **Qual problema o programa resolve:** Simula a função de um editor de texto básico com a funcionalidade de "Desfazer" (Undo). Ele insere palavras e permite remover sempre a última palavra digitada, seguindo o princípio **LIFO** (*Last In, First Out* - O último a entrar é o primeiro a sair).
* **Quais estruturas foram utilizadas:** * **Pilha (Stack):** Implementada nativamente através de uma **Lista** (`list`) do Python, utilizando os métodos `.append()` para empilhar (inserir palavra) e `.pop()` para desempilhar (remover a última palavra).
    * **Tupla (`tuple`):** Para armazenar de forma imutável as opções do menu.
* **Exemplo simples de entrada e saída:**
    * *Entrada:* Opção `1` (Digitar "Olá") -> Opção `1` (Digitar "Mundo") -> Opção `3` (Mostrar texto).
    * *Saída:* `Texto atual: Olá Mundo`
    * *Entrada:* Opção `2` (Desfazer)
    * *Saída:* `Palavra removida: Mundo`

### 3. Fila de Atendimento Acadêmico (`desafio_03_fila_atendimento.py`)
* **Qual problema o programa resolve:** Simula o sistema de chamadas de uma secretaria, organizando os alunos por ordem de chegada. Segue o princípio **FIFO** (*First In, First Out* - O primeiro a entrar é o primeiro a sair).
* **Quais estruturas foram utilizadas:** * **Fila (Queue):** Implementada através de uma **Lista** (`list`) do Python, utilizando `.append()` para enfileirar (adicionar ao final) e `.pop(0)` para desenfileirar (remover o primeiro elemento da lista).
    * **Tupla (`tuple`):** Para o menu de opções.
* **Exemplo simples de entrada e saída:**
    * *Entrada:* Opção `1` (Digitar "João") -> Opção `1` (Digitar "Maria") -> Opção `3` (Mostrar fila).
    * *Saída:* ```text
        Fila atual:
        1° - João
        2° - Maria
        ```
    * *Entrada:* Opção `2` (Chamar próximo)
    * *Saída:* `Chamando aluno: João`

---

## 🚀 Como executar os programas

**Pré-requisitos:**
Certifique-se de ter o **Python 3.10 ou superior** instalado em sua máquina. Os desafios 2 e 3 utilizam a estrutura de controle `match/case` (introduzida na versão 3.10).

**Passo a passo:**
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git](https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git)
