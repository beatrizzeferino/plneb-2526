from flask import Flask, render_template, request, redirect
import json

app=Flask(__name__)

fd_b=open("dicionario_medico.json", "r", encoding="utf-8")
db=json.load(fd_b)


@app.route("/", methods=["GET", "POST"])
def homepage():
    # Se o utilizador submeteu o formulário de pesquisa
    if request.method == "POST":
        termo = request.form.get("inputPesquisa", "").strip()
        
        if termo:
            # Pesquisa case-insensitive
            for conceito in db.keys():
                if conceito.lower() == termo.lower():
                    # Encontrou! Redireciona para a página do conceito
                    return redirect(f"/conceitos/{conceito}")
            
            # Não encontrou: volta para a home com mensagem de erro
            return render_template("home.html", 
                                 conceitos=list(db.keys()),
                                 erro=True,
                                 termo_errado=termo)
    
    # GET normal: mostra a página
    return render_template("home.html", conceitos=list(db.keys()))


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

app.run(host="localhost", port=4002, debug=True)