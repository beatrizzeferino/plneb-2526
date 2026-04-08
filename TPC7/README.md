# TPC - Dicionário Médico

Este trabalho consistiu no desenvolvimento da homepage de uma aplicação web de um **Dicionário Médico**, utilizando Flask (Python), HTML e Bootstrap 5. 

Optou-se por utilizar a página inicial simples como um motor de pesquisa sendo possível consultar a lista de todos os conceitos ou pesquisar por termo.

## Estrutura

A página inicial (`home.html`) contém:

- **Card Centralizado**: Utilização de `flexbox` para centrar verticalmente e horizontalmente o conteúdo;

- **Formulário de Pesquisa**: `Input group` do Bootstrap com campo de texto e botão; 

- **Alerta**: Em caso de termo não presente na base de dados é aberto um alerta informativo através de classe `alert alert-warning`.

- **Botão de Navegação**: Acesso direto à lista completa de conceitos através de classe `btn-primary`.

