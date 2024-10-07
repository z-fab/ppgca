# Projeto Análise de Árvores Binárias (BST e AVL)

Projeto da disciplina Algoritmos e Estruturas de Dados do curso de pós-graduação em Computação Aplicada (PPGCA) da Universidade Presbiteriana Mackenzie.

---

### Projeto:

Faça um programa para comparar o desempenho das Árvores Binárias de Busca (BST) e das Árvores AVL. O programa deve:

a) Implementar árvores BST e AVL, considerando:

- Nós contendo chave e um payload com informações adicionais.
- Métodos de busca, inserção e cálculo da altura da árvore.

b) Realizar inserções de dados em ambas as árvores, utilizando diferentes tipos de entradas:

- Dados aleatórios.
- Dados ordenados de forma crescente.

c) Marcar os tempos de inserção e busca nas árvores, comparando ambos os métodos em todas as condições de entrada.

d) Gerar um relatório com:

- **i)** Especificações do método utilizado, como equipamento usado, tamanho dos dados, algoritmos, linguagem de programação, etc.
- **ii)** Gráficos que comparem o desempenho de ambas as árvores em termos de tempo de execução e altura.
- **iii)** Análise crítica sobre o desempenho das duas árvores, incluindo quando uma árvore pode ser preferível à outra.

### Conclusões principais:

- A AVL apresentou um desempenho de inserção mais estável, porém com tempo de inserção superior ao da BST devido ao trabalho adicional necessário para manter o balanceamento.
- Em termos de busca, apesar da AVL ter uma estrutura balanceada, não houve uma vantagem clara sobre a BST em todos os casos.
- A BST sofre muito mais com inserções ordenadas, tornando-se desbalanceada e apresentando degradação significativa de desempenho, enquanto a AVL mantém uma altura muito menor.
- A AVL é mais adequada para cenários onde a previsibilidade da altura da árvore é crucial, enquanto a BST pode ser útil em situações onde as inserções são aleatórias e a simplicidade é uma prioridade.

### Requisitos para rodar o projeto:

- Python 3.8+
- Bibliotecas utilizadas:
  - Polars
  - Seaborn
  - Matplotlib

### Instruções de execução:

1. Clone o repositório.
2. Instale as dependências com `poetry install`.
3. Execute o script principal para rodar os testes e gerar os relatórios: `poetry run python src/main.py`.

