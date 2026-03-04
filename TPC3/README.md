# TPC3

Este trabalho de casa consistiu no desenvolvimento de código, utilizando o módulo re, que permitisse a extração de informação de um ficheiro em formato de texto para uma ficheiro JSON, separando o conteúdo em termo e descrição.

Incialmente foi analisado o ficheiro texto para entender o padrão de formatação do conteúdo. Assim, notou-se que:
* Termos encontram-se isolados numa linha, esta iniciada por duas quebras de linha (\n\n) e por letra minúscula;
* Descrições na(s) linha(s) imediatamente abaixo, iniciadas por uma letra maiúscula;

## Passo a passo de resolução
### Passo 1: Remoção das quebras de página
Foram removidas todas as quebras de página do ficheiro através da expressão 

            re.sub(r'\f', '', texto)

### Passo 2: Remoção das quebras de linhas nas descrições
Notou-se que algumas descrições se encontravam divididas com quebras de linha. Assim, foi utilizada a expressão 

            re.sub(r'\n([a-zà-ú])', r' \1', texto)

para as unir.

A expressão procura um quebra de linha seguida de uma letra minúscula e, quando encontra, substitui a quebra de linha por um espaço. Esta expressão funciona pois as descrições iniciam-se com uma letra maiúscula, logo não serão apanhadas pela expressão e os termos começam com letra minúscula mas são antecedidos por \n\n, não sendp também estes apanhamos pela expressão.

### Passo 3: Remoção de linhas vazias
Foram removidas linhas vazias que pudessem existir através da expressão 

            re.sub(r'\n\s*\n', '\n', texto)

para evitar que estas possam alterar a separação dos termos.

### Passo 4: Marcação dos termos com @
De modo a ser possível distinguir os termos das descrições, foi inserido o símbolo @ antes de todos os termos através da expressão 

            re.sub(r'\n([^A-Z\n]+)\n([A-ZÀ-Ú])', r'\n\n@\1\n\2', '\n' + texto)

A expressão procura um quebra de linha seguida de algo que não seja uma maiúscula ou quebra de linha seguida de uma quebra de linha e uma maiúscula e, quando encontra, coloca um @ antes do termo. Esta expressão funciona pois, na primeira parte, não permite maiúsculas para evitar apanhas as descrições e, na segunda parte, obriga a ter uma maiúscula para confirmar que o termo vem seguido de uma descrição.

## Dificuldades
É de ressaltar foram notados alguns casos excecionais no ficheiro como, por exemplo:
* O termo Å é uma letra maiúscula, o que deveria falhar em algumas expressões mas, uma vez que contém um acento, este não entra na expressão [A-Z]. No entanto, em termos que iniciem por letra maiúscula sem acento, não funcioraria.
* O termo "ficações terminais dos brônquios, apresentando cal" não apresenta descrição então aparece colado ao termo seguinte "ficiforme"

Para estas exceções, as expressões escolhidas podem falhar pelo que estes casos devem ser tidos em atenção de forma individual.