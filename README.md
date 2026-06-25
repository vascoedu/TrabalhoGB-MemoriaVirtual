# TrabalhoGB-MemoriaVirtual
Simulador de Memória Virtual em Python

Este projeto consiste na implementação de um simulador de memória virtual, com foco na aplicação prática de conceitos de sistemas operacionais, como paginação, tradução de endereços e gerenciamento de memória.
O simulador permite observar o funcionamento da MMU (Memory Management Unit), incluindo acessos à memória, ocorrência de page faults e substituição de páginas.

---

## Objetivo
Desenvolver um simulador funcional de memória virtual que:

- Modele memória virtual de **1 MB**
- Modele memória principal de **64 KB**
- Implemente a tabela de páginas
- Realize a tradução de endereços
- Detecte e trate *page faults*
- Utilize algoritmo de substituição (FIFO)
- Exiba as operações de forma clara

---

## Conceitos Aplicados
- Memória virtual  
- Paginação  
- MMU (Memory Management Unit)  
- Tabela de páginas  
- Page fault  
- Substituição de páginas (FIFO)  

---

## Modelagem da Memória

### Memória Virtual
- Tamanho total: **1 MB**
- Divisão: **128 páginas de 8 KB**
- Cada processo possui seu próprio espaço de endereçamento

A memória virtual é representada por vetores de bytes, permitindo simular acessos a endereços e identificar páginas e deslocamentos. Essa abordagem facilita o carregamento sob demanda e a detecção de *page faults*.

---

### Memória Principal
- Tamanho total: **64 KB**
- Divisão: **8 frames de 8 KB**

Cada frame pode armazenar uma página de qualquer processo. Como a quantidade de frames é limitada, ocorrem situações frequentes de *page fault* e substituição, tornando a simulação mais realista.

---

## Mapeamento Página → Frame

A tabela de páginas associa:

(Processo, Página) → Frame

- Cada página pode estar carregada ou não
- Garante isolamento entre processos
- Permite identificar rapidamente *page faults*

---

## Funcionamento do Sistema

1. Um processo acessa um endereço virtual  
2. A MMU divide o endereço em:
   - Página
   - Offset  
3. A tabela de páginas é consultada:
   - ✅ Presente → **HIT**
   - ❌ Ausente → **PAGE FAULT**

---

## Page Fault

Quando ocorre:

- Se há frame livre → a página é carregada  
- Se não há → ocorre substituição de página  

---

## Algoritmo de Substituição (FIFO)

- Remove a página mais antiga carregada
- Insere a nova página no frame liberado

Esse algoritmo demonstra de forma clara o comportamento do gerenciamento de memória.

---

## Execução do Programa

Durante a execução, o sistema exibe:

- Processo ativo  
- Endereço virtual  
- Endereço físico  
- HIT ou PAGE FAULT  
- Substituições  
- Conteúdo acessado  

### Exemplo de saída:

[PAGE FAULT] Processo 1, página 0
-> Carregando página no frame 0
[HIT] Processo 1 -> vAddr 1923 => pAddr 1923
Conteúdo lido: 251

---

## Resultados

- Inicialmente: predominância de *page faults*  
- Com o tempo: aumento de *HITs*  
- Após memória cheia:
  - ocorre substituição FIFO  

O comportamento observado confirma o funcionamento correto do sistema.

---

## Conclusão

O simulador demonstra, na prática:

- Tradução de endereços virtuais para físicos  
- Gerenciamento de memória sob demanda  
- Impacto dos *page faults*  
- Funcionamento do algoritmo FIFO  

Além disso, o projeto é modular, simples e pode ser facilmente expandido.

---

## Instruções de Execução:

 - Download do arquivo simulador.py
 - python3 simulador.py no terminal

---

## Apresentação
[Link Video](https://youtu.be/7Yz6JT9Jba8)

---

## Autor
Vasco Graveto
