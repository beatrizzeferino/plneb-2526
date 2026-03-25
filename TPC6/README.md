# TPC6

Este trabalho de casa consistiu no desenvolvimento de um script em Python para a extração e análise de personagens presentes no livro Harry Potter e a Pedra Filosofal e construção de uma estrutura de dados que represente a frequência com que diferentes personagens aparecem juntas.

Para realizar esta tarefa, foi utilizada a biblioteca spaCy, mais especificamente o modelo pt_core_news_lg.

---

## Passo a passo de resolução

### Passo 1: Preparação do texto

O ficheiro de texto foi lido e, após a leitura, foi removida a parte inicial (primeiros 2663 caracteres) do documento que não fazia parte da narrativa principal.

O texto resultante foi depois processado pelo modelo de linguagem do spaCy

### Passo 2: Identificação das personagens

Para cada frase identificada pelo spaCy, o script percorre todas as entidades e seleciona apenas aquelas cuja etiqueta corresponde a pessoas (PER). Desta forma, obtém-se uma lista das personagens mencionadas em cada frase.

Para evitar repetições dentro da mesma frase, foi implementada uma verificação que garante que cada personagem aparece apenas uma vez na lista associada à frase.

### Passo 3: Construção da rede de amigos

Após identificar as personagens presentes numa frase, o script considera que todas as personagens dessa lista estão relacionadas entre si.

Assim, para cada personagem encontrada:
- cria-se uma entrada num dicionário caso ainda não exista;
- incrementa-se o contador de interações com todas as outras personagens presentes na mesma frase.

Desta forma, é construída uma estrutura de dados que regista quantas vezes cada par de personagens aparece na mesma frase ao longo do livro.

### Passo 4: Ordenação dos resultados

Depois de processar todo o texto, os resultados são organizados em duas etapas:

1. Ordenação dos amigos de cada personagem:
Para cada personagem, os seus amigos são ordenados por ordem decrescente de frequência de coocorrência.

2. Ordenação global das personagens:
O dicionário principal é também ordenado de acordo com a maior frequência de interação de cada personagem. Assim, as personagens que possuem relações mais fortes aparecem primeiro no resultado final.

### Passo 5: Armazenamento em JSON

Após a construção e organização da estrutura de dados, os resultados são guardados num ficheiro JSON.

---

Dificuldades

A principal dificuldade prendeu-se com a identificação consistente das personagens. O modelo de reconhecimento de entidades não é perfeito e identifica como personagens palavras que não o são, para além de que, por vezes, separa o nome de personagens (por exemplo, nome próprio, apelido ou nome completo).
