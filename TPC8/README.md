# TPC8

Este trabalho consistiu no desenvolvimento da página de pesquisa de uma aplicação web de um **Dicionário Médico**, utilizando Flask (Python), HTML e Bootstrap 5. 

## Estrutura

A página de pesquisar (`pesquisarhtml`) contém:

- **Barra de pesquisa**: onde pode ser inserida a query a pesquisar;

- **Checkboxes combináveis**: que permitem alterar as configurações da pesquisa
    - **Word Boundary**: quando ativa torna a pesquisa limitada à palavra, isto é, apenas mostra resultados cuja pesquisa se encontre isolada por espaços das restantes palavras, não apresentado resultados dentro de uma palavra. 
    Por exemplo, com a checkbox desativada, se for pesquisado 'teste' são apresentados resultados como 'Papanicolaou, teste de' e 'anacatestesia', caso esteja ativa apenas aparece 'Papanicolaou, teste de'.  

    - **Case sensitive**: quando ativa torna a pesquisa sensível a maiúsculas e minúsculas , isto é, apresenta todos os resultados independentemente das letras estarem como maiúsculas ou minúsculas.
    Por exemplo, com a checkbox desativada, se for pesquisado 'adn' são apresentados resultados como 'ADN' e 'adnato', caso esteja ativa apenas aparece 'adnato'.

## Resultados
Para facilitar a interpretação dos resultados obtidos, a query pesquisada aparece destacada a bold e highlighted (com as tags `<bold>` e `<mark>`). Optou-se pela combinação das tags pois, com a fonte maior da designação, apenas o bold não se tornava tão visível.
