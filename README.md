# 🧠 OBI Training

> Repositório dedicado aos meus estudos, treinamentos e soluções de problemas para a **Olimpíada Brasileira de Informática (OBI)**.

![Status](https://img.shields.io/badge/status-em%20treinamento-8b7bf0?style=flat-square)
![Language](https://img.shields.io/badge/language-Python-3776AB?style=flat-square\&logo=python\&logoColor=white)
![OBI](https://img.shields.io/badge/OBI-2026-blue?style=flat-square)
![National](https://img.shields.io/badge/OBI%202026-3%C2%AA%20Fase%20Nacional-gold?style=flat-square)

---

## 🎯 Sobre o projeto

Este repositório reúne minhas **soluções para problemas da OBI**, exercícios de lógica, algoritmos e implementações desenvolvidas durante minha preparação.

A ideia não é apenas guardar respostas, mas **registrar minha evolução na resolução de problemas**: desde exercícios mais básicos até problemas que exigem estruturas de dados, estratégias de otimização e raciocínio algorítmico.

> 🚀 **Atualmente, estou classificado para a 3ª fase — Fase Nacional da OBI 2026.**
>
> E o treinamento continua. Meu objetivo é seguir resolvendo problemas, corrigindo meus erros e evoluindo cada vez mais em algoritmos e programação competitiva.

---

## 🏆 OBI 2026

Minha trajetória na OBI 2026 foi um dos principais motivos para a criação deste repositório.

### 🥇 2ª Fase

Na 2ª fase da OBI 2026, consegui:

* **4/4 problemas resolvidos**
* **400/400 pontos**
* Classificação para a **3ª fase — Fase Nacional**

Esse resultado aumentou ainda mais meu interesse por **algoritmos e resolução de problemas** e me motivou a continuar treinando.

### 🇧🇷 3ª Fase — Fase Nacional

Atualmente, estou **classificado para a 3ª fase nacional da OBI 2026**.

Agora, o foco é continuar aumentando meu repertório e melhorar principalmente minha capacidade de:

* interpretar problemas;
* encontrar padrões;
* escolher a estratégia adequada;
* analisar complexidade;
* trabalhar com estruturas de dados;
* otimizar soluções;
* lidar com casos extremos;
* escrever soluções corretas sob pressão.

---

## 📚 O que estou estudando

Durante os treinamentos, venho trabalhando com diferentes conceitos de programação e algoritmos, como:

### 🔹 Fundamentos

* Entrada e saída
* Variáveis
* Condicionais
* Loops
* Vetores
* Strings
* Matemática básica
* Simulação

### 🔹 Algoritmos

* Ordenação
* Busca
* Sequências
* Greedy
* Contagem
* Manipulação de números
* Estratégias de otimização

### 🔹 Estruturas de dados

* Arrays
* Listas
* Filas
* Heaps / Priority Queue
* Estruturas auxiliares

### 🔹 Complexidade

Também estou buscando entender não apenas **se uma solução funciona**, mas **por que ela funciona e quanto ela custa** em tempo e memória.

---

## 🗂️ Organização

Este repositório **não segue uma estrutura rígida ou uma ordem fixa**.

Os problemas estão organizados de acordo com a forma como foram sendo estudados e resolvidos durante meu treinamento. Por isso, é possível encontrar soluções:

* diretamente na raiz do repositório;
* dentro de pastas relacionadas à **2ª fase**;
* dentro de pastas relacionadas à **3ª fase**;
* em diferentes diretórios conforme o conteúdo ou momento em que foram estudados.

A organização pode continuar mudando conforme novos problemas e treinamentos forem adicionados.

O foco principal deste repositório é **registrar minha evolução na resolução de problemas**, e não seguir uma estrutura pré-definida.

---

## 💻 Alguns problemas e soluções

### 🔢 Comparação de números

Uma das soluções trabalha com a comparação dos dígitos de dois números para construir os maiores valores possíveis a partir dos dígitos que podem ser mantidos.

A implementação utiliza:

* conversão entre números e strings;
* `zfill()` para igualar o tamanho dos números;
* comparação de caracteres;
* construção dos resultados;
* tratamento de casos em que não existem dígitos disponíveis.

```python
aa = int(input())
bb = int(input())

a_str = str(aa)
b_str = str(bb)

maior = max(len(a_str), len(b_str))

b = b_str.zfill(maior)
a = a_str.zfill(maior)

resultado_a = []
resultado_b = []

for i in range(len(a) - 1, -1, -1):

    if a[i] < b[i]:
        resultado_b.append(b[i])

    elif a[i] > b[i]:
        resultado_a.append(a[i])

    else:
        resultado_b.append(b[i])
        resultado_a.append(a[i])

if not resultado_a:
    resultado_a.append("-1")

if not resultado_b:
    resultado_b.append("-1")
```

---

### ⚖️ Distribuição utilizando Heap

Outra solução utiliza a estrutura de dados **Heap / Priority Queue** através da biblioteca `heapq`.

O objetivo é distribuir os pesos entre diferentes filas, sempre escolhendo a fila que possui o **menor peso acumulado**.

```python
import heapq

heap = [(0, i) for i in range(f)]
heapq.heapify(heap)
```

A cada peso:

1. a fila com menor peso acumulado é retirada do heap;
2. o novo peso é adicionado a essa fila;
3. o peso total é atualizado;
4. a fila retorna para o heap.

Essa abordagem é um exemplo de como uma estrutura de dados adequada pode ajudar a construir uma solução eficiente para um problema de distribuição.

---

## 🧩 Como estou treinando

Mais do que simplesmente conseguir um `Accepted`, quero entender cada solução que implemento.

Durante os treinamentos, busco responder:

> **Por que essa abordagem funciona?**

> **Existe uma solução melhor?**

> **Qual é a complexidade?**

> **O que acontece nos casos extremos?**

> **Qual estrutura de dados faz sentido aqui?**

Esse processo faz parte da minha preparação para evoluir cada vez mais em **algoritmos, programação competitiva e engenharia de software**.

---

## 📈 Evolução

Este repositório está em constante desenvolvimento.

Cada problema resolvido representa mais uma ferramenta adicionada ao meu repertório.

```text
Problema
   ↓
Tentativa
   ↓
Erro
   ↓
Análise
   ↓
Solução
   ↓
Aprendizado
   ↓
Evolução
```

O objetivo é continuar treinando, revisando soluções antigas e aumentando gradualmente a dificuldade dos problemas.

---

## 🚀 Próximos passos

* [ ] Resolver mais problemas da OBI
* [ ] Aumentar gradualmente a dificuldade
* [ ] Estudar novos algoritmos
* [ ] Aprofundar estruturas de dados
* [ ] Melhorar análise de complexidade
* [ ] Revisar soluções antigas
* [ ] Treinar com tempo limitado
* [ ] Continuar a preparação para a Fase Nacional

---

## 👨‍💻 Sobre mim

Sou estudante de **Desenvolvimento de Sistemas** e tenho como objetivo seguir carreira como **Engenheiro de Software**.

Além do desenvolvimento de aplicações, utilizo a programação competitiva para desenvolver principalmente:

* raciocínio lógico;
* resolução de problemas;
* pensamento algorítmico;
* análise de complexidade;
* capacidade de encontrar soluções sob pressão.

Atualmente, além dos meus projetos de desenvolvimento, estou focado em evoluir cada vez mais em **algoritmos através da OBI**.

---

## ⭐ Em constante evolução

> **Este repositório não representa onde eu quero chegar.**
> **Representa o caminho que estou percorrendo para chegar lá.**

### 🇧🇷 Classificado para a 3ª fase nacional da OBI 2026.

**Agora é continuar treinando. 🚀**
