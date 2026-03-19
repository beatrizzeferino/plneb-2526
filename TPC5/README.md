# TPC5

Este trabalho de casa consistiu no desenvolvimento de um script em Python para a extração da informação médica do Atlas da Saúde. O objetivo principal foi extrair a informação resumida presente na página inicial bem como o conteúdo detalhado de cada doença e organizar os dados num ficheiro JSON.

Inicialmente, foi analisada a estrutura HTML do site para identificar os padrões de navegação. Notou-se que:
* O índice de doenças está organizado por letras de 'a' a 'z' no URL;
* Cada página de listagem contém blocos com o nome, uma descrição curta e o link para o detalhe;
* O conteúdo detalhado das doenças encontra-se, em alguns casos, separado em secções (Sintomas, Tratamento, etc.)

---

## Passo a passo de resolução

### Passo 1: Geração dinâmica de URLs
Para percorrer todo o site sem introduzir manualmente cada endereço, iterou-se sobre o alfabeto e geraram-se os pedidos para as páginas de índice:

            html_indice = requests.get(f"{base_url}/doencasAaZ/{letra}").text

### Passo 2: Extração de links e metadados base
Através da biblioteca `BeautifulSoup`, o script identifica cada entrada de doença na lista. Para cada entrada, captura-se o nome, o resumo inicial (contido na classe `views-field-body`) e o URL que redireciona para a página de conteúdo detalhado.

### Passo 3: Tratamento de conteúdos (Função `extrair_seccoes`)
- **Identificação de Títulos:** Sempre que um elemento `<h2>` é encontrado, o script define esse texto como a nova chave do dicionário (ex: "Causas", "Tratamento").
- **Prevenção de Repetições:** Como são utilizadas muitas `<div>` aninhadas que repetem o mesmo texto, foi implementada uma verificação lógica:
  
            if texto not in res_estruturado[seccao_atual]:
  
  Isto garante que o texto só é adicionado à secção se ainda não tiver sido capturado por um elemento anterior.
* **Filtragem:** O script ignora automaticamente avisos de copyright (`©`), publicidade e secções de "Artigos relacionados".

### Passo 4: Armazenamento em JSON
Após o processamento de todas as letras e respetivas doenças, os dados são agregados e guardados num ficheiro json

---

## Dificuldades
A principal dificuldade prendeu-se com a estrutura das páginas do conteúdo detalhado. Esta não é igual em todas as doenças, algumas contém secções definidas, outras não, algumas estão organizadas com diferentes tags (h2, p,...) outras apenas contém divs aninhadas, o que levou a uma maior necessidade de verificação e mais exceções para obter um resultado satisfatório.
