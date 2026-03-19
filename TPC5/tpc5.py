import requests, json, time
from bs4 import BeautifulSoup
import re

contagem=0
def extrair_seccoes(soup):
    corpo = soup.find("div", class_="field-name-body") or soup.find("div", class_="node-content")
    if not corpo: return {}

    res_estruturado = {"Introdução": ""}
    seccao_atual = "Introdução"

    todos_elementos = corpo.find_all(['h2', 'p', 'div', 'li'])

    for elemento in todos_elementos:
        texto = elemento.text.strip()

        if not texto or "Artigos relacionados" in texto or "©" in texto:
            continue

        if elemento.name == 'h2':
            seccao_atual = texto.replace(":", "").strip()
            res_estruturado[seccao_atual] = ""
        
        else:
            if texto not in res_estruturado[seccao_atual]:
                prefixo = "\n\n" if res_estruturado[seccao_atual] else ""
                res_estruturado[seccao_atual] += prefixo + texto

    resultado_limpo = {}

    for chave, valor in res_estruturado.items():
        if valor:
            valor=re.sub("\n+", " ", valor)
            resultado_limpo[chave] = valor

    return resultado_limpo


resultado_final = {}
base_url = 'https://www.atlasdasaude.pt'

for letra in "abcdefghijklmnopqrstuvwxyz":
    print(f"A processar letra: {letra.upper()}")
    try:
        html_indice = requests.get(f"{base_url}/doencasAaZ/{letra}").text
        soup_indice = BeautifulSoup(html_indice, "html.parser")
        
        for doenca in soup_indice.find_all("div", class_="views-row"):
            link_tag = doenca.find("div", class_="views-field-title").h3.a
            nome = link_tag.text.strip()
            link_completo = base_url + link_tag['href']
            
            print(f" -> {nome}")

            html_detalhe = requests.get(link_completo).text
            dados = extrair_seccoes(BeautifulSoup(html_detalhe, "html.parser"))

            resultado_final[nome] = {
                "small_desc": doenca.find("div", class_="views-field-body").text.strip() if doenca.find("div", class_="views-field-body") else "",
                "full_desc": dados
            }
            contagem+=1

    except Exception as e:
        print(f"Erro na letra {letra}: {e}")

f_out=open("doencas_completo.json", "w", encoding="UTF-8")
json.dump(resultado_final, f_out, indent=4, ensure_ascii=False)
f_out.close()

print(f"Concluído! {contagem} termos tratados")
