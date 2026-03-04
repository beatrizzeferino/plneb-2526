import re
import json

f=open("dicionario_medico.txt", "r", encoding="utf8")
texto = f.read()

# Passo 1: Remoção das quebras de página
texto = re.sub(r'\f', '', texto)

# Passo 2: Remoção das quebras de linhas nas descrições
texto = re.sub(r'\n([a-zà-ú])', r' \1', texto)

# Passo 3: Remoção de linhas vazias
texto = re.sub(r'\n\s*\n', '\n', texto)

# Passo 4: Marcação dos termos com @
texto = re.sub(r'\n([^A-Z\n]+)\n([A-ZÀ-Ú])', r'\n\n@\1\n\2', texto)

# Criação do dicionário
conceitos = re.split(r'\n\n@', texto)
conceitos_dict = {}

for conceito in conceitos[1:]:
    conteudo_conceito = conceito.strip()
    partes = conteudo_conceito.split('\n', 1)
        
    if len(partes) == 2:
        designacao = partes[0].strip()
        descricao = partes[1].replace('\n', ' ').strip()
        conceitos_dict[designacao] = descricao

# Criação do ficheiro JSON
def escreve_json(dict, filename):
    ficheiro=open(filename, "w",  encoding="utf8")
    json.dump(dict, ficheiro, indent=4, ensure_ascii=False)

escreve_json(conceitos_dict, "dicionario_medico_tpc3.json")