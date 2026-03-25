import spacy
import json

nlp = spacy.load("pt_core_news_lg")

file = open(r"..\..\Aula_6\Harry Potter e A Pedra Filosofal.txt", "r", encoding="utf8")
texto = file.read()
texto_limpo=texto[2663:] #foram retirados os primeiros 2663 caracteres referentes a informações adicionais, começando a análise apenas na história
doc=nlp(texto_limpo)

dictio = {}

for sent in doc.sents:
    personagens = []

    for entity in sent.ents:
        if entity.label_ == "PER":
            if entity.text not in personagens:
                personagens.append(entity.text)

    for personagem in personagens:
        if personagem not in dictio:
            dictio[personagem] = {}
        
        for amigo in personagens:
            if amigo != personagem:
                if amigo not in dictio[personagem]:
                    dictio[personagem][amigo] = 1
                else:
                    dictio[personagem][amigo] += 1


#Ordenar os amigos do personagem por frequência de aparições na mesma frase
for personagem in dictio:
    dictio[personagem] = dict(sorted(dictio[personagem].items(), key=lambda x: x[1],reverse=True))

#Ordenar os personagens pelo amigo com maior frequência
dictio = dict(sorted(dictio.items(),key=lambda x: max(x[1].values()) if x[1] else 0,reverse=True))
    
f_out = open("HarrysFriends.json", "w", encoding="utf8")
json.dump(dictio, f_out, indent=4, ensure_ascii=False)
f_out.close()