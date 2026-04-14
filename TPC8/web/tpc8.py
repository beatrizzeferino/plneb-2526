from flask import Flask, render_template, request, redirect
import json
import re

app=Flask(__name__)

fd_b=open("dicionario_medico.json", "r", encoding="utf-8")
db=json.load(fd_b)


@app.get("/")  #rota para humanos
def homepage():
    return render_template("home.html")

@app.get("/api/conceitos")  #rota para máquina
def conceitos_api():
    return db

@app.get("/conceitos")  
def conceitos():
    return render_template("conceitos.html", conceitos=db.keys())


@app.get("/conceitos/<designacao>")  #link variável
def conceito(designacao):
    if designacao in db:
        descricao = db[designacao]
        return render_template("conceito.html", designacao=designacao, descricao=descricao)
    else:
        return render_template("erro.html", error="O conceito introduzido não existe.")
    
@app.get("/tabela")  
def tabela():
    return render_template("tabela.html", conceitos=db)

@app.get("/pesquisar")  
def pesquisar():
    return render_template("pesquisar.html", conceitos=db)
    

@app.post("/pesquisar")  
def pesquisar_conceitos():
    palavra=request.form['palavra']
    wb = request.form.get('word-boundary')
    cs = request.form.get('case-sensitive') 
    
    pattern = rf"\b{palavra}\b" if wb else palavra #utilizamos rf para usar raw string para as expressões regex e f string para poder passar a variável
 
    resultados = []
    for designacao, descricao in db.items():
        if cs:
            # Case-sensitive - não usa flags
            match_designacao = re.search(pattern, designacao)
            match_descricao = re.search(pattern, descricao)
        else:
            # Case-insensitive - usa re.IGNORECASE
            match_designacao = re.search(pattern, designacao, re.IGNORECASE)
            match_descricao = re.search(pattern, descricao, re.IGNORECASE)
        
        if match_designacao or match_descricao:
            if cs:
                res = {
                    'designacao': re.sub(f"({pattern})", r"<mark><strong>\1</strong></mark>", designacao), #mark e bold para destaque do termo na pesquisa
                    'descricao': re.sub(f"({pattern})", r"<mark><strong>\1</strong></mark>", descricao)
                }
            else:
                res = {
                    'designacao': re.sub(f"({pattern})", r"<mark><strong>\1</strong></mark>", designacao, flags=re.IGNORECASE),
                    'descricao': re.sub(f"({pattern})", r"<mark><strong>\1</strong></mark>", descricao, flags=re.IGNORECASE)
                }
            resultados.append(res)
    
    print(f"Palavra pesquisada: {palavra}, Resultados: {len(resultados)}")
 
    return render_template("pesquisar.html", conceitos=resultados)

@app.post("/conceitos")
def adicionar_conceitos():
    descricao=request.form['descricao']
    designacao=request.form['designacao'] #mesma chave que foi passada como name no forms
    db[designacao]=descricao
    f_out=open("bd.json", "w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    return render_template("conceitos.html", conceitos=db.keys())

@app.delete("/conceitos/<designacao>")
def apagar_conceito(designacao):
    del db[designacao]
    f_out=open("bd.json", "w", encoding="UTF-8")
    json.dump(db, f_out, indent=4, ensure_ascii=False)
    f_out.close()

    return {"redirect_url": "/conceitos", "message": "Conceito apagado com sucesso!"}

    

app.run(host="localhost", port=4002, debug=True)